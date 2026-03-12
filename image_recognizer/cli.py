#!/usr/bin/env python3
"""
命令行入口模块 - 图片识别工具
基于 Qwen VL 多模态模型，支持本地图片的通用描述、OCR、图表分析、基金信息识别
"""

import sys
import json
import argparse
from typing import Optional, Dict

# 导入核心识别函数（处理导入异常）
try:
    from .recognizer import recognize_image
except ImportError:
    # 兼容直接运行 cli.py 的场景
    from recognizer import recognize_image


def parse_cli_args() -> argparse.Namespace:
    """解析命令行参数"""
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
    parser.add_argument(
        "--task", "-t",
        choices=["general", "ocr", "chart", "fund"],
        default="general",
        help="任务类型（默认：general）"
    )
    parser.add_argument("--prompt", "-p", help="自定义提示词（可选）")
    parser.add_argument("--json", "-j", action="store_true", help="以 JSON 格式输出结果")
    parser.add_argument("--output", "-o", help="输出文件路径（可选）")
    parser.add_argument("--version", "-v", action="version", version="image-recognizer 1.0.0")

    return parser.parse_args()


def format_output(result: Dict[str, str], use_json: bool = False) -> str:
    """格式化输出结果"""
    if use_json:
        return json.dumps(result, ensure_ascii=False, indent=2)
    
    if result["status"] == "success":
        return f"""
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
        return f"❌ 识别失败：{result['message']}"


def save_output(content: str, output_path: str) -> Optional[str]:
    """保存输出内容到文件"""
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
        return output_path
    except Exception as e:
        return f"保存文件失败：{str(e)}"


def main() -> None:
    """CLI 主函数"""
    # 解析参数
    args = parse_cli_args()
    
    # 执行图片识别
    result = recognize_image(
        image_path=args.image,
        prompt=args.prompt,
        task=args.task
    )
    
    # 格式化输出
    output_content = format_output(result, use_json=args.json)
    
    # 输出/保存结果
    if args.output:
        save_result = save_output(output_content, args.output)
        if save_result.startswith("保存文件失败"):
            print(f"❌ {save_result}", file=sys.stderr)
            sys.exit(1)
        print(f"✅ 结果已保存到：{args.output}")
    else:
        print(output_content)
    
    # 返回状态码
    sys.exit(0 if result["status"] == "success" else 1)


if __name__ == "__main__":
   main()
    
    main()
