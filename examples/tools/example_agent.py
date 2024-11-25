from dotenv import load_dotenv

from griptape.file.tools.open_file_tool import OpenFileTool
from griptape.structures import Agent

load_dotenv()


agent = Agent(tools=[OpenFileTool()])

agent.run("Can you show me the image at examples/media/capybara_cloud.jpeg?")
