from griptape.file_extras.tools.metadata_tool.metadata import Metadata
from griptape.utils.decorators import activity
from griptape.artifacts import TextArtifact
from griptape.tools import BaseTool
from schema import Literal, Schema


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
    def read_metadata(self, image_path: str) -> TextArtifact:
        """Extract metadata from a file using ExifTool."""
        metadata_obj = Metadata(image_path)
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
    def write_metadata(self, image_path: str, kv_pairs: dict) -> TextArtifact:
        """Writes metadata to a file using ExifTool."""
        metadata_obj = Metadata(image_path)
        metadata_obj.set(**kv_pairs)
        return TextArtifact(metadata_obj.data)
