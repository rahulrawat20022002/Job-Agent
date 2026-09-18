"""Runner for the 18 September 2026 scheduled job search run (top 4, normal cut)."""

from role_configs_18sep import CONFIGS_18SEP
from build_html import build_role


if __name__ == "__main__":
    for cfg in CONFIGS_18SEP:
        try:
            build_role(cfg)
            print(f"  OK: {cfg['folder']}")
        except Exception as e:
            print(f"  FAILED to build {cfg['folder']}: {e}")
