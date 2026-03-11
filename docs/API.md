# API 文档

## 函数参考

### `recognize_image(image_path, prompt=None, task="general", api_key=None)`

识别图片内容

**参数:**
- `image_path` (str): 本地图片文件路径
- `prompt` (str, optional): 自定义提示词
- `task` (str, optional): 任务类型，可选值：
  - `"general"` - 通用识别（默认）
  - `"ocr"` - OCR 文字提取
  - `"chart"` - 图表分析
  - `"fund"` - 基金截图分析
- `api_key` (str, optional): Qwen API key，默认从环境变量或配置文件读取

**返回值:**
```python
{
    "status": "success" | "error",
    "image": str,              # 图片路径
    "task": str,               # 任务类型
    "result": str,             # 识别结果（成功时）
    "message": str,            # 错误信息（失败时）
    "tokens_used": int,        # Token 使用量
    "model": str               # 使用的模型
}
```

**示例:**
```python
from image_recognizer import recognize_image

# 通用识别
result = recognize_image("image.jpg")

# OCR 文字提取
result = recognize_image("document.png", task="ocr")

# 自定义提示词
result = recognize_image("chart.png", prompt="请详细分析这张图表")
```

---

## 类参考

### `RecognizerClient`

识别器客户端类（待实现）

**属性:**
- `api_key`: API key
- `model`: 使用的模型
- `timeout`: 请求超时时间

**方法:**
- `recognize(image_path, task, prompt)`: 识别图片
- `batch_recognize(image_list, task)`: 批量识别
- `set_model(model_name)`: 切换模型

---

## 错误处理

```python
result = recognize_image("image.jpg")

if result['status'] == 'error':
    print(f"识别失败：{result['message']}")
    # 常见错误：
    # - "未找到 API key"
    # - "图片文件不存在"
    # - "API 请求失败"
    # - "API 请求超时"
```

---

## 最佳实践

1. **错误处理**: 始终检查 `result['status']`
2. **Token 监控**: 通过 `result['tokens_used']` 监控 API 使用量
3. **重试机制**: 对于超时错误，可以实现重试逻辑
4. **批量处理**: 多个图片之间添加延时，避免触发速率限制
