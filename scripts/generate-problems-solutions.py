#!/usr/bin/env python3
"""
Pre-render hook: build the "Problems and Solutions" chapter.

Quarto runs pre-render hooks with CWD set to the sub-project dir (the folder
containing this book's _quarto.yml), NOT the repo root. By that point CI has
already staged the shared `problems/` folder into this dir, so we glob it with
a bare path and emit bare include paths (no ../) — per the golden rule (A.4).

Output: problems-solutions.qmd in CWD. It is gitignored and disposable — edit
the source problem files, never this generated chapter. Setting
`show-solutions: true` in its front matter is what reveals the when-meta-gated
solution blocks inside each problem file.
"""
import re
from pathlib import Path

PROBLEMS_DIR = Path("problems")
OUTPUT = Path("problems-solutions.qmd")


def natural_key(path):
    # split into digit / non-digit runs so problem1-2 sorts before problem1-10
    return [int(tok) if tok.isdigit() else tok.lower()
            for tok in re.split(r"(\d+)", path.name)]


def main():
    if PROBLEMS_DIR.is_dir():
        problems = sorted(PROBLEMS_DIR.glob("problem*.qmd"), key=natural_key)
    else:
        # No staged problems/ (e.g. a plain local preview before CI staging).
        # Emit a valid-but-empty chapter so the render still succeeds.
        problems = []

    lines = [
        "---",
        'title: "Problems and Solutions"',
        "show-solutions: true",
        "number-sections: false",
        "---",
        "",
    ]

    if problems:
        for p in problems:
            # bare include path: problems/ is staged inside this project dir
            lines.append(f"{{{{< include problems/{p.name} >}}}}")
            lines.append("")
    else:
        lines.append("_No problems found._")

    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[generate-problems-solutions] wrote {OUTPUT} "
          f"with {len(problems)} problem(s).")


if __name__ == "__main__":
    main()