"""
图片识别器测试模块
"""

import unittest
import os
from image_recognizer import recognize_image

class TestRecognizer(unittest.TestCase):
    
    def test_file_exists(self):
        """测试示例文件是否存在"""
        # 这里应该放真实的测试图片路径
        # 暂时只测试函数是否可调用
        self.assertTrue(callable(recognize_image))
    
    def test_invalid_image_path(self):
        """测试无效图片路径"""
        result = recognize_image("/nonexistent/path/image.jpg")
        self.assertEqual(result['status'], 'error')
    
    # TODO: 添加更多测试用例
    # def test_ocr_task(self):
    #     result = recognize_image("tests/images/sample_text.jpg", task="ocr")
    #     self.assertEqual(result['status'], 'success')
    #     self.assertIn('result', result)

if __name__ == '__main__':
    unittest.main()
