"""Read-only stdio MCP adapter using the maintained SDK v1 API.

Install the optional mcp extra. No network listener, file-read tool, background
scheduler, account credentials or model provider is required by this server.
"""
from . import data, valuation, evidence, trials, literature, conference, catalysts


def create_server():
    try:
        from mcp.server.fastmcp import FastMCP
    except ImportError:
        raise SystemExit("Install the optional MCP extra: python -m pip install '.[mcp]'") from None
    server = FastMCP("HH Healthcare Research")

    @server.tool()
    def search_pubmed(query: str, max_records: int = 20) -> dict:
        """Retrieve PubMed metadata/abstracts with query coverage; capped results are partial."""
        return data.pubmed(query, max_records)

    @server.tool()
    def search_clinical_trials(query: str, max_records: int = 20) -> dict:
        """Search ClinicalTrials.gov; completion dates are not promised readout dates."""
        return data.trials(query, max_records)

    @server.tool()
    def get_clinical_trial(nct_id: str) -> dict:
        """Fetch one exact NCT record, including the raw registry document."""
        return data.trial(nct_id)

    @server.tool()
    def query_openfda(endpoint: str, search: str, max_records: int = 20) -> dict:
        """Query a supported openFDA endpoint; event reports do not measure incidence."""
        return data.fda(endpoint, search, max_records)

    @server.tool()
    def discover_cms_datasets(keyword: str) -> dict:
        """Discover CMS API distribution IDs, vintages and dictionary links."""
        return data.cms_discover(keyword)

    @server.tool()
    def sample_cms_dataset(dataset_id: str, filters: dict | None = None, max_records: int = 20) -> dict:
        """Return an explicitly incomplete CMS sample; never treat it as population totals."""
        return data.cms_sample(dataset_id, filters, max_records)

    @server.tool()
    def calculate_rnpv(packet: dict) -> dict:
        """Calculate user-defined cash-flow scenarios with explicit row-level probabilities."""
        return valuation.calculate(packet)

    @server.tool()
    def audit_evidence_packet(packet: dict) -> str:
        """Validate citations and render supplied claim judgments; does not infer claim truth."""
        return evidence.render(packet, "claims")

    @server.tool()
    def compare_trial_documents(packet: dict) -> dict:
        """Compare structured extractions from registry/publication/press-release documents."""
        return trials.compare(packet)

    @server.tool()
    def prepare_literature_review(packet: dict) -> dict:
        """Deduplicate identifiers, retain ambiguity and audit supplied screening decisions."""
        return literature.review(packet)

    @server.tool()
    def triage_conference(packet: dict) -> dict:
        """Keep confirmed public materials and flag repeated trial/cohort combinations."""
        return conference.triage(packet)

    @server.tool()
    def compare_catalyst_snapshots(before: dict, after: dict) -> dict:
        """Compare complete snapshots of the same NCT watchlist without modifying state."""
        return catalysts.diff(before, after)

    @server.tool()
    def prepare_journal_club(packet: dict) -> str:
        """Render a traceable journal-club brief and eight-slide outline from supplied appraisal."""
        return evidence.render(packet, "journal-club")

    return server


def main():
    create_server().run(transport="stdio")


if __name__ == "__main__":
    main()
