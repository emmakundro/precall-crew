#!/usr/bin/env python
"""Entry point for the Pre-Call Intelligence Crew.

Run from src/:
    python -m precall_crew.main
"""
from dotenv import load_dotenv

load_dotenv()

# Tracing must be set up BEFORE importing the crew (instrumentors monkey-patch).
from precall_crew.observability import setup_tracing  # noqa: E402

setup_tracing()

from precall_crew.flow import PrecallFlow  # noqa: E402


def run():
    print("=" * 60)
    print("  PRE-CALL INTELLIGENCE CREW")
    print("=" * 60)
    PrecallFlow().kickoff()


if __name__ == "__main__":
    run()
