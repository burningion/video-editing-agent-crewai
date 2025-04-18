from mcp import StdioServerParameters
from crewai_tools import MCPServerAdapter
from crewai import Agent, Task, Crew
import os

serverparams = StdioServerParameters(
    command="uv",
    args=["run", "video-editor-mcp", os.environ['VJ_API_KEY']],
    env={"UV_PYTHON": "3.11", **os.environ},
)

with MCPServerAdapter(serverparams) as tools:
    # tools is now a list of CrewAI Tools matching 1:1 with the MCP server's tools
    agent = Agent(role="You are a video editing agent",
                  goal="create an exciting edit",
                  backstory="", tools=tools)
    task = Task(agent=agent,
                description="search videos for skateboarding",
                expected_output="a video edit of skateboarding")
    crew = Crew(agents=[agent], tasks=[task])
    crew.kickoff()