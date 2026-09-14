"""Renders the English interview-prep copy of the Hirschmann Automation and
Control GmbH Masterarbeit Agentic Pentesting CV/cover letter. Not part of
any scheduled drafting run; no Notion or CSV write."""

from role_configs_hirschmann_en import CONFIGS_HIRSCHMANN_EN
from build_html import build_role


if __name__ == "__main__":
    for cfg in CONFIGS_HIRSCHMANN_EN:
        try:
            build_role(cfg)
            print(f"  OK: {cfg['folder']}")
        except Exception as e:
            print(f"  FAILED to build {cfg['folder']}: {e}")
