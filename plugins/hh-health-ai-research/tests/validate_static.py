#!/usr/bin/env python3
"""Static checks only. Does not access APIs, execute source code, or install software."""
from pathlib import Path
import json, re, hashlib

ROOT = Path(__file__).resolve().parents[1]

def require(condition, message):
    if not condition:
        raise AssertionError(message)

def run():
    manifest = json.loads((ROOT / 'plugin.json').read_text())
    require(manifest['$schema'] == 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json', 'manifest schema')
    require(manifest['name'] == ROOT.name, 'root name mismatch')
    require(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', manifest['name']) is not None, 'invalid package name')
    require(len(manifest['name']) <= 64, 'package name too long')
    require(re.fullmatch(r'(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)', manifest['version']) is not None, 'strict release version')
    require(not ({'skills','mcpServers','apps','interface'} & manifest.keys()), 'nonportable top-level fields')
    ui = manifest['extensions']['com.openai']['interface']
    require(len(ui['shortDescription']) <= 30, 'subtitle too long')
    prompts = ui['defaultPrompt']
    require(isinstance(prompts,str) or (isinstance(prompts,list) and 1 <= len(prompts) <= 3 and all(isinstance(p,str) for p in prompts)), 'invalid prompts')
    skill_files = sorted(ROOT.glob('skills/*/SKILL.md'))
    require(len(skill_files) == 13, 'wrong skill count')
    all_names = set()
    relative_links = 0
    for file in skill_files:
        text = file.read_text(encoding='utf-8')
        require(text.startswith('---\n'), f'frontmatter missing: {file}')
        front = text.split('---',2)[1]
        match = re.search(r'^name:\s*([^\n]+)', front, flags=re.M)
        require(match and match.group(1).strip() == file.parent.name, f'name mismatch: {file}')
        require(re.search(r'^description:\s*\S', front, flags=re.M), f'description missing: {file}')
        require(file.parent.name not in all_names, 'duplicate skill')
        all_names.add(file.parent.name)
        require(len(text.split()) >= 180, f'empty workflow: {file}')
    for file in ROOT.rglob('*'):
        require(not file.is_symlink(), f'symlink: {file}')
        if not file.is_file():
            continue
        require(file.stat().st_size <= 5 * 1024 * 1024, f'oversized file: {file}')
        if file.suffix not in {'.md','.json','.yaml','.py'} and file.name != 'LICENSE':
            raise AssertionError(f'unexpected file type: {file}')
        text = file.read_text(encoding='utf-8')
        for unsafe in ('$'+'{CLAUDE_PLUGIN_ROOT}', '~/' + '.claude/', 'link_'+'6a9d', 'link_'+'6ab3', '-----BEGIN '+'PRIVATE KEY-----'):
            require(unsafe not in text, f'unsafe host path or private marker: {file}')
        if file.suffix == '.md':
            for link in re.findall(r'\]\(([^)]+)\)',text):
                if re.match(r'^[a-z]+:',link) or link.startswith('#'):
                    continue
                path = link.split('#')[0]
                target = (file.parent / path).resolve()
                require(target.is_relative_to(ROOT.resolve()), f'link escapes package: {file}: {link}')
                require(target.exists(), f'broken relative link: {file}: {link}')
                relative_links += 1
    require(not (ROOT/'mcp.json').exists(), 'unexpected MCP registration')
    require(not (ROOT/'.app.json').exists(), 'unexpected app binding')
    provenance = json.loads((ROOT/'provenance.json').read_text())
    require(len(provenance['evidence_modules']) == 12, 'wrong module count')
    require(len(provenance['sources']) == 14, 'wrong reviewed source count')
    for src in provenance['sources']:
        require(re.fullmatch(r'[0-9a-f]{40}',src['git_blob_sha']), 'invalid blob id')
    specs = json.loads((ROOT/'tests/smoke-cases.json').read_text())['cases']
    require(all(c['expected_skill'] in all_names for c in specs), 'unroutable acceptance case')
    print(json.dumps({'status':'PASS','scope':'Static package validation only','skill_count':len(skill_files),'module_count':12,'reviewed_source_count':14,'relative_links_checked':relative_links,'acceptance_specs':len(specs),'live_workflow_tests_run':False},indent=2))

if __name__ == '__main__':
    run()
