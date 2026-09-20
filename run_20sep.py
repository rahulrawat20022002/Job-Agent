"""Runner for the 20 September 2026 scheduled job search run (top 3, 8-10 backlog cap)."""

from role_configs_20sep import CONFIGS_20SEP
from build_html import build_role


if __name__ == "__main__":
    for cfg in CONFIGS_20SEP:
        try:
            build_role(cfg)
            print(f"  OK: {cfg['folder']}")
        except Exception as e:
            print(f"  FAILED to build {cfg['folder']}: {e}")
