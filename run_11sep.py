"""Runner for the 11 September 2026 scheduled job search run (top 3, normal cut)."""

from role_configs_11sep import CONFIGS_11SEP
from build_html import build_role


if __name__ == "__main__":
    for cfg in CONFIGS_11SEP:
        try:
            build_role(cfg)
            print(f"  OK: {cfg['folder']}")
        except Exception as e:
            print(f"  FAILED to build {cfg['folder']}: {e}")
