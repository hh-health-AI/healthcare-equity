"""Read-only public API clients with bounded requests and explicit coverage.

Only allowlisted HTTPS endpoints are fetched; secrets never enter provenance.
The transport can be injected to test pagination and error behavior offline.
"""
import hashlib
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from .common import ResearchError, require, utcnow, digest
from .trials import normalize

HOSTS = {"clinicaltrials.gov", "eutils.ncbi.nlm.nih.gov", "api.fda.gov", "data.cms.gov"}


def check_url(url):
    p = urllib.parse.urlparse(url)
    require(p.scheme == "https" and p.hostname in HOSTS and p.port in (None, 443) and not p.username and not p.password, "Only approved public HTTPS data endpoints are allowed")


def safe_url(url):
    p = urllib.parse.urlparse(url)
    query = [(k, "REDACTED" if k.lower() in {"api_key", "apikey", "email"} else v) for k, v in urllib.parse.parse_qsl(p.query)]
    return urllib.parse.urlunparse(p._replace(query=urllib.parse.urlencode(query)))


class SafeRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        check_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


class Client:
    def __init__(self, timeout=30):
        self.timeout = timeout
        self._last = {}
        self._opener = urllib.request.build_opener(SafeRedirect())

    def get(self, url, params=None, xml=False):
        if params:
            url += "?" + urllib.parse.urlencode(params)
        check_url(url)
        host = urllib.parse.urlparse(url).hostname
        contact = os.getenv("HH_CONTACT", "")
        require("\n" not in contact and "\r" not in contact, "Invalid HH_CONTACT header")
        headers = {"User-Agent": "HH-Healthcare-Research/0.1 (+https://github.com/hh-health-AI/healthcare-equity) " + contact, "Accept": "application/xml" if xml else "application/json"}
        for attempt in range(3):
            pause = max(0, (0.36 if host == "eutils.ncbi.nlm.nih.gov" else 0.12) - (time.monotonic() - self._last.get(host, 0)))
            time.sleep(pause)
            self._last[host] = time.monotonic()
            try:
                with self._opener.open(urllib.request.Request(url, headers=headers), timeout=self.timeout) as r:
                    raw = r.read(64 * 1024 * 1024 + 1)
                require(len(raw) <= 64 * 1024 * 1024, "Upstream response exceeds 64 MiB limit")
                payload = raw.decode("utf-8") if xml else json.loads(raw)
                return payload, {"url": safe_url(url), "retrieved_at": utcnow(), "response_sha256": hashlib.sha256(raw).hexdigest()}
            except urllib.error.HTTPError as e:
                if e.code in (429, 500, 502, 503, 504) and attempt < 2:
                    time.sleep(2 ** attempt)
                    continue
                if e.code == 404 and host == "api.fda.gov":
                    try:
                        body = json.loads(e.read(65536))
                        if body.get("error", {}).get("code") == "NOT_FOUND" and body.get("error", {}).get("message", "").lower() == "no matches found!":
                            return {"results": [], "meta": {"results": {"total": 0}}}, {"url": safe_url(url), "retrieved_at": utcnow(), "http_status": 404, "note": "Validated openFDA no-matches response"}
                    except (ValueError, AttributeError):
                        pass
                raise ResearchError(f"Upstream HTTP {e.code} at {host}; no completeness claim can be made") from None
            except (urllib.error.URLError, TimeoutError, UnicodeDecodeError, json.JSONDecodeError) as e:
                raise ResearchError(f"Upstream transport/format failure at {host}: {type(e).__name__}") from None


def envelope(source, query, records, total, complete, provenance, limitations):
    return {"schema_version": "1.0", "source": source, "query": query, "retrieved_at": utcnow(), "returned": len(records), "total_reported": total, "complete": complete, "completeness_scope": "Records matching this exact source query at retrieval, not all clinical or market evidence", "provenance": provenance, "limitations": limitations, "records": records}


def cap(value, upper=10000):
    require(isinstance(value, int) and not isinstance(value, bool) and 1 <= value <= upper, f"max_records must be 1..{upper}")


def trial(nct_id, client=None):
    require(re.fullmatch(r"NCT\d{8}", nct_id) is not None, "Use an NCT ID with eight digits")
    payload, meta = (client or Client()).get("https://clinicaltrials.gov/api/v2/studies/" + nct_id)
    record = normalize(payload)
    require(record["id"] == nct_id, "Registry returned the wrong trial")
    record["registry_record"] = payload
    return envelope("ClinicalTrials.gov", {"nct_id": nct_id}, [record], 1, True, [meta], ["Registry is sponsor reported and may lag; primary completion is not a readout date."])


