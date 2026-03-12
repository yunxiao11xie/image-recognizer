"""
Image Recognizer - 基于 Qwen VL 的图片识别工具
"""

__version__ = "1.0.0"
__author__ = "Xie Lingxiao"

# 移除不存在的 RecognizerClient 引用
from .recognizer import recognize_image

# 同步修正导出列表
__all__ = ["recognize_image", "__version__"]
