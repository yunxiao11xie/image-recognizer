#!/usr/bin/env python3
"""
命令行入口模块
"""

import sys
import argparse
from .recognizer import recognize_image

def main():
    parser = argparse.ArgumentParser(
        description="图片识别工具 - 使用 Qwen VL 多模态模型",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  image-recognizer image.jpg                      # 通用识别
  image-recognizer image.jpg --task ocr           # OCR 文字提取
  image-recognizer chart.png --task chart         # 图表分析
  image-recognizer fund.jpg --prompt "自定义提示词"  # 自定义提示
        """
    )
    
    parser.add_argument("image", help="本地图片文件路径")
    parser.add_argument("--task", "-t", choices=["general", "ocr", "chart", "fund"], 
                       default="general", help="任务类型（默认：general）")
    parser.add_argument("--prompt", "-p", help="自定义提示词（可选）")
    parser.add_argument("--json", "-j", action="store_true", help="以 JSON 格式输出结果")
    parser.add_argument("--output", "-o", help="输出文件路径（可选）")
    parser.add_argument("--version", "-v", action="version", version="image-recognizer 1.0.0")
    
    args = parser.parse_args()
    
    # 执行识别
    result = recognize_image(args.image, args.prompt, args.task)
    
    # 输出结果
    if args.json:
        import json
        output = json.dumps(result, ensure_ascii=False, indent=2)
    else:
        if result['status'] == 'success':
            output = f"""
✅ 识别成功

📁 图片：{result['image']}
🎯 任务：{result['task']}
🤖 模型：{result.get('model', 'N/A')}
📊 Token 使用：{result.get('tokens_used', 0)}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📝 识别结果:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{result['result']}
"""
        else:
            output = f"❌ 识别失败：{result['message']}"
    
    # 输出或保存
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"✅ 结果已保存到：{args.output}")
    else:
        print(output)
    
    # 返回状态码
    sys.exit(0 if result['status'] == 'success' else 1)

if __name__ == "__main__":
    main()
