"""Runner for the 26 September 2026 scheduled job search run (top 3, 8-10 gate cap)."""

from role_configs_26sep import CONFIGS_26SEP
from build_html import build_role


if __name__ == "__main__":
    for cfg in CONFIGS_26SEP:
        try:
            build_role(cfg)
            print(f"  OK: {cfg['folder']}")
        except Exception as e:
            print(f"  FAILED to build {cfg['folder']}: {e}")
