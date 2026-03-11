#!/bin/bash

# 🚀 image-recognizer 快速发布脚本
# 使用方法：./publish_to_github.sh YOUR_GITHUB_USERNAME

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 检查参数
if [ -z "$1" ]; then
    echo -e "${RED}❌ 错误：请提供 GitHub 用户名${NC}"
    echo "用法：$0 <YOUR_GITHUB_USERNAME>"
    echo "示例：$0 xielingxiao"
    exit 1
fi

GITHUB_USERNAME=$1
REPO_NAME="image-recognizer"
PROJECT_DIR="/tmp/image-recognizer"

echo -e "${GREEN}🚀 开始发布到 GitHub...${NC}"
echo ""

# 进入项目目录
cd $PROJECT_DIR

# 1. 更新占位符
echo -e "${YELLOW}📝 更新配置文件...${NC}"
sed -i "s/YOUR_USERNAME/$GITHUB_USERNAME/g" README.md
sed -i "s/YOUR_USERNAME/$GITHUB_USERNAME/g" README_zh.md
sed -i "s/YOUR_USERNAME/$GITHUB_USERNAME/g" setup.py
sed -i "s/YOUR_USERNAME/$GITHUB_USERNAME/g" pyproject.toml
echo -e "${GREEN}✅ 配置文件已更新${NC}"
echo ""

# 2. 提交更改
echo -e "${YELLOW}💾 提交配置更新...${NC}"
git add -A
git commit -m "docs: 更新 GitHub 用户名占位符" || echo "没有更改需要提交"
echo -e "${GREEN}✅ 提交完成${NC}"
echo ""

# 3. 添加远程仓库
echo -e "${YELLOW}🔗 添加远程仓库...${NC}"
git remote remove origin 2>/dev/null || true
git remote add origin git@github.com:$GITHUB_USERNAME/$REPO_NAME.git
echo -e "${GREEN}✅ 远程仓库已添加${NC}"
echo ""

# 4. 推送代码
echo -e "${YELLOW}📤 推送到 GitHub...${NC}"
echo "提示：如果是第一次推送，可能需要输入 GitHub 密码或使用 SSH key"
git push -u origin main
echo -e "${GREEN}✅ 推送成功！${NC}"
echo ""

# 5. 显示结果
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}🎉 发布成功！${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo "📦 仓库地址：https://github.com/$GITHUB_USERNAME/$REPO_NAME"
echo ""
echo "📋 下一步操作："
echo "   1. 访问仓库页面"
echo "   2. 添加 Topics 标签"
echo "   3. 创建第一个 Release"
echo "   4. 分享给朋友们！"
echo ""
echo -e "${YELLOW}💡 提示：查看 PUBLISH_CHECKLIST.md 获取完整清单${NC}"
echo ""
