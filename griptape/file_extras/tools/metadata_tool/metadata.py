import subprocess
import json


class Metadata:
    """
    Helper class for managing metadata operations using ExifTool.
    """

    def __init__(self, file_path: str):
        self.file = file_path
        self.data = {}
        self.flag = {}
        self.get()

    def get(self):
        """Extract metadata from a file using ExifTool and store it as a dictionary."""
        try:
            result = subprocess.run(
                ["exiftool", "-s", "-G1", "-j", self.file],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )

            if result.returncode == 0:
                self._process_raw_data(result.stdout)
            else:
                print(f"Error reading metadata for {self.file}: {result.stderr}")
                self.data = {}
        except Exception as e:
            print(f"An error occurred: {e}")
            self.data = {}

    def set(self, **kwargs):
        """Writes metadata to a file using ExifTool."""
        updated_data = self._map_keys_to_metadata(kwargs)

        if not updated_data:
            print("No valid metadata changes to commit.")
            return False

        cmd = (
            ["exiftool"]
            + [f"-{self.flag[key]}={value}" for key, value in updated_data.items()]
            + ["-overwrite_original", self.file]
        )
        result = subprocess.run(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        if result.returncode == 0:
            print("Metadata written successfully.")
            self.data.update(updated_data)
            return True

        print(f"Error writing metadata: {result.stderr}")
        return False

    def _process_raw_data(self, raw_data):
        """Parse raw JSON metadata from ExifTool into structured data."""
        raw_metadata = json.loads(raw_data)[0]
        self.data = {}
        self.flag = {}

        for key, value in raw_metadata.items():
            key_parts = key.split(":")
            field = key_parts[-1]
            self.data[field] = value
            self.flag[field] = key

    def _map_keys_to_metadata(self, kwargs):
        """Maps input keys to valid metadata fields, accounting for case insensitivity and partial matches."""
        mapped_data = {}
        lower_existing_keys = {key.lower(): key for key in self.data.keys()}

        for key, value in kwargs.items():
            key_lower = key.lower()

            if key_lower in lower_existing_keys:
                valid_key = lower_existing_keys[key_lower]
                print(f"Matched input key '{key}' to metadata field '{valid_key}'.")
                mapped_data[valid_key] = value
            else:
                print(f"Warning: Input key '{key}' did not match any metadata field.")

        return mapped_data
