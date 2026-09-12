#!/usr/bin/env python3
"""
One-shot patch: fills in the three stubbed role prompts in
src/agents/debate_agent.py (Proponent / Critic / Editor) with full prompts
consistent with the Summarizer's grounding contract, then byte-compiles the
file to prove it's still valid Python.

USAGE:
    # from the ROOT of the Data_analytics_2 repo:
    python fix_debate_prompts.py

It edits src/agents/debate_agent.py IN PLACE (a .bak backup is written first).
"""
import re
import shutil
import sys
import py_compile
from pathlib import Path

TARGET = Path("src/agents/debate_agent.py")

# Each key is the exact stub text currently in the file; the value is the full
# replacement prompt. No literal { } braces (they'd break the f-string).
REPLACEMENTS = {
    "You are Policy Analyst A (Proponent)... (rest of prompt)":
        "You are Policy Analyst A, the Proponent. Build the strongest possible "
        "answer to the QUERY using ONLY the CONTEXT sources below.\n"
        "    - Use only what the sources state; add no outside or prior knowledge.\n"
        "    - Support every factual claim with the exact citation tag from the "
        "source header, e.g. [Source 1: file=..., page=...].\n"
        "    - If the sources do not contain the answer, say clearly that the "
        "information is not found rather than inventing it.\n"
        "    - If a source is in another language, translate its meaning "
        "faithfully; never fabricate or embellish.\n"
        "    - Be specific and well-structured. This is the opening argument the "
        "Critic will scrutinise, so cite tightly and claim only what the sources support.",

    "You are Policy Analyst B (Critic)... (rest of prompt)":
        "You are Policy Analyst B, the Critic. Your job is to attack the "
        "Proponent's answer in the DEBATE HISTORY against the CONTEXT sources - "
        "not to write your own answer.\n"
        "    - Check every claim the Proponent made against the sources. Flag any "
        "claim the sources do not support, any missing or incorrect [Source X] "
        "citation, and any overreach beyond what the text states.\n"
        "    - Point out relevant evidence in the CONTEXT that the Proponent "
        "ignored or misused.\n"
        "    - If the Proponent asserted something not in the sources, call it out "
        "explicitly as unsupported.\n"
        "    - Do not introduce outside knowledge; judge strictly against the "
        "provided sources.\n"
        "    - Be concrete: cite the specific source that contradicts or fails to "
        "support each disputed claim.",

    "You are the Chief Policy Editor... (rest of prompt)":
        "You are the Chief Policy Editor. Write the FINAL, balanced policy brief "
        "that answers the QUERY, reconciling the Proponent's argument and the "
        "Critic's objections in the DEBATE HISTORY.\n"
        "    - Keep only claims supported by the CONTEXT sources. Drop or correct "
        "anything the Critic showed to be unsupported.\n"
        "    - Cite every claim with the exact [Source X: file=..., page=...] tag "
        "from the source header.\n"
        "    - Where the sources are silent or conflicting, say so honestly and "
        "state what cannot be concluded, rather than guessing.\n"
        "    - Use only the sources; add no prior knowledge, and translate "
        "foreign-language sources faithfully without inventing detail.\n"
        "    - Produce a clear, well-structured brief. This is the user-facing "
        "answer - it must be accurate and fully grounded, not a summary of the debate.",
}


def main() -> int:
    if not TARGET.exists():
        print(f"ERROR: {TARGET} not found. Run this from the repo root "
              f"(the folder that contains src/agents/).")
        return 1

    text = TARGET.read_text(encoding="utf-8")

    missing = [stub for stub in REPLACEMENTS if stub not in text]
    if missing:
        print("WARNING: these stubs were not found (already patched?):")
        for m in missing:
            print(f"   - {m}")
    if len(missing) == len(REPLACEMENTS):
        print("Nothing to do - all stubs already gone. Exiting without changes.")
        return 0

    backup = TARGET.with_suffix(".py.bak")
    shutil.copyfile(TARGET, backup)
    print(f"Backup written: {backup}")

    for stub, full in REPLACEMENTS.items():
        if stub in text:
            text = text.replace(stub, full)
            print(f"  patched: {stub[:45]}...")

    TARGET.write_text(text, encoding="utf-8")

    # prove it still compiles
    try:
        py_compile.compile(str(TARGET), doraise=True)
        print("py_compile OK - debate_agent.py is valid Python.")
    except py_compile.PyCompileError as e:
        print("py_compile FAILED - restoring backup.")
        shutil.copyfile(backup, TARGET)
        print(e)
        return 1

    print("\nDone. Now review and commit:")
    print("   git diff src/agents/debate_agent.py")
    print('   git add src/agents/debate_agent.py')
    print('   git commit -m "Fill in Proponent/Critic/Editor debate prompts"')
    print("   git push")
    return 0


if __name__ == "__main__":
    sys.exit(main())
