from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.googlesearch import GoogleSearch

load_dotenv()

web_agent = Agent(
    model=Groq(id="llama-3.1-70b-versatile"),
    tools=[GoogleSearch()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)
web_agent.print_response("List out popular blogs from person named Achanandhi M in Medium", stream=True)