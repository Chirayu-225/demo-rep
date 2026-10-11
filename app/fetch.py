"""Fetches remote health endpoints."""
import requests


def check_health(url: str) -> bool:
    response = requests.get(url, timeout=10)
    return response.status_code == 200
