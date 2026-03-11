# 🖼️ Image Recognizer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Qwen VL](https://img.shields.io/badge/Qwen-VL--Plus-purple.svg)](https://dashscope.aliyun.com/)

**Powerful image recognition tool powered by Qwen VL multimodal AI model.**

🇨🇳 [中文文档](README_zh.md)

## ✨ Features

- 🖼️ **Image Content Recognition** - Identify objects, scenes, people, etc.
- 📝 **OCR Text Extraction** - Extract all text from images (multi-language support)
- 📊 **Chart Analysis** - Analyze stock charts, fund graphs, data visualizations
- 📄 **Document Recognition** - Recognize screenshots, documents, tables
- 🌍 **Multi-language Support** - Chinese, English, and more

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/image-recognizer.git
cd image-recognizer

# Install dependencies
pip install -r requirements.txt

# Or install via pip (after publishing)
pip install image-recognizer
```

### Basic Usage

```bash
# General recognition
python scripts/recognize.py image.jpg

# OCR text extraction
python scripts/recognize.py document.png --task ocr

# Chart analysis
python scripts/recognize.py kline_chart.png --task chart

# Custom prompt
python scripts/recognize.py image.jpg --prompt "Describe this image in detail"
```

### Python API

```python
from image_recognizer import recognize_image

result = recognize_image(
    image_path="image.jpg",
    task="general",
    prompt="Describe this image"
)

print(result['result'])
```

## 📋 Task Types

| Task | Description | Example |
|------|-------------|---------|
| `general` | General image recognition | Objects, scenes, people |
| `ocr` | Text extraction | Documents, screenshots |
| `chart` | Chart analysis | Stock charts, data graphs |
| `fund` | Fund screenshot analysis | Fund details, performance |

## ⚙️ Configuration

### API Key Setup

This tool uses Qwen VL API. You need to:

1. Get API key from [Alibaba Cloud DashScope](https://dashscope.aliyun.com/)
2. Set environment variable:
   ```bash
   export QWEN_API_KEY="sk-xxx"
   ```
   
   Or configure in `~/.openclaw/openclaw.json`

### Model Selection

Default model: `qwen-vl-plus`

Supported models:
- `qwen-vl-plus` - Balanced performance
- `qwen-vl-max` - Higher accuracy (slower)

## 📚 Examples

### Example 1: OCR Text Extraction

```bash
python scripts/recognize.py receipt.jpg --task ocr --json
```

### Example 2: Fund Chart Analysis

```bash
python scripts/recognize.py fund_screenshot.jpg --task fund
```

### Example 3: Batch Processing

```bash
for img in images/*.jpg; do
    python scripts/recognize.py "$img" --output "results/$(basename $img).txt"
done
```

## 🧪 Testing

```bash
# Run tests
pytest tests/

# Run single test
python -m unittest tests/test_recognizer.py
```

## 📖 Documentation

- [API Documentation](docs/API.md)
- [Usage Guide](docs/USAGE.md)
- [FAQ](docs/FAQ.md)

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Qwen VL](https://github.com/QwenLM/Qwen-VL) - Multimodal AI model
- [OpenClaw](https://github.com/openclaw/openclaw) - AI agent framework

## 📬 Contact

- **Author**: Xie Lingxiao
- **Email**: [your-email@example.com]
- **GitHub**: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)

## 🗺️ Roadmap

- [ ] Support for more image formats (WEBP, GIF)
- [ ] Batch processing mode
- [ ] GUI interface
- [ ] Local model support (Ollama integration)
- [ ] Multi-model comparison
- [ ] API server mode

---

<div align="center">

**If you like this project, please give it a ⭐️ Star!**

</div>
