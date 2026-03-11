"""
示例 1: OCR 文字提取
"""

from image_recognizer import recognize_image

# OCR 文字提取
result = recognize_image(
    image_path="your_document.jpg",
    task="ocr",
    prompt="请提取这张图片中的所有文字内容，保持原文的格式和顺序"
)

if result['status'] == 'success':
    print("✅ 识别成功！")
    print(f"📝 文字内容:\n{result['result']}")
    print(f"📊 Token 使用：{result['tokens_used']}")
else:
    print(f"❌ 识别失败：{result['message']}")
