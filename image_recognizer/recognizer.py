#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
图片识别脚本 - 使用 Qwen VL 多模态模型
支持本地图片文件和图片 URL 识别
"""

import sys
import os
import json
import base64
import argparse
import requests
from pathlib import Path

# 默认配置
DEFAULT_MODEL = "doubao-1-5-vision-pro-32k-250115"
CONFIG_PATH = os.path.expanduser("~/.openclaw/openclaw.json")

def get_baidu_access_token(api_key):
    """获取百度 access token"""
    try:
        # 百度 API key 格式：bce-v3/ALTAK-xxx/xxx
        response = requests.post(
            "https://qianfan.baidubce.com/v2/auth/oauth/token",
            headers={"Content-Type": "application/json"},
            json={"grant_type": "client_credentials", "client_id": api_key},
            timeout=30
        )
        if response.status_code == 200:
            return response.json().get("access_token")
        return None
    except:
        return None

def get_api_key():
    """从配置文件或环境变量获取 API key"""
    # 1. 优先使用环境变量
    api_key = os.environ.get("QWEN_API_KEY")
    if api_key:
        return api_key
    
    # 2. 从 OpenClaw 配置文件读取
    try:
        with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
            config = json.load(f)
            api_key = config.get('models', {}).get('providers', {}).get('qwen', {}).get('apiKey')
            if api_key:
                return api_key
    except Exception as e:
        print(f"⚠️ 读取配置文件失败：{e}", file=sys.stderr)
    
    # 3. 尝试其他可能的配置位置（优先 doubao，因为 qwen 欠费）
    for provider in ['doubao', 'qwencode', 'baidu']:
        try:
            with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
                config = json.load(f)
                api_key = config.get('models', {}).get('providers', {}).get(provider, {}).get('apiKey')
                if api_key:
                    return api_key
        except:
            continue
    
    return None

def encode_image(image_path):
    """将图片编码为 base64"""
    with open(image_path, 'rb') as f:
        image_data = base64.b64encode(f.read()).decode('utf-8')
    return image_data

def recognize_image(image_path, prompt=None, task="general", api_key=None):
    """
    识别图片内容
    
    Args:
        image_path: 本地图片路径
        prompt: 自定义提示词
        task: 任务类型 (general, ocr, chart)
        api_key: Qwen API key
    
    Returns:
        dict: 识别结果
    """
    # 获取 API key
    if not api_key:
        api_key = get_api_key()
    
    if not api_key:
        return {
            "status": "error",
            "message": "未找到 API key，请设置 QWEN_API_KEY 环境变量或配置 ~/.openclaw/openclaw.json"
        }
    
    # 检查图片文件
    if not os.path.exists(image_path):
        return {
            "status": "error",
            "message": f"图片文件不存在：{image_path}"
        }
    
    # 根据任务类型设置默认提示词
    if not prompt:
        prompts = {
            "general": "请详细描述这张图片的内容，包括所有可见的文字、物体、场景等信息。",
            "ocr": "请提取这张图片中的所有文字内容，保持原文的格式和顺序，不要遗漏任何文字。",
            "chart": "请分析这张图表的内容，包括图表类型、数据趋势、关键数据点等。如果是股票或基金走势图，请分析其走势和关键指标。",
            "fund": "请识别这张基金截图的所有信息，包括基金名称、代码、净值、涨跌幅、持仓、业绩走势等详细信息。"
        }
        prompt = prompts.get(task, prompts["general"])
    
    # 编码图片
    try:
        image_data = encode_image(image_path)
    except Exception as e:
        return {
            "status": "error",
            "message": f"读取图片失败：{e}"
        }
    
    # 调用 Qwen API（阿里通义千问）
    # 注意：需要账户有余额
    url = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "qwen-vl-max",  # 使用 qwen-vl-max 代替 qwen3.5-plus（视觉专用）
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{image_data}"}
                    },
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ],
        "stream": False
    }
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=120)
        response.raise_for_status()
        result = response.json()
        
        # 解析结果
        if 'choices' in result and len(result['choices']) > 0:
            content = result['choices'][0]['message']['content']
            usage = result.get('usage', {})
            
            return {
                "status": "success",
                "image": image_path,
                "task": task,
                "prompt": prompt,
                "result": content,
                "tokens_used": usage.get('total_tokens', 0),
                "model": DEFAULT_MODEL
            }
        else:
            return {
                "status": "error",
                "message": f"API 返回格式异常：{result}"
            }
    
    except requests.exceptions.Timeout:
        return {
            "status": "error",
            "message": "API 请求超时，请重试"
        }
    except requests.exceptions.RequestException as e:
        return {
            "status": "error",
            "message": f"API 请求失败：{e}"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"识别失败：{e}"
        }

def main():
    parser = argparse.ArgumentParser(
        description="图片识别工具 - 使用 Qwen VL 多模态模型",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python3 recognize.py image.jpg                      # 通用识别
  python3 recognize.py image.jpg --task ocr           # OCR 文字提取
  python3 recognize.py chart.png --task chart         # 图表分析
  python3 recognize.py fund.jpg --prompt "自定义提示词"  # 自定义提示
        """
    )
    
    parser.add_argument("image", help="本地图片文件路径")
    parser.add_argument("--task", "-t", choices=["general", "ocr", "chart", "fund"], 
                       default="general", help="任务类型（默认：general）")
    parser.add_argument("--prompt", "-p", help="自定义提示词（可选）")
    parser.add_argument("--json", "-j", action="store_true", help="以 JSON 格式输出结果")
    parser.add_argument("--output", "-o", help="输出文件路径（可选）")
    
    args = parser.parse_args()
    
    # 执行识别
    result = recognize_image(args.image, args.prompt, args.task)
    
    # 输出结果
    if args.json:
        output = json.dumps(result, ensure_ascii=False, indent=2)
    else:
        if result['status'] == 'success':
            output = f"""
✅ 识别成功

📁 图片：{result['image']}
🎯 任务：{result['task']}
🤖 模型：{result['model']}
📊 Token 使用：{result['tokens_used']}

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
