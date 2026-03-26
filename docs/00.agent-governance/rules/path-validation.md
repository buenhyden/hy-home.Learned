# Path Validation Rules

Use this file to validate path integrity and prevent stale references in active governance docs.

## Validation Scope

- Root entrypoints: `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`
- Governance docs: `docs/00.agent-governance/**/*.md`
- Docs index: `docs/README.md`

## Stale Patterns To Block

- Legacy non-numeric docs paths (short-form stage folders from old layouts).
- Invalid template path patterns like parent-directory template shortcuts.
- URI-style filesystem links.

## Commands

### 1. Scan for stale path patterns

```bash
rg -n "docs/(prd|specs|adr|agentic|manuals)|\.\./templates/|file:///" \
  AGENTS.md CLAUDE.md GEMINI.md docs/README.md docs/00.agent-governance \
  --glob '!docs/00.agent-governance/rules/path-validation.md'
```

### 2. Scan for Korean text in English-only governance docs

```bash
rg -n -P "[\\x{AC00}-\\x{D7A3}]" docs/00.agent-governance
```

### 3. Validate thin-root budgets

```bash
wc -l AGENTS.md CLAUDE.md GEMINI.md
```

### 4. Validate markdown links in active governance files

```bash
python - <<'PY'
from pathlib import Path
import re

roots = [
    Path('AGENTS.md'), Path('CLAUDE.md'), Path('GEMINI.md'),
    Path('docs/README.md')
]
roots += list(Path('docs/00.agent-governance').rglob('*.md'))
pattern = re.compile(r'\[[^\]]+\]\(([^)]+)\)')
errors = []
for f in roots:
    text = f.read_text(encoding='utf-8')
    for m in pattern.finditer(text):
        link = m.group(1).split('#', 1)[0]
        if not link or link.startswith(('http://', 'https://', 'mailto:', '#')):
            continue
        p = (f.parent / link).resolve() if not link.startswith('/') else Path(link)
        if not p.exists():
            errors.append((str(f), link))
if errors:
    for f, l in errors:
        print(f"BROKEN: {f} -> {l}")
    raise SystemExit(1)
print('OK: no broken markdown links in active governance docs')
PY
```

## Pass Criteria

- No stale path match outside this file.
- No Korean text in `docs/00.agent-governance/`.
- Root entrypoint files remain thin.
- No broken markdown links in active governance docs.
