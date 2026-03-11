# 🖼️ Image Recognizer - Image Recognition Tool

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Qwen VL](https://img.shields.io/badge/Qwen-VL--Plus-purple.svg)](https://dashscope.aliyun.com/)

**Powerful image recognition tool based on the Qwen VL multimodal AI model**

🇨🇳 [中文](README_zh.md)

## ✨ Features

- 🖼️ **Image Content Recognition** - Identify objects, scenes, people, etc.
- 📝 **OCR Text Extraction** - Extract all text from images (multilingual support)
- 📊 **Chart Analysis** - Analyze stock K-line charts, fund trend charts, and data charts
- 📄 **Document Recognition** - Identify structured information such as screenshots, documents, and tables
- 🌍 **Multilingual Support** - Chinese, English, and other languages

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com//image-recognizer.git
cd image-recognizer

# Install dependencies
pip install -r requirements.txt

# Or install via pip (after release)
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
python scripts/recognize.py image.jpg --prompt "Please describe the content of this image in detail"
```

### Python API

```python
from image_recognizer import recognize_image

result = recognize_image(
    image_path="image.jpg",
    task="general",
    prompt="Please describe this image"
)

print(result['result'])
```

## 📋 Task Types

| Task | Description | Examples |
|------|-------------|----------|
| `general` | General image recognition | Objects, scenes, people |
| `ocr` | Text extraction | Documents, screenshots |
| `chart` | Chart analysis | Stock K-line charts, data charts |
| `fund` | Fund screenshot analysis | Fund details, performance trends |

## ⚙️ Configuration

### API Key Setup

This tool uses the Qwen VL API and requires:

1. Obtain an API key from [Alibaba Cloud DashScope](https://dashscope.aliyun.com/)
2. Set the environment variable:
   ```bash
   export QWEN_API_KEY="sk-xxx"
   ```
   
   Or configure it in `~/.openclaw/openclaw.json`

### Model Selection

Default model: `qwen-vl-plus`

Supported models:
- `qwen-vl-plus` - Balanced performance
- `qwen-vl-max` - Higher accuracy (slower)

## 📚 Usage Examples

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

# Run a single test
python -m unittest tests/test_recognizer.py
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- [Qwen VL](https://github.com/QwenLM/Qwen-VL) - Multimodal AI model
- [OpenClaw](https://github.com/openclaw/openclaw) - AI agent framework

## 📬 Contact

- **Author**: yunxiao11xie
- **Email**: [lingxiao.xie@qq.com]

---

<div align="center">

**If you find this project useful, please give it a ⭐️ Star!**

</div>
