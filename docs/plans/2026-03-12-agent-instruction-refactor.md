# Agent Instruction Refactor Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Refactor `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` into minimal entrypoints backed by shared, linked documentation under `.claude/`.

**Architecture:** Keep the three root files as stable discovery points because other repository docs already reference them. Move reusable governance and model-specific detail into `.claude/`, then make each root file point to the shared manual set with corrected relative links.

**Tech Stack:** Markdown, repository-relative links, `.agent/rules/`, `.agent/workflows/`, `.claude/`, `docs/guides/`

---

### Task 1: Capture the current documentation defects

**Files:**
- Modify: `AGENTS.md`
- Modify: `CLAUDE.md`
- Create: `GEMINI.md`
- Test: `python3` inline link-check script

**Step 1: Record the broken references before refactoring**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
import re

for file in ["AGENTS.md", "CLAUDE.md", "GEMINI.md"]:
    text = Path(file).read_text()
    links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)
    missing = [link for link in links if not link.startswith(("http", "#")) and not Path(link).exists()]
    print(file, missing)
PY
```

Expected:
- `AGENTS.md` reports the missing `runbooks/` path.
- `CLAUDE.md` reports the missing `.agent/workflows/tdd-workflow.md` path.
- `GEMINI.md` reports the missing `.agent/rules/0120-requirements-and-specifications-standard.md` path.

**Step 2: Confirm the shared-content candidates**

Review:
- shared governance and persona adoption rules in `AGENTS.md`
- model-only directives in `CLAUDE.md`
- model-only directives in `GEMINI.md`

Expected:
- shared rules are separated from Claude-only and Gemini-only overlays.

### Task 2: Create the shared governance manual set in `.claude`

**Files:**
- Create: `.claude/README.md`
- Create: `.claude/shared-governance.md`
- Create: `.claude/claude-code.md`
- Create: `.claude/gemini-models.md`

**Step 1: Create the index**

Add a short README that explains:
- root files remain the canonical entrypoints
- the directory contains the detailed governance and model overlays
- which file to open next for each model

**Step 2: Create shared governance**

Document:
- persona adoption requirement
- spec and planning gate
- rule/workflow/skill triage requirement
- lazy-loading navigation order
- current repository knowledge map using existing paths

**Step 3: Create the Claude overlay**

Document only Claude-specific guidance:
- workflow order
- Python/tooling validation expectations
- when to use `next-devtools`, `context7`, and testing workflows

**Step 4: Create the Gemini overlay**

Document only Gemini-specific guidance:
- planning-first behavior
- `task.md` / `implementation_plan.md` expectations
- `sequential-thinking` usage
- long-context usage with lazy loading

### Task 3: Reduce the three root files to entrypoints

**Files:**
- Modify: `AGENTS.md`
- Modify: `CLAUDE.md`
- Modify: `GEMINI.md`

**Step 1: Refactor `AGENTS.md`**

Keep:
- short project description
- non-negotiable shared rules
- links to the shared manual set

Remove:
- detailed model-specific content
- duplicated navigation detail that now lives in the shared manual

**Step 2: Refactor `CLAUDE.md`**

Keep:
- short Claude-specific entrypoint
- load order
- link to the detailed Claude manual

Remove:
- broken link to `tdd-workflow`
- nonexistent `skills/` reference
- tool names that do not belong in a generic root entrypoint

**Step 3: Refactor `GEMINI.md`**

Keep:
- short Gemini-specific entrypoint
- load order
- link to the detailed Gemini manual

Remove:
- broken standards link
- duplicated governance that now belongs in shared docs

### Task 4: Verify the new structure

**Files:**
- Test: `AGENTS.md`
- Test: `CLAUDE.md`
- Test: `GEMINI.md`
- Test: `.claude/*.md`

**Step 1: Re-run the relative link check**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
import re

files = [
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    ".claude/README.md",
    ".claude/shared-governance.md",
    ".claude/claude-code.md",
    ".claude/gemini-models.md",
]

for file in files:
    text = Path(file).read_text()
    links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)
    missing = [link for link in links if not link.startswith(("http", "#")) and not (Path(file).parent / link).resolve().exists()]
    print(file, missing)
PY
```

Expected:
- every file prints an empty missing-link list

**Step 2: Review for scope control**

Check:
- only the requested three root files and the new shared manual files were changed
- no unrelated template or guide content was rewritten

**Step 3: Remove the deprecated location**

Check:
- deprecated instruction directories have been removed from the active
  documentation chain
- there are no remaining instruction-chain references to removed paths

**Step 4: Commit**

```bash
git add AGENTS.md CLAUDE.md GEMINI.md docs/plans/2026-03-12-agent-instruction-refactor.md .claude
git commit -m "docs(agent): refactor model instruction entrypoints"
```
