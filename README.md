# Demo repository for Vulnerability Triage Agent

A tiny Python service that pins known-vulnerable dependency versions on purpose.
Push this folder to its own public GitHub repository and use it as the live demo
and the synthetic benchmark. Expected verdicts live in
`backend/eval/labels/demo-repo.json` in the agent repository.

| Dependency | Used how | Expected |
| --- | --- | --- |
| PyYAML 5.3.1 | `yaml.full_load` in `app/config_loader.py` | CVE-2020-14343 reachable |
| Jinja2 2.11.2 | `Template.render` only, no `urlize` | CVE-2020-28493 not reachable |
| requests 2.25.1 | `requests.get` without a `Session` | CVE-2024-35195 not reachable or needs review |

Verify each label against the advisory yourself before relying on the numbers.
Do not deploy this project.
