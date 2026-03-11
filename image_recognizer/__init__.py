"""
Image Recognizer - 基于 Qwen VL 的图片识别工具
"""

__version__ = "1.0.0"
__author__ = "Xie Lingxiao"

from .recognizer import recognize_image, RecognizerClient

__all__ = ["recognize_image", "RecognizerClient", "__version__"]
