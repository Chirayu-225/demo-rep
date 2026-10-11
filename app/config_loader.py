"""Loads service configuration from YAML files."""
import yaml


def load_config(path: str) -> dict:
    with open(path, encoding="utf-8") as handle:
        # full_load is the trigger for CVE-2020-14343 in PyYAML < 5.4
        return yaml.full_load(handle)
