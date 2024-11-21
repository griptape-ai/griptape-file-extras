from __future__ import annotations

import os
import subprocess
import sys

from attrs import define
from schema import Literal, Schema

from griptape.artifacts import ErrorArtifact, TextArtifact
from griptape.tools import BaseTool
from griptape.utils.decorators import activity


@define
class MediaViewerTool(BaseTool):
    @activity(
        config={
            "description": "Can be used to display an image",
            "schema": Schema(
                {
                    Literal(
                        "file_path",
                        description="Name of the file to show. Example: images/chair.png",
                    ): str,
                }
            ),
        }
    )
    def show_file(self, params: dict) -> TextArtifact | ErrorArtifact:
        # get the file path from the parameters
        file_path = params["values"]["file_path"]
        try:
            if sys.platform.startswith("darwin"):  # macOS
                subprocess.call(("open", file_path))
            elif os.name == "nt":  # Windows
                os.startfile(file_path)
            elif os.name == "posix":  # Linux/Unix
                subprocess.call(("xdg-open", file_path))
            else:
                print("Unsupported OS.")
            return TextArtifact(f"File displayed: {file_path}")
        except Exception as e:
            return TextArtifact(str(e))
