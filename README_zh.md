# 🖼️ Image Recognizer - 图片识别工具

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Qwen VL](https://img.shields.io/badge/Qwen-VL--Plus-purple.svg)](https://dashscope.aliyun.com/)

**基于 Qwen VL 多模态 AI 模型的强大图片识别工具**

🇺🇸 [English Documentation](README.md)

## ✨ 功能特性

- 🖼️ **图片内容识别** - 识别物体、场景、人物等
- 📝 **OCR 文字提取** - 提取图片中的所有文字（支持多语言）
- 📊 **图表分析** - 分析股票 K 线图、基金走势图、数据图表
- 📄 **文档识别** - 识别截图、文档、表格等结构化信息
- 🌍 **多语言支持** - 中文、英文等多种语言

## 🚀 快速开始

### 安装

```bash
# 克隆仓库
git clone https://github.com/YOUR_USERNAME/image-recognizer.git
cd image-recognizer

# 安装依赖
pip install -r requirements.txt

# 或通过 pip 安装（发布后）
pip install image-recognizer
```

### 基础用法

```bash
# 通用识别
python scripts/recognize.py image.jpg

# OCR 文字提取
python scripts/recognize.py document.png --task ocr

# 图表分析
python scripts/recognize.py kline_chart.png --task chart

# 自定义提示词
python scripts/recognize.py image.jpg --prompt "请详细描述这张图片的内容"
```

### Python API

```python
from image_recognizer import recognize_image

result = recognize_image(
    image_path="image.jpg",
    task="general",
    prompt="请描述这张图片"
)

print(result['result'])
```

## 📋 任务类型

| 任务 | 说明 | 示例 |
|------|------|------|
| `general` | 通用图片识别 | 物体、场景、人物 |
| `ocr` | 文字提取 | 文档、截图 |
| `chart` | 图表分析 | 股票 K 线图、数据图 |
| `fund` | 基金截图分析 | 基金详情、业绩走势 |

## ⚙️ 配置

### API Key 设置

本工具使用 Qwen VL API，需要：

1. 从 [阿里云百炼](https://dashscope.aliyun.com/) 获取 API key
2. 设置环境变量：
   ```bash
   export QWEN_API_KEY="sk-xxx"
   ```
   
   或在 `~/.openclaw/openclaw.json` 中配置

### 模型选择

默认模型：`qwen-vl-plus`

支持的模型：
- `qwen-vl-plus` - 性能均衡
- `qwen-vl-max` - 更高精度（较慢）

## 📚 使用示例

### 示例 1：OCR 文字提取

```bash
python scripts/recognize.py receipt.jpg --task ocr --json
```

### 示例 2：基金图表分析

```bash
python scripts/recognize.py fund_screenshot.jpg --task fund
```

### 示例 3：批量处理

```bash
for img in images/*.jpg; do
    python scripts/recognize.py "$img" --output "results/$(basename $img).txt"
done
```

## 🧪 测试

```bash
# 运行测试
pytest tests/

# 运行单个测试
python -m unittest tests/test_recognizer.py
```

## 📖 文档

- [API 文档](docs/API.md)
- [使用指南](docs/USAGE.md)
- [常见问题](docs/FAQ.md)

## 🤝 贡献

欢迎贡献！请：

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 提交 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 🙏 致谢

- [Qwen VL](https://github.com/QwenLM/Qwen-VL) - 多模态 AI 模型
- [OpenClaw](https://github.com/openclaw/openclaw) - AI 代理框架

## 📬 联系方式

- **作者**: 谢凌霄
- **邮箱**: [your-email@example.com]
- **GitHub**: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)

## 🗺️ 开发计划

- [ ] 支持更多图片格式（WEBP、GIF）
- [ ] 批量处理模式
- [ ] 图形界面（GUI）
- [ ] 本地模型支持（Ollama 集成）
- [ ] 多模型对比
- [ ] API 服务器模式

---

<div align="center">

**如果觉得项目有用，请给个 ⭐️ Star！**

</div>
