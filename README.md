# Pre-Call Intelligence Crew (CrewAI + Phoenix demo)

Multi-agent app for the Arize AI Solutions Manager panel: give it a company
+ meeting context, get a pre-sales call brief built from live web research —
with every agent, task, and LLM call traced in Phoenix (Arize's open-source
observability tool).

## Architecture
Flow (control) → Crew (autonomy) → 3 sequential agents:

1. **account_researcher** (Serper search + website scrape) → research digest
2. **competitive_analyst** (Serper search) → competitive landscape
3. **brief_writer** (no tools — synthesis only) → `output/pre_call_brief.md`

The writer deliberately has no tools: gathering and synthesis are separate
jobs. The Flow wrapper mirrors CrewAI's production guidance — crews for
autonomy, Flows for control.

## Setup
1. Python 3.10–3.13.
2. `pip install -r requirements.txt`
3. Copy `.env.example` to `.env`, fill in `ANTHROPIC_API_KEY` and
   `SERPER_API_KEY` (free key at serper.dev).
4. `mkdir -p src/output` (the brief lands in `output/` relative to where you run).

## Run
Terminal 1 — Phoenix UI:

    python -m phoenix.server.main serve
    # UI at http://localhost:6006

Terminal 2 — the app (from `src/`):

    cd src && mkdir -p output
    streamlit run app.py          # web UI at http://localhost:8501
    # or terminal-only:
    python -m precall_crew.main

Enter a company (try an Arize customer for the QBR-prep demo) and a meeting
context. Watch the verbose agent logs stream, open the brief in
`src/output/pre_call_brief.md`, then walk the trace at http://localhost:6006.

To run without tracing, set `PHOENIX_ENABLED=false` (or remove it) in `.env`.

## Structure
- `src/precall_crew/config/agents.yaml` — 3 agents
- `src/precall_crew/config/tasks.yaml` — 3 sequential tasks
- `src/precall_crew/crew.py` — @CrewBase wiring (YAML keys must match method names)
- `src/precall_crew/flow.py` — Flow wrapper (state + execution order)
- `src/precall_crew/observability.py` — Phoenix tracing (opt-in via env)
- `src/precall_crew/main.py` — terminal entry point (tracing set up before crew import)
- `src/app.py` — Streamlit UI (inputs → run crew → rendered brief + download)
