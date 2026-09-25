# Contributing

Start with a reproducible issue describing the research question, input, expected behavior and observed result. Remove patient information, private research and API keys. Use synthetic fixtures when possible.

For code changes, add a test that addresses the actual failure or coverage risk. Run `python -m unittest discover -s tests -v` and `python scripts/validate_package.py`. For data adapters, document pagination, caps, identifier normalization, source vintage, failure behavior and terms of use. Preserve the provenance envelope.

For skills, include a realistic prompt, required sources, methodology, output contract, missing-data behavior and a bounded completion criterion. Avoid claims of validated clinical accuracy or investment returns without supporting evidence. Distinguish workflows run by an AI host from deterministic utilities.

A useful new example should teach one difficult interpretation issue. Label fictional data plainly. Keep source excerpts short and licensed appropriately. Do not commit model credentials, personal data or bulk copyrighted source content.