def trials(query, max_records=100, client=None):
    cap(max_records)
    require(isinstance(query, str) and query.strip(), "A trial search query is required")
    c, records, provenance, token, seen = client or Client(), [], [], None, set()
    total = None
    while len(records) < max_records:
        params = {"query.term": query, "pageSize": min(1000, max_records - len(records)), "countTotal": "true", "format": "json"}
        if token:
            params["pageToken"] = token
        payload, meta = c.get("https://clinicaltrials.gov/api/v2/studies", params)
        provenance.append(meta)
        require(isinstance(payload.get("studies"), list), "Registry search lacks studies array")
        reported = payload.get("totalCount")
        require(isinstance(reported, int), "Registry search lacks totalCount")
        if total is not None:
            require(reported == total, "Registry result count changed during pagination; rerun")
        total = reported
        batch = [normalize(s) for s in payload["studies"]]
        require(len(batch) <= params["pageSize"], "Registry exceeded requested page size")
        for record in batch:
            require(record["id"] not in seen, "Duplicate registry record across pages; rerun")
            seen.add(record["id"])
        records.extend(batch)
        next_token = payload.get("nextPageToken")
        require(not next_token or (next_token != token and bool(batch)), "Registry pagination made no progress")
        token = next_token
        if not token:
            break
    require(total >= len(records), "Registry count inconsistent with records")
    return envelope("ClinicalTrials.gov", {"term": query, "max_records": max_records}, records, total, not token and len(records) == total, provenance, ["Partial results when capped. Registry dates and sponsor-guided announcement dates are different."])


def _text(node):
    return "" if node is None else "".join(node.itertext()).strip()


def pubmed(query, max_records=100, client=None):
    cap(max_records)
    require(isinstance(query, str) and query.strip(), "A PubMed query is required")
    c = client or Client()
    params = {"db": "pubmed", "term": query, "retmode": "json", "retmax": max_records, "tool": "hh-healthcare-research"}
    key = os.getenv("NCBI_API_KEY")
    if key:
        params["api_key"] = key
    search, meta = c.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi", params)
    result = search.get("esearchresult", {})
    require("count" in result and isinstance(result.get("idlist"), list) and not result.get("ERROR") and not result.get("errorlist"), "PubMed search error or malformed response")
    total, ids = int(result["count"]), result["idlist"]
    require(len(ids) == len(set(ids)), "PubMed returned duplicate IDs")
    require(len(ids) == min(total, max_records), "PubMed search returned an unexplained partial ID set")
    provenance, records = [meta], []
    for start in range(0, len(ids), 100):
        part = ids[start:start + 100]
        fetch_params = {"db": "pubmed", "id": ",".join(part), "retmode": "xml", "tool": "hh-healthcare-research"}
        if key:
            fetch_params["api_key"] = key
        xml, stamp = c.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi", fetch_params, xml=True)
        provenance.append(stamp)
        try:
            root = ET.fromstring(xml)
        except ET.ParseError:
            raise ResearchError("PubMed XML was malformed") from None
        for article in root.findall("PubmedArticle"):
            pmid = _text(article.find("MedlineCitation/PMID"))
            a = article.find("MedlineCitation/Article")
            require(a is not None and pmid, "PubMed article lacks identity")
            doi_value = next((_text(i) for i in article.findall("PubmedData/ArticleIdList/ArticleId") if i.get("IdType") == "doi"), None)
            types = [_text(i) for i in a.findall("PublicationTypeList/PublicationType")]
            records.append({"id": "PMID:" + pmid, "pmid": pmid, "doi": doi_value, "title": _text(a.find("ArticleTitle")), "journal": _text(a.find("Journal/Title")), "publication_date": " ".join(_text(n) for n in a.findall("Journal/JournalIssue/PubDate/*")), "abstract": "\n".join((n.get("Label", "") + ": " if n.get("Label") else "") + _text(n) for n in a.findall("Abstract/AbstractText")), "publication_types": types, "retracted": "Retracted Publication" in types, "related_notices": [{"type": n.get("RefType"), "pmid": _text(n.find("PMID")), "source": _text(n.find("RefSource"))} for n in article.findall("MedlineCitation/CommentsCorrectionsList/CommentsCorrections")], "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"})
    require({r["pmid"] for r in records} == set(ids) and len(records) == len(ids), "PubMed fetch incomplete or unsupported record type; retain query and inspect missing IDs")
    return envelope("PubMed", {"term": query, "translation": result.get("querytranslation"), "max_records": max_records}, records, total, len(records) == total, provenance, ["PubMed indexing and abstracts are not complete full-text evidence. Retraction metadata may lag. A single-database query is not an exhaustive systematic review."])


