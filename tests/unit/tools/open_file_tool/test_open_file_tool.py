import os

from griptape.artifacts import TextArtifact
from griptape.file_extras.tools.open_file_tool import OpenFileTool


class TestOpenFileTool:
    def test_open_file_tool(self):
        filename = "capybara_cloud.jpeg"
        script_dir = os.path.dirname(os.path.abspath(__file__))
        images_dir = os.path.join(script_dir, "media")

        tool = OpenFileTool()
        value = os.path.join(images_dir, filename)
        params = {"values": {"file_path": value}}
        result = tool.open_file(params)

        assert isinstance(result, TextArtifact), "File displayed: {value}"
