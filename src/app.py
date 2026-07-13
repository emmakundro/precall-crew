"""Streamlit UI for the Pre-Call Intelligence Crew.

Run from src/:
    streamlit run app.py
"""
from dotenv import load_dotenv

load_dotenv()

# Tracing must be set up BEFORE importing the crew (instrumentors monkey-patch).
from precall_crew.observability import setup_tracing  # noqa: E402

setup_tracing()

import streamlit as st  # noqa: E402

from precall_crew.crew import PrecallCrew  # noqa: E402

st.set_page_config(page_title="Pre-Call Intelligence Crew", page_icon="📞")

st.title("📞 Pre-Call Intelligence Crew")
st.caption(
    "Three CrewAI agents — researcher, competitive analyst, brief writer — "
    "traced end-to-end in Phoenix."
)

company = st.text_input("Company to research", placeholder="e.g., Booking.com")
meeting_context = st.text_area(
    "Meeting context (who, deal stage, goal)",
    placeholder="e.g., QBR with the ML platform team; goal is expansion into new LLM use cases",
)

if st.button("Generate brief", type="primary", disabled=not company):
    ctx = meeting_context.strip() or (
        "First discovery call; goal is to understand priorities."
    )
    with st.status("Crew running — agent logs stream in the terminal...", expanded=True) as status:
        st.write("1/3 Account researcher: web search + site scrape")
        st.write("2/3 Competitive analyst: landscape + market pressures")
        st.write("3/3 Brief writer: synthesis (no tools)")
        result = PrecallCrew().crew().kickoff(
            inputs={"company": company.strip(), "meeting_context": ctx}
        )
        status.update(label="Brief complete", state="complete")

    st.markdown(result.raw)
    st.download_button(
        "Download brief (.md)",
        result.raw,
        file_name=f"pre_call_brief_{company.strip().replace(' ', '_')}.md",
    )
    try:
        st.caption(f"Token usage: {result.token_usage}")
    except Exception:
        pass
    st.caption("Trace: http://localhost:6006 (Phoenix)")
