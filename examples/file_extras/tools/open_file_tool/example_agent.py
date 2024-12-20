from dotenv import load_dotenv

from griptape.file_extras.tools.open_file_tool import OpenFileTool
from griptape.file_extras.utils.env_utils import get_env_var
from griptape.structures import Agent
from griptape.drivers import OpenAiChatPromptDriver

load_dotenv()

api_key = get_env_var("OPENAI_API_KEY")

TEST_IMAGE = "examples/file_extras/tools/open_file_tool/media/capybara_cloud.jpeg"

agent = Agent(
    prompt_driver=OpenAiChatPromptDriver(model="gpt-4o-mini", api_key=api_key),
    tools=[OpenFileTool()],
)

agent.run(f"Can you show me the image at {TEST_IMAGE}?")
