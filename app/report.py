"""Renders a plain-text status report. Uses Jinja2 templates but never the urlize filter."""
from jinja2 import Template

REPORT = Template("Service {{ name }} is {{ status }} ({{ checks }} checks passed)")


def render_report(name: str, status: str, checks: int) -> str:
    return REPORT.render(name=name, status=status, checks=checks)
