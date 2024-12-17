from dotenv import load_dotenv

from griptape.file_extras.tools.open_file_tool import OpenFileTool
from griptape.structures import Agent


load_dotenv()

TEST_IMAGE = "examples/file_extras/tools/open_file_tool/media/capybara_cloud.jpeg"

agent = Agent(tools=[OpenFileTool()])
agent.run(f"Can you show me the image at {TEST_IMAGE}?")
