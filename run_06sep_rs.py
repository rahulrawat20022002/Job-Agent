"""Ad-hoc runner for the Rohde und Schwarz Agentic AI Experiments tailoring on 6 September 2026."""

from role_configs_06sep_rs import CONFIGS_06SEP_RS
from build_html import build_role


if __name__ == "__main__":
    for cfg in CONFIGS_06SEP_RS:
        try:
            build_role(cfg)
            print(f"  OK: {cfg['folder']}")
        except Exception as e:
            print(f"  FAILED to build {cfg['folder']}: {e}")