FDA_ENDPOINTS = {"drug/event", "drug/label", "drug/drugsfda", "drug/enforcement", "device/event", "device/510k", "device/pma", "device/enforcement"}


def fda(endpoint, search, max_records=100, client=None):
    cap(max_records, 1000)
    require(endpoint in FDA_ENDPOINTS, "Unsupported openFDA endpoint")
    require(isinstance(search, str) and search.strip(), "An explicit openFDA search expression is required")
    params = {"search": search, "limit": max_records}
    if os.getenv("OPENFDA_API_KEY"):
        params["api_key"] = os.getenv("OPENFDA_API_KEY")
    payload, meta = (client or Client()).get(f"https://api.fda.gov/{endpoint}.json", params)
    rows, total = payload.get("results"), payload.get("meta", {}).get("results", {}).get("total")
    require(isinstance(rows, list) and isinstance(total, int) and total >= len(rows), "openFDA response missing count or records")
    require(len(rows) <= max_records, "openFDA exceeded requested sample size")
    return envelope("openFDA", {"endpoint": endpoint, "search": search, "max_records": max_records}, rows, total, len(rows) == total, [meta], ["Reports do not establish incidence, causality or comparative safety. Zero matches do not mean zero events. For exact approved label language verify Drugs@FDA approval documents."])


def cms_discover(keyword, client=None):
    require(isinstance(keyword, str) and keyword.strip(), "A CMS catalog keyword is required")
    data, meta = (client or Client()).get("https://data.cms.gov/data.json")
    require(isinstance(data.get("dataset"), list), "CMS catalog lacks dataset array")
    rows = []
    for ds in data["dataset"]:
        if keyword.casefold() in ds.get("title", "").casefold():
            for dist in ds.get("distribution", []):
                url = dist.get("accessURL", "")
                match = re.fullmatch(r"https://data\.cms\.gov/data-api/v1/dataset/([a-f0-9-]{36})/data", url)
                if match:
                    rows.append({"title": ds["title"], "distribution_title": dist.get("title"), "dataset_id": match[1], "url": url, "modified": dist.get("modified", ds.get("modified")), "temporal": dist.get("temporal"), "dictionary": dist.get("describedBy")})
    return envelope("CMS catalog", {"title_contains": keyword}, rows, len(rows), True, [meta], ["Discovery covers matching catalog titles and API distributions only. Validate year, dictionary and dataset vintage before analysis."])


def cms_sample(dataset_id, filters=None, max_records=100, client=None):
    cap(max_records, 5000)
    require(re.fullmatch(r"[a-f0-9]{8}-(?:[a-f0-9]{4}-){3}[a-f0-9]{12}", dataset_id) is not None, "Invalid CMS dataset UUID")
    filters = filters or {}
    require(isinstance(filters, dict), "CMS filters must be an object of exact field/value matches")
    params = {"size": max_records, "offset": 0}
    for field, value in filters.items():
        require(re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", field) is not None, "Invalid CMS filter field")
        require(isinstance(value, (str, int, float)) and not isinstance(value, bool), "CMS filter values must be scalar")
        params[f"filter[{field}]"] = value
    rows, meta = (client or Client()).get(f"https://data.cms.gov/data-api/v1/dataset/{dataset_id}/data", params)
    require(isinstance(rows, list) and all(isinstance(r, dict) for r in rows), "CMS sample lacks expected record list")
    require(len(rows) <= max_records, "CMS returned more than the requested cap")
    for row in rows:
        for field, value in filters.items():
            require(field in row and str(row[field]).casefold() == str(value).casefold(), "CMS returned a row outside the requested filter; do not use this sample")
    return envelope("CMS data sample", {"dataset_id": dataset_id, "filters": filters, "max_records": max_records}, rows, None, False, [meta], ["SAMPLE ONLY: population completeness is unverified even if fewer rows than requested arrive. Do not compute market totals/shares from this output. Inspect dictionary, suppression, payer coverage, period and dataset revisions. Open Payments is not prescription volume."])


def watch_snapshot(ids, client=None):
    require(ids and len(ids) == len(set(ids)), "Supply unique NCT IDs")
    c, records, provenance = client or Client(), [], []
    for rid in sorted(ids):
        r = trial(rid, c)
        record = r["records"][0].copy()
        record.pop("registry_record", None)
        records.append(record); provenance.extend(r["provenance"])
    return {"schema_version": "1.0", "scope": {"source": "ClinicalTrials.gov", "ids": sorted(ids)}, "as_of": utcnow(), "complete": True, "records": records, "provenance": provenance, "records_sha256": digest(records)}
