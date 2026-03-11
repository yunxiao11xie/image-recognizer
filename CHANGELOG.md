# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Support for more image formats (WEBP, GIF)
- Batch processing mode
- GUI interface
- Local model support (Ollama integration)
- Multi-model comparison
- API server mode

## [1.0.0] - 2026-03-11

### Added
- Initial release of Image Recognizer
- Support for Qwen VL multimodal AI model
- Four task types:
  - General image recognition
  - OCR text extraction (multi-language)
  - Chart analysis (stock, fund, data visualization)
  - Fund screenshot analysis
- Command-line interface (CLI)
- Python API for programmatic use
- Configuration via environment variables or config file
- Comprehensive documentation (Chinese and English)
- Example scripts for common use cases
- Unit tests framework
- MIT License

### Technical Details
- Built with Python 3.8+
- Uses Qwen VL API (Alibaba Cloud DashScope)
- Supports custom prompts for flexible recognition
- JSON output format for easy integration
- Token usage tracking

### Known Issues
- Requires API key from Alibaba Cloud DashScope
- Image size limit depends on API quota
- Network connection required for cloud API

---

## Version History

| Version | Release Date | Key Features |
|---------|-------------|--------------|
| 1.0.0 | 2026-03-11 | Initial release |

---

## Migration Guide

### From v1.0.0 to Future Versions

(To be added in future releases)

---

## Breaking Changes

(To be added if applicable)

---

## Contributors

- **Xie Lingxiao** - Initial work

(To be updated as contributors join)

---

For more information, visit: https://github.com/YOUR_USERNAME/image-recognizer
