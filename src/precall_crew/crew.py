from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool, SerperDevTool


@CrewBase
class PrecallCrew:
    """Pre-Call Intelligence Crew: research -> competitive analysis -> brief."""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # --- Agents ---------------------------------------------------------
    # Note: YAML keys must exactly match these method names.

    @agent
    def account_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["account_researcher"],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True,
        )

    @agent
    def competitive_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["competitive_analyst"],
            tools=[SerperDevTool()],
            verbose=True,
        )

    @agent
    def brief_writer(self) -> Agent:
        # Deliberately no tools: gathering and synthesis are separate jobs.
        return Agent(
            config=self.agents_config["brief_writer"],
            verbose=True,
        )

    # --- Tasks ----------------------------------------------------------

    @task
    def research_task(self) -> Task:
        return Task(config=self.tasks_config["research_task"])

    @task
    def competitive_task(self) -> Task:
        return Task(config=self.tasks_config["competitive_task"])

    @task
    def brief_task(self) -> Task:
        return Task(
            config=self.tasks_config["brief_task"],
            output_file="output/pre_call_brief.md",
        )

    # --- Crew -----------------------------------------------------------

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,   # collected from @agent methods
            tasks=self.tasks,     # collected from @task methods, in order
            process=Process.sequential,
            verbose=True,
        )
