from app.config_loader import load_config
from app.fetch import check_health
from app.report import render_report


def main() -> None:
    config = load_config("config.yaml")
    healthy = check_health(config["health_url"])
    print(render_report(config["name"], "up" if healthy else "down", 1 if healthy else 0))


if __name__ == "__main__":
    main()
