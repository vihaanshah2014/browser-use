"""
Simple try of the agent.

@dev You need to add OPENAI_API_KEY to your environment variables.
"""

import logging
import os
import sys

from src.controller.service import ControllerService

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio

from langchain_openai import ChatOpenAI

from src import Agent

logging.basicConfig(level=logging.INFO)

llm = ChatOpenAI(model='gpt-4o-mini')
agent = Agent(
	task='Opening new tabs to search for images of Albert Einstein, Oprah Winfrey, and Steve Jobs. Then ask user for further instructions.',
	llm=llm,
)


async def main():
	result, history = await agent.run()
	print(result)
	print(history)


asyncio.run(main())
