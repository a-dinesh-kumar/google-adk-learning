# Save this inside agent.py
from google.adk.agents import Agent
from pydantic import BaseModel, Field

# 1. Define the internal schema that the agent can read and write to
class UserState(BaseModel):
    user_name: str | None = Field(default=None, description="The extracted name of the user")

root_agent = Agent(
    model="gemini-3.5-flash-lite",
    name="name_extractor",
    # Instruct the model to update the state variable key whenever a name is shared
    instruction="""
    You are a helpful assistant.
    1. If the user tells you their name, extract it and save it to the 'user_name' property in your state schema immediately.
    2. Then, reply with just their name on the first turn.
    3. On subsequent turns, if they ask for their name, read from your state schema and say 'Your name is [name]'.
    """,
    state_schema=UserState, # This parameter handles persistent state memory mutations across turns
)
