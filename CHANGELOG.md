# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!-- ## [Unreleased]

### Added 
### Changed 
### Deprecated 
### Removed 
### Fixed 
### Security   -->

## [0.3.00] - 2025-04-01
### Added 
- [CHANGELOG.md](CHANGELOG.md)
- Added note in metadata_tool [README.md](docs/file_extras/tools/metadata_tool/README.md) about requiring [exiftool](https://exiftool.org/).

### Changed
- Updated to `Griptape Framework 1.1.0`
- Updated metadata tool to use `os.path.abspath` for filepath
- Updated metadata tool to check for `ExifTool`