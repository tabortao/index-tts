
import platform
from setuptools import find_packages, setup



setup(
    name="indextts",
    version="0.1.2",
    author="Index SpeechTeam",
    author_email="xuanwu@bilibili.com",
    long_description=open("README.md", encoding="utf8").read(),
    long_description_content_type="text/markdown",
    description="An Industrial-Level Controllable and Efficient Zero-Shot Text-To-Speech System",
    url="https://github.com/index-tts/index-tts",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "torch==2.6.0",
        "torchaudio==2.6.0",
        "transformers==4.48.2",
        "accelerate==1.6.0",
        "tokenizers==0.21.1",
        "einops==0.8.1",
        "matplotlib==3.10.1",
        "omegaconf==2.3.0",
        "sentencepiece==0.2.0",
        "librosa==0.11.0",
        "numpy==2.1.3",
        "WeTextProcessing==1.0.4.1",
    ],
    extras_require={
        "webui": ["gradio"],
    },
    entry_points={
        "console_scripts": [
            "indextts = indextts.cli:main",
        ]
    },
    license="Apache-2.0",
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
