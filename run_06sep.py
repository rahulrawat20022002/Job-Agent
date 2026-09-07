"""Runner for the 6 September 2026 scheduled job search run (normal top 3 cut)."""

from role_configs_06sep import CONFIGS_06SEP
from build_html import build_role


if __name__ == "__main__":
    for cfg in CONFIGS_06SEP:
        try:
            build_role(cfg)
            print(f"  OK: {cfg['folder']}")
        except Exception as e:
            print(f"  FAILED to build {cfg['folder']}: {e}")
