import os

from schema import Literal, Schema

from griptape.artifacts import TextArtifact
from griptape.file_extras.tools.metadata_tool.metadata import Metadata
from griptape.tools import BaseTool
from griptape.utils.decorators import activity


class MetadataTool(BaseTool):
    """
    Tool for reading and writing metadata from/to image files using ExifTool.
    """

    @activity(
        config={
            "description": "Reads metadata from an image file using ExifTool.",
            "schema": Schema(
                {
                    Literal(
                        "image_path",
                        "The path and filename of the image to read the metadata from",
                    ): str,
                }
            ),
        }
    )
    def read_metadata(self, params: dict) -> TextArtifact:
        """Extract metadata from a file using ExifTool."""
        # get the file path from the parameters
        image_path = params["values"]["image_path"]
        absolute_path = os.path.abspath(image_path)
        metadata_obj = Metadata(file_path=absolute_path)
        return TextArtifact(metadata_obj.data)

    @activity(
        config={
            "description": "Writes metadata to an image file using ExifTool.",
            "schema": Schema(
                {
                    Literal(
                        "image_path",
                        "The path and filename of the image whose metadata to write to",
                    ): str,
                    Literal(
                        "kv_pairs",
                        "Key-value pairs to overwrite the contents of metadata fields",
                    ): dict,
                }
            ),
        }
    )
    def write_metadata(self, params: dict) -> TextArtifact:
        """Writes metadata to a file using ExifTool."""
        image_path = params["values"]["image_path"]
        absolute_path = os.path.abspath(image_path)
        kv_pairs = params["values"]["kv_pairs"]
        metadata_obj = Metadata(file_path=absolute_path)
        metadata_obj.set(**kv_pairs)
        return TextArtifact(metadata_obj.data)
