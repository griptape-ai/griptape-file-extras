import os

from griptape.artifacts import TextArtifact
from griptape.file_extras.tools.metadata_tool import MetadataTool


class TestMetadataTool:
    def test_metadata_tool(self):
        filename = "capybara_cloud_wMetadata.jpeg"
        script_dir = os.path.dirname(os.path.abspath(__file__))
        images_dir = os.path.join(script_dir, "media")

        tool = MetadataTool()
        value = os.path.join(images_dir, filename)
        params = {"values": {"image_path": value}}
        result = tool.read_metadata(params)

        assert isinstance(result, TextArtifact), "File displayed: {value}"
