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
import requests
from pathlib import Path
from typing import Optional, Dict, Any
from urllib.parse import urlparse

# 默认配置
DEFAULT_MODEL = "qwen-vl-max"  # 统一模型名称（与实际调用一致）
CONFIG_PATH = Path.home() / ".openclaw" / "openclaw.json"
SUPPORTED_IMAGE_FORMATS = (".jpg", ".jpeg", ".png", ".webp", ".bmp", ".gif")


def get_api_key() -> Optional[str]:
    """
    从环境变量/配置文件获取 API Key（优化：仅读取一次配置文件）
    优先级：环境变量 QWEN_API_KEY > 配置文件 qwen > doubao > qwencode > baidu
    """
    # 1. 优先读取环境变量
    api_key = os.environ.get("QWEN_API_KEY")
    if api_key:
        return api_key.strip()

    # 2. 读取配置文件（仅读一次）
    config: Dict[str, Any] = {}
    try:
        if CONFIG_PATH.exists():
            with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
                config = json.load(f)
    except Exception as e:
        print(f"⚠️ 读取配置文件失败：{str(e)}", file=sys.stderr)
        return None

    # 3. 依次检查配置文件中的多个 provider
    for provider in ['qwen', 'doubao', 'qwencode', 'baidu']:
        api_key = config.get('models', {}).get('providers', {}).get(provider, {}).get('apiKey')
        if api_key and api_key.strip():
            return api_key.strip()

    return None


def is_valid_url(url: str) -> bool:
    """判断是否为有效 URL"""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False


def download_image_from_url(url: str) -> Optional[str]:
    """从 URL 下载图片到临时文件"""
    try:
        response = requests.get(url, timeout=30, stream=True)
        response.raise_for_status()
        
        # 创建临时文件（保留后缀）
        from tempfile import NamedTemporaryFile
        suffix = Path(urlparse(url).path).suffix or ".jpg"
        if suffix not in SUPPORTED_IMAGE_FORMATS:
            suffix = ".jpg"
        
        temp_file = NamedTemporaryFile(delete=False, suffix=suffix)
        for chunk in response.iter_content(chunk_size=8192):
            temp_file.write(chunk)
        temp_file.close()
        return temp_file.name
    except Exception as e:
        print(f"⚠️ 下载图片失败：{str(e)}", file=sys.stderr)
        return None


def encode_image(image_path: str) -> Optional[str]:
    """
    将图片编码为 Base64（自动适配图片格式）
    返回：Base64 编码字符串 | None
    """
    try:
        # 获取图片实际格式
        suffix = Path(image_path).suffix.lower()
        mime_type = f"image/{suffix.lstrip('.')}" if suffix in SUPPORTED_IMAGE_FORMATS else "image/jpeg"
        
        with open(image_path, 'rb') as f:
            image_data = base64.b64encode(f.read()).decode('utf-8')
        
        # 返回带 MIME 类型的完整编码（注：实际调用时只需要编码内容，这里拆分更灵活）
        return image_data
    except FileNotFoundError:
        print(f"❌ 图片文件不存在：{image_path}", file=sys.stderr)
        return None
    except PermissionError:
        print(f"❌ 无权限读取图片：{image_path}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"❌ 编码图片失败：{str(e)}", file=sys.stderr)
        return None


def recognize_image(
    image_path: str,
    prompt: Optional[str] = None,
    task: str = "general",
    api_key: Optional[str] = None
) -> Dict[str, Any]:
    """
    识别图片内容（支持本地文件/URL）
    
    Args:
        image_path: 本地图片路径 | 图片 URL
        prompt: 自定义提示词
        task: 任务类型 (general/ocr/chart/fund)
        api_key: Qwen API Key（优先使用传入值，否则自动获取）
    
    Returns:
        dict: 识别结果（status: success/error）
    """
    # 1. 校验 API Key
    if not api_key:
        api_key = get_api_key()
    if not api_key:
        return {
            "status": "error",
            "message": "未找到 API Key，请设置 QWEN_API_KEY 环境变量或配置 ~/.openclaw/openclaw.json"
        }

    # 2. 处理图片（URL → 临时文件 | 本地文件 → 校验）
    local_image_path = image_path
    if is_valid_url(image_path):
        local_image_path = download_image_from_url(image_path)
        if not local_image_path:
            return {
                "status": "error",
                "message": f"无法下载图片 URL：{image_path}"
            }
    else:
        if not Path(local_image_path).exists():
            return {
                "status": "error",
                "message": f"图片文件不存在：{local_image_path}"
            }

    # 3. 设置默认提示词
    if not prompt:
        prompt_map = {
            "general": "请详细描述这张图片的内容，包括所有可见的文字、物体、场景等信息。",
            "ocr": "请提取这张图片中的所有文字内容，保持原文的格式和顺序，不要遗漏任何文字。",
            "chart": "请分析这张图表的内容，包括图表类型、数据趋势、关键数据点等。如果是股票或基金走势图，请分析其走势和关键指标。",
            "fund": "请识别这张基金截图的所有信息，包括基金名称、代码、净值、涨跌幅、持仓、业绩走势等详细信息。"
        }
        prompt = prompt_map.get(task, prompt_map["general"])

    # 4. 编码图片
    image_data = encode_image(local_image_path)
    if not image_data:
        return {
            "status": "error",
            "message": f"编码图片失败：{local_image_path}"
        }

    # 5. 调用 Qwen VL API
    api_url = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # 自动适配图片 MIME 类型
    suffix = Path(local_image_path).suffix.lower().lstrip('.')
    mime_type = f"image/{suffix}" if suffix in SUPPORTED_IMAGE_FORMATS else "image/jpeg"

    request_data = {
        "model": DEFAULT_MODEL,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:{mime_type};base64,{image_data}"}
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
        response = requests.post(api_url, headers=headers, json=request_data, timeout=120)
        response.raise_for_status()  # 抛出 HTTP 错误
        result = response.json()

        # 解析返回结果
        if "choices" in result and len(result["choices"]) > 0:
            content = result["choices"][0]["message"]["content"]
            usage = result.get("usage", {})
            
            # 清理临时文件（URL 下载的图片）
            if local_image_path != image_path and Path(local_image_path).exists():
                os.unlink(local_image_path)

            return {
                "status": "success",
                "image": image_path,
                "task": task,
                "prompt": prompt,
                "result": content,
                "tokens_used": usage.get("total_tokens", 0),
                "model": DEFAULT_MODEL
            }
        else:
            return {
                "status": "error",
                "message": f"API 返回无有效内容：{json.dumps(result, ensure_ascii=False)}"
            }

    except requests.exceptions.Timeout:
        return {"status": "error", "message": "API 请求超时（超过 120 秒），请重试"}
    except requests.exceptions.HTTPError as e:
        return {"status": "error", "message": f"API HTTP 错误：{e.response.status_code} - {e.response.text}"}
    except requests.exceptions.ConnectionError:
        return {"status": "error", "message": "API 连接失败，请检查网络或 API 地址"}
    except Exception as e:
        return {"status": "error", "message": f"识别异常：{str(e)}"}
    finally:
        # 兜底清理临时文件
        if local_image_path != image_path and Path(local_image_path).exists():
            try:
                os.unlink(local_image_path)
            except:
                pass
