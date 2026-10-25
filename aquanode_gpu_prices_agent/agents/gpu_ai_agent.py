from pydantic_ai import Agent 
from dotenv import load_dotenv 
from tools.aquanode_tools import getTools 
from prompts.aq_system_prompt import SYSTEM_PROMPT

load_dotenv()

agent = Agent(
    model = 'openai:gpt-5.2',
    tools = getTools(), 
    system_prompt = SYSTEM_PROMPT
)

async def recommendGpus(prompt : str):
    async with agent.run_stream(prompt) as result:
        async for token in result.stream_text(delta=True):
            print(token)