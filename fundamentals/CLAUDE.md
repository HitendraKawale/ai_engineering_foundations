# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Part of the `ai-engineering-foundations` monorepo (workspace root: `..`). This `fundamentals/` directory contains standalone Python scripts demonstrating core async and API patterns.

## Commands

The project uses `uv` for dependency management (lockfile at `../uv.lock`, config at `../pyproject.toml`).

```bash
# Install dependencies
uv sync

# Run the async todo demo
uv run python fundamentals/async_todo.py

# Run the notes API (serves on http://0.0.0.0:8000)
uv run python fundamentals/notes_api.py
```

There is no test suite or linter configured yet.

## Architecture

**`async_todo.py`** — pure asyncio demo. `TaskStore` is an in-memory list-backed store; `slow_add` simulates latency. `asyncio.gather()` drives concurrent execution. No external dependencies.

**`notes_api.py`** — FastAPI demo with bearer-token auth. Key elements:
- `verify_key` dependency checks `Authorization: Bearer secretkey` on every route via `Depends(verify_key)`
- In-memory `notes: dict[int, Note]` + `next_id` global state (resets on restart)
- `NoteCreate` / `Note` are Pydantic v2 models for request validation and response serialization

> **Known bugs in `notes_api.py`**: The HTTP verbs are swapped — `create_note` is registered on `GET /notes` and `get_note` on `POST /notes/{id}`. There is also a duplicate `GET /notes` route (FastAPI silently ignores the second one). These are intentional learning artifacts, not accidental.
