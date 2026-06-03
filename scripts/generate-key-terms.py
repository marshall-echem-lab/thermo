import re
import sys
from pathlib import Path

TERM_LINE = re.compile(
    r'^\s*\*\*(.+?)\*\*'        # **Term**
    r'(?:\s*(\([^)]*\)))?'      # optional ($symbol$)
    r'\s*(?:—|--)\s*(.*)',       # — definition
)

def extract_key_terms(path: Path) -> list[dict]:
    lines = path.read_text(encoding="utf-8").splitlines()
    terms = []
    i = 0

    while i < len(lines):
        line = lines[i].strip()

        # Look for opening of a .callout-note block
        if re.match(r'^:::\s*\{', line) and ".callout-note" in line:
            inner = []
            i += 1
            depth = 1
            # Collect all lines until the closing :::
            while i < len(lines) and depth > 0:
                s = lines[i].strip()
                if s == ":::":
                    depth -= 1
                elif re.match(r'^:::', s) and len(s) > 3:
                    depth += 1
                    inner.append(lines[i])
                else:
                    inner.append(lines[i])
                i += 1

            # Check heading contains Key Term(s)
            heading = next((l for l in inner if l.strip()), "")
            if not re.search(r'Key Terms?', heading, re.IGNORECASE):
                continue

            # Extract terms from inner lines
            for l in inner:
                if not l.strip() or l.strip().startswith("#"):
                    continue
                m = TERM_LINE.match(l)
                if m:
                    symbol = m.group(2).strip() if m.group(2) else None
                    # Strip outer parens from symbol e.g. ($G$) → $G$
                    if symbol and symbol.startswith("(") and symbol.endswith(")"):
                        symbol = symbol[1:-1]
                    terms.append({
                        "name":       m.group(1).strip(),
                        "symbol":     symbol,
                        "definition": m.group(3).strip(),
                    })
        else:
            i += 1

    return terms

book_dir = Path(".")

all_terms = []
for qmd_file in sorted(book_dir.glob("*.qmd")):
    if qmd_file.name == "key-terms.qmd":
        continue
    print(f"  Scanning {qmd_file.name}...")
    found = extract_key_terms(qmd_file)
    if found:
        print(f"  Found {len(found)} term(s) in {qmd_file.name}")
    all_terms.extend(found)

all_terms.sort(key=lambda t: t["name"].lower())

lines = ["# Key Terms {.unnumbered}\n"]
for t in all_terms:
    header = f"**{t['name']}**"
    if t["symbol"]:
        header += f" ({t['symbol']})"
    lines.append(f"{header}\n:   {t['definition']}\n")

output = Path("key-terms.qmd")
output.write_text("\n".join(lines), encoding="utf-8")
print(f"Generated key-terms.qmd with {len(all_terms)} term(s).")