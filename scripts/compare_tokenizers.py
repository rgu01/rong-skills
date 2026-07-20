#!/usr/bin/env python3
"""Compare Claude model tokenizers via the count_tokens API.

Feeds the same varied strings to two (or more) models and reports whether they
tokenize each string to the same number of tokens. Identical counts across
varied inputs indicate a shared vocabulary; any difference proves they differ.

Uses the count_tokens endpoint, which is model-specific and returns real Claude
token counts (never use tiktoken — it's OpenAI's tokenizer and is wrong here).

Usage:
    export ANTHROPIC_API_KEY=...        # or run `ant auth login`
    python scripts/compare_tokenizers.py
    python scripts/compare_tokenizers.py claude-opus-4-8 claude-haiku-4-5
"""

import sys

from anthropic import Anthropic

# Varied samples: plain English, structured text, non-English (stresses the
# tokenizer hardest), and code. Add your own to probe further.
SAMPLES = [
    "the project brainstorming",
    "digraph { A -> B; }",
    "こんにちは世界",
    "def retry(max_attempts=3):",
    "supercalifragilisticexpialidocious",
]

DEFAULT_MODELS = ["claude-opus-4-8", "claude-haiku-4-5"]


def count(client: Anthropic, model: str, text: str) -> int:
    """Return the token count for `text` under `model`'s vocabulary."""
    resp = client.messages.count_tokens(
        model=model,
        messages=[{"role": "user", "content": text}],
    )
    return resp.input_tokens


def main() -> int:
    models = sys.argv[1:] or DEFAULT_MODELS
    if len(models) < 2:
        print("Provide at least two model IDs to compare.", file=sys.stderr)
        return 2

    client = Anthropic()

    header = "  ".join(f"{m:>18}" for m in models)
    print(f"{'verdict':<7}  {header}  sample")
    print("-" * (9 + len(header) + 10))

    all_same = True
    for s in SAMPLES:
        counts = [count(client, m, s) for m in models]
        same = len(set(counts)) == 1
        all_same = all_same and same
        cols = "  ".join(f"{c:>18}" for c in counts)
        print(f"{'SAME' if same else 'DIFF':<7}  {cols}  {s!r}")

    print()
    if all_same:
        print("All samples matched: these models share a vocabulary "
              "(on this sample set).")
    else:
        print("At least one sample differed: these models do NOT share a "
              "vocabulary.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
