"""Runner for the 18 October 2026 scheduled job search run (top 3, normal cut)."""

from role_configs_18oct import CONFIGS_18OCT
from build_html import build_role


if __name__ == "__main__":
    for cfg in CONFIGS_18OCT:
        try:
            build_role(cfg)
            print(f"  OK: {cfg['folder']}")
        except Exception as e:
            print(f"  FAILED to build {cfg['folder']}: {e}")
