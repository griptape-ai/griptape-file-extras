# Open File Tool

A tool for opening files in the user's default application.

For example, ask an agent to open an image from /path/to/image and it will display it.

```python
from dotenv import load_dotenv

from griptape.file_extras.tools.open_file_tool import OpenFileTool
from griptape.structures import Agent

load_dotenv()


agent = Agent(tools=[OpenFileTool()])

agent.run("Can you show me the image at examples/media/capybara_cloud.jpeg?")

```

will output:

```bash
[11/29/24 11:28:42] INFO     ToolkitTask 5833bde42a0d4112bc2dbdd0e92f39fa
                             Input: Can you show me the image at examples/media/capybara_cloud.jpeg?
[11/29/24 11:28:44] INFO     Subtask 061a71eb20454c429425c8a140d422e6
                             Actions: [
                               {
                                 "tag": "call_6DnLmyroY5uS5q1Xij1alNDU",
                                 "name": "OpenFileTool",
                                 "path": "open_file",
                                 "input": {
                                   "values": {
                                     "file_path": "examples/media/capybara_cloud.jpeg"
                                   }
                                 }
                               }
                             ]
                    INFO     Subtask 061a71eb20454c429425c8a140d422e6
                             Response: File displayed: C:\Users\jason\Documents\GitHub\griptape-extensions\griptape-file-extras\examples\media\capybara_cloud.jpeg
[11/29/24 11:28:46] INFO     ToolkitTask 5833bde42a0d4112bc2dbdd0e92f39fa
                             Output: The image at `examples/media/capybara_cloud.jpeg` has been opened for you.
```