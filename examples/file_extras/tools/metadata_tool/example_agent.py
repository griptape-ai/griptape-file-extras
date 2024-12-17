from dotenv import load_dotenv

from griptape.file_extras.tools.metadata_tool import MetadataTool
from griptape.structures import Agent
from griptape.drivers import OpenAiChatPromptDriver

import os

load_dotenv()

key = "OPENAI_API_KEY"
if not (OPENAI_API_KEY := os.getenv(key)):
    raise ValueError(f"{key} missing")

TEST_IMAGE = (
    "examples/file_extras/tools/metadata_tool/media/capybara_cloud_wMetadata.jpeg"
)

agent = Agent(
    prompt_driver=OpenAiChatPromptDriver(model="gpt-4o-mini", api_key=OPENAI_API_KEY),
    tools=[MetadataTool()],
)

agent.run(
    f'From the metadata for "{TEST_IMAGE}", what value is in the "Keywords" field?'
)
