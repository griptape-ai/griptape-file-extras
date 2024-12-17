from dotenv import load_dotenv

from griptape.file_extras.tools.open_file_tool import OpenFileTool
from griptape.structures import Agent
from griptape.drivers import OpenAiChatPromptDriver

import os

load_dotenv()

key = "OPENAI_API_KEY"
if not (OPENAI_API_KEY := os.getenv(key)):
    raise ValueError(f"{key} missing")

TEST_IMAGE = "examples/file_extras/tools/open_file_tool/media/capybara_cloud.jpeg"

agent = Agent(
    prompt_driver=OpenAiChatPromptDriver(model="gpt-4o-mini", api_key=OPENAI_API_KEY),
    tools=[OpenFileTool()],
)

agent.run(f"Can you show me the image at {TEST_IMAGE}?")
