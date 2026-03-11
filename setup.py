from setuptools import setup, find_packages

with open("README_zh.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="image-recognizer",
    version="1.0.0",
    author="Xie Lingxiao",
    author_email="your-email@example.com",
    description="Powerful image recognition tool powered by Qwen VL multimodal AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YOUR_USERNAME/image-recognizer",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.28.0",
    ],
    entry_points={
        "console_scripts": [
            "image-recognizer=image_recognizer.cli:main",
        ],
    },
)
