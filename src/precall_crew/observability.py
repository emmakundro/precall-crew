"""Optional Phoenix (Arize) tracing. Opt in with PHOENIX_ENABLED=true in .env.

Must be called BEFORE any crewai imports execute agent code — the
OpenInference instrumentors monkey-patch, so order matters.

Requires (only if enabling):
    pip install arize-phoenix openinference-instrumentation-crewai \
        openinference-instrumentation-anthropic   # matches MODEL=anthropic/...
    python -m phoenix.server.main serve           # UI at http://localhost:6006
"""
import os


def setup_tracing() -> None:
    if os.getenv("PHOENIX_ENABLED", "").lower() != "true":
        return
    try:
        from phoenix.otel import register

        register(
            project_name="precall-crew",
            endpoint=os.getenv(
                "PHOENIX_COLLECTOR_ENDPOINT", "http://localhost:6006/v1/traces"
            ),
            auto_instrument=True,
        )
        print("Phoenix tracing ON -> http://localhost:6006")
    except ImportError:
        print(
            "PHOENIX_ENABLED is set but Phoenix packages aren't installed; "
            "running without tracing."
        )
