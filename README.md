# Griptape Open File Tool

A Griptape tool for opening files. 

For example, you can tell an agent to "show you the image at /path/to/image" and it will display it using your default image viewer.

```python
import os

from dotenv import load_dotenv

from griptape.file.tools.open_file_tool import OpenFileTool
from griptape.structures import Agent

load_dotenv()

# Get the path of the image which is in the media directory.
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
images_dir = os.path.join(parent_dir, "media")

agent = Agent(tools=[OpenFileTool()])

agent.run(f"Show me the image at {images_dir}/capybara_cloud.jpeg")

```

This will output:

```bash
[11/22/24 06:11:47] INFO     ToolkitTask 35d860a6f0ac45289bed46822bd1bd2f
                             Input: Show me the image at
                             c:\Users\jason\Documents\GitHub\griptape-extensions\griptape-media-viewer-tool\examples\media/capybara_cloud.jp
                             eg
[11/22/24 06:11:49] INFO     Subtask c4224dddb05e400a88b50d71e165ac8d
                             Actions: [
                               {
                                 "tag": "call_1one03sQjzA0o8rIVNj6RaL6",
                                 "name": "MediaViewerTool",
                                 "path": "show_file",
                                 "input": {
                                   "values": {
                                     "file_path":
                             "c:\\Users\\jason\\Documents\\GitHub\\griptape-extensions\\griptape-media-viewer-tool\\examples\\media/capybara
                             _cloud.jpeg"
                                   }
                                 }
                               }
                             ]
                    INFO     Subtask c4224dddb05e400a88b50d71e165ac8d
                             Response: File displayed:
                             c:\Users\jason\Documents\GitHub\griptape-extensions\griptape-media-viewer-tool\examples\media/capybara_cloud.jp
                             eg
[11/22/24 06:11:51] INFO     ToolkitTask 35d860a6f0ac45289bed46822bd1bd2f
                             Output: The image at the specified path has been displayed.
```

![Capybara Cloud](example_image.png)


## Installing

The easiest way to include this extension into an existing project is to install directly from the repository, like so:

```bash
poetry add git+https://github.com/shhlife/griptape-open-file-tool.git
```

or you can install it with pip:

```bash
pip install git+https://github.com/shhlife/griptape-open-file-tool.git
```

Then to use it, simply import it into your python project, instantiate it, and give it to an `Agent`, or use a `ToolTask`, or `ToolkitTask`:


```python
from griptape.file.tools.open_file_tool import OpenFileTool
from griptape.structures import Agent

agent = Agent(tools=[OpenFileTool()])
```
