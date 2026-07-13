"""Flow wrapper around the Pre-Call Intelligence Crew.

Why a Flow? CrewAI's production guidance: crews for autonomy, Flows for
control. The crew handles the fuzzy research work; the Flow gives
deterministic structure, typed state, and a natural place to add
human-in-the-loop approval before anything customer-facing ships.
"""
from crewai.flow.flow import Flow, listen, start
from pydantic import BaseModel

from precall_crew.crew import PrecallCrew


class PrecallState(BaseModel):
    company: str = ""
    meeting_context: str = ""
    brief: str = ""


class PrecallFlow(Flow[PrecallState]):

    @start()
    def collect_inputs(self):
        self.state.company = input("Company to research: ").strip()
        self.state.meeting_context = input(
            "Meeting context (who, deal stage, goal): "
        ).strip()
        if not self.state.company:
            raise ValueError("A company name is required.")
        if not self.state.meeting_context:
            self.state.meeting_context = (
                "First discovery call; goal is to understand priorities."
            )

    @listen(collect_inputs)
    def run_crew(self):
        result = PrecallCrew().crew().kickoff(
            inputs={
                "company": self.state.company,
                "meeting_context": self.state.meeting_context,
            }
        )
        self.state.brief = result.raw
        # Handy for the 'learnings' slide: what drove cost/latency
        try:
            print("\nToken usage:", result.token_usage)
        except Exception:
            pass

    @listen(run_crew)
    def deliver(self):
        print("\n" + "=" * 60)
        print("  BRIEF COMPLETE -> output/pre_call_brief.md")
        print("=" * 60)
        print(self.state.brief)
