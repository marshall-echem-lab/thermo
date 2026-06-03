import re
from pathlib import Path

CALLOUT_PATTERN = re.compile(
    r":::\s*\{\.callout-note\}.*?\n\s*##\s*Key Term\s*\n(.*?):::",
    re.DOTALL | re.IGNORECASE
)

TERM_PATTERN = re.compile(
    r"\*\*(.+?)\*\*"
    r"(?:\s*\((.+?)\))?"
    r"\s*[—–-]\s*"
    r"(.+)",
    re.DOTALL
)

def extract_key_terms(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    terms = []
    for callout_match in CALLOUT_PATTERN.finditer(text):
        content = callout_match.group(1).strip()
        term_match = TERM_PATTERN.match(content)
        if term_match:
            terms.append({
                "name":       term_match.group(1).strip(),
                "symbol":     term_match.group(2).strip() if term_match.group(2) else None,
                "definition": term_match.group(3).strip(),
            })
        else:
            print(f"  Warning: couldn't parse term in {path.name}: {repr(content[:80])}")
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

lines = ["# Key Terms\n"]
for t in all_terms:
    header = f"**{t['name']}**"
    if t["symbol"]:
        header += f" ({t['symbol']})"
    lines.append(f"{header}\n:   {t['definition']}\n")

output = Path("key-terms.qmd")
output.write_text("\n".join(lines), encoding="utf-8")
print(f"Generated key-terms.qmd with {len(all_terms)} term(s).")