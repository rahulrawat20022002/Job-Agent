"""Runner for the 8 September 2026 scheduled job search run (top 1, normal cut)."""

from role_configs_08sep import CONFIGS_08SEP
from build_html import build_role


if __name__ == "__main__":
    for cfg in CONFIGS_08SEP:
        try:
            build_role(cfg)
            print(f"  OK: {cfg['folder']}")
        except Exception as e:
            print(f"  FAILED to build {cfg['folder']}: {e}")
