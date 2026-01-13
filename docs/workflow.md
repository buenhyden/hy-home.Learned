# Workflow

How to contribute and maintain this knowledge archive.

## ✍️ Contribution Workflow

1. **Create a Branch**:

    ```bash
    git checkout -b chore/add-til-python-uv
    ```

2. **Write Content**:
    - Create a new markdown file in the appropriate directory (e.g., `TIL/2026/...`).
    - Use standard markdown formatting.
3. **Run Checks**:

    ```bash
    pre-commit run --all-files
    ```

4. **Commit**:
    Follow Conventional Commits:

    ```bash
    git commit -m "docs(til): add python uv setup guide"
    ```

## 🤖 AI-Assisted Workflow

### Using Agents

You can use the definitions in `.github/agents/` to prompt your AI assistant (Cursor, Antigravity) to act as a specific persona.

**Example Prompt**:
> @expert-nextjs-developer Help me structure this Next.js study note.

### Using Instructions

Detailed technical instructions are located in `.github/instructions/`. AI agents configured with this repository context will automatically refer to these best practices.
