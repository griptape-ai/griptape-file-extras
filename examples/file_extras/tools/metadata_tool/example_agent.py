from dotenv import load_dotenv

from griptape.file_extras.tools.metadata_tool import MetadataTool
from griptape.file_extras.utils.env_utils import get_env_var
from griptape.structures import Agent
from griptape.drivers import OpenAiChatPromptDriver

load_dotenv()

api_key = get_env_var("OPENAI_API_KEY")

TEST_IMAGE = (
    "examples/file_extras/tools/metadata_tool/media/capybara_cloud_wMetadata.jpeg"
)

agent = Agent(
    prompt_driver=OpenAiChatPromptDriver(model="gpt-4o-mini", api_key=api_key),
    tools=[MetadataTool()],
)

agent.run(
    f'From the metadata for "{TEST_IMAGE}", what value is in the "Keywords" field?'
)
