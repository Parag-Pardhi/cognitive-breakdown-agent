# Cognitive Breakdown Agent

A portfolio-grade task decomposition agent that converts a complex objective into structured, executable steps with dependencies, priorities, risks, and validation checks.

## Features
- Deterministic planning mode that works without an API key
- Optional OpenAI-compatible LLM planning
- Structured JSON output using Pydantic
- Dependency-aware task graph
- Risk and validation sections
- CLI interface
- Unit tests

## Quick start
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python -m cognitive_agent "Build an enterprise RAG application"
```

For LLM mode, copy `.env.example` to `.env` and configure an OpenAI-compatible endpoint and model.

## Architecture
`CLI -> Planner -> LLM adapter (optional) -> Schema validation -> Dependency validation -> JSON/Markdown output`

The default planner is intentionally local and deterministic so the repository can be cloned and demonstrated without paid services.

## Example
```bash
python -m cognitive_agent "Launch a production FastAPI service with authentication"
```

## Testing
```bash
pytest -q
```

## Disclaimer
This is a portfolio implementation of an agentic planning pattern. It does not claim access to private reasoning or proprietary model internals.