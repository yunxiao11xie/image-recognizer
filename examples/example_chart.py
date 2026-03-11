"""
示例 2: 图表分析
"""

from image_recognizer import recognize_image

# 图表分析
result = recognize_image(
    image_path="stock_chart.png",
    task="chart",
    prompt="请分析这张 K 线图的趋势、支撑位、阻力位、成交量变化等"
)

if result['status'] == 'success':
    print("✅ 图表分析完成！")
    print(f"📊 分析结果:\n{result['result']}")
else:
    print(f"❌ 分析失败：{result['message']}")
