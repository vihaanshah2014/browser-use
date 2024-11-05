import logging
import os
import sys

from langchain_openai import ChatOpenAI

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio

from langchain_anthropic import ChatAnthropic

from src import Agent, Controller

logging.basicConfig(level=logging.INFO)


# Persist the browser state across agents
controller = Controller()

model = ChatOpenAI(model='gpt-4o-mini')

# Initialize browser agent
agent1 = Agent(
	task='Open 3 wikipedia articles about the history of the internet.',
	llm=model,
	controller=controller,
)
agent2 = Agent(
	task='Considering all open tabs give me the names of 2 founders of the companies.',
	llm=model,
	controller=controller,
)


# Let it work its magic
async def main():
	await agent1.run()
	founders = await agent2.run()

	print(founders)


asyncio.run(main())
