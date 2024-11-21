import os

from dotenv import load_dotenv

from griptape.file.tools.open_file_tool import OpenFileTool
from griptape.structures import Agent

load_dotenv()

script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
images_dir = os.path.join(parent_dir, "media")

agent = Agent(tools=[OpenFileTool()])

agent.run(f"Show me the image at {images_dir}/capybara_cloud.jpeg")
