# Griptape File Extras

A Griptape repository for working with files. 

## Current Extras

### Tools

* [Open File Tool](docs/file_extras/tools/open_file_tool/README.md) - Will open any file using the user's default application for that file type.

## Installing

The easiest way to include this extension into an existing project is to install directly from the repository, like so:

```bash
poetry add git+https://github.com/griptape-ai/griptape-file-extras.git
```

or you can install it with pip:

```bash
pip install git+https://github.com/griptape-ai/griptape-file-extras.git
```

Then to use it, simply import it into your python project, instantiate it, and give it to an `Agent`, or use a `ToolTask`, or `ToolkitTask`:


```python
from griptape.file-extras.tools.open_file_tool import OpenFileTool
from griptape.structures import Agent

agent = Agent(tools=[OpenFileTool()])
```
