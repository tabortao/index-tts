# index-tts Windows安装教程

index-tts 是一个主要用于本地推理和部署的文本转语音（TTS）项目，尤其以其快速、低资源占用以及声音质量优异著称。它能够将文本信息转换为自然、流畅的语音，同时支持各种自定义设置以满足用户的个性化需求。

如需要一键安装包，可以Issues留言获取。

## 安装依赖

**Micromamba**是[Mamba](https://mamba.readthedocs.io/en/latest/) 项目的一部分，它是Conda包管理器的一个轻量级、高效且快速的替代品。相比于传统的Conda，Micromamba提供了更小的安装体积和更快的性能，特别适合需要快速创建和管理虚拟环境的场景。

```bash
# Powershell安装micromamba
Invoke-Expression ((Invoke-WebRequest -Uri https://micro.mamba.pm/install.ps1 -UseBasicParsing).Content)
# 软件会被安装到如下目录
# 推荐修改，安装时候，可以自定义环境目录，如F:\Development\Python\micromamba
# C:\Users\username\micromamba\condabin
# C:\Users\username\AppData\Local\micromamba

# 下载代码
git clone https://github.com/index-tts/index-tts.git
cd index-tts

# 创建虚拟环境

# 如果想给别人使用，推荐指定虚拟环境路径到项目文件夹，注意修改为自己的项目路径
micromamba create -p F:\Code\TTS\index-tts\py312 python=3.12
# micromamba create -n py312 python=3.12 -y
# 激活指定路径的虚拟环境
micromamba activate F:\Code\TTS\index-tts\py312
# micromamba activate py312

# 安装依赖，使用阿里云镜像
# 先注释掉requirements.txt里面的# WeTextProcessing、# wetext
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com

# 安装pynini
micromamba install -c conda-forge pynini==2.1.6
pip install WeTextProcessing --no-deps --index-url https://pypi.tuna.tsinghua.edu.cn/simple

# 安装PyTorch，需指定torch版本，减少兼容性错误
pip3 install torch==2.6.0 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126

# 提示可能缺少模块importlib_resources的话
pip install importlib_resources==6.5.2 --index-url https://pypi.tuna.tsinghua.edu.cn/simple

# micromamba导出项目依赖文件
micromamba list -p F:\Code\TTS\index-tts\py312 --export > requirements2.txt
# 或者conda兼容的导出项目依赖文件
micromamba list -p F:\Code\TTS\index-tts\py312 --export | Select-String -NotMatch '^#' > requirements3.txt

# micromamba恢复环境
micromamba create --name <new_env_name> --file requirements.txt
micromamba create -p F:\Code\TTS\index-tts\py312 --file requirements.txt
```

## 下载模型
### 方式一：Modelscope下载推荐方式
安装Modelscope SDK
```bash
pip install modelscope --index-url https://pypi.tuna.tsinghua.edu.cn/simple
```
在index-tts文件夹新建download_model.py, 粘贴如下内容并运行`python download_model.py`:

```python
from modelscope import snapshot_download
snapshot_download('IndexTeam/IndexTTS-1.5', local_dir='checkpoints/IndexTTS-1.5')
```
使用Modelscope下载
```bash
python download_model.py
```

### 方式二：huggingface-cli下载

```bash
# 1.5版本模型
huggingface-cli download IndexTeam/IndexTTS-1.5 \
  config.yaml bigvgan_discriminator.pth bigvgan_generator.pth bpe.model dvae.pth gpt.pth unigram_12000.vocab \
  --local-dir checkpoints
# 1.0版本模型
huggingface-cli download IndexTeam/Index-TTS \
  bigvgan_discriminator.pth bigvgan_generator.pth bpe.model dvae.pth gpt.pth unigram_12000.vocab \
  --local-dir checkpoints

```

### 方式三：weget下载

```bash
mkdir -p pretrained_models
# 1.5版本模型下载
wget https://huggingface.co/IndexTeam/IndexTTS-1.5/resolve/main/bigvgan_discriminator.pth -P checkpoints
wget https://huggingface.co/IndexTeam/IndexTTS-1.5/resolve/main/bigvgan_generator.pth -P checkpoints
wget https://huggingface.co/IndexTeam/IndexTTS-1.5/resolve/main/bpe.model -P checkpoints
wget https://huggingface.co/IndexTeam/IndexTTS-1.5/resolve/main/dvae.pth -P checkpoints
wget https://huggingface.co/IndexTeam/IndexTTS-1.5/resolve/main/gpt.pth -P checkpoints
wget https://huggingface.co/IndexTeam/IndexTTS-1.5/resolve/main/unigram_12000.vocab -P checkpoints
wget https://huggingface.co/IndexTeam/IndexTTS-1.5/resolve/main/config.yaml -P checkpoints

# 1.0版本模型下载
# Make sure you have git-lfs installed (https://git-lfs.com)
wget https://huggingface.co/IndexTeam/Index-TTS/resolve/main/bigvgan_discriminator.pth -P checkpoints
wget https://huggingface.co/IndexTeam/Index-TTS/resolve/main/bigvgan_generator.pth -P checkpoints
wget https://huggingface.co/IndexTeam/Index-TTS/resolve/main/bpe.model -P checkpoints
wget https://huggingface.co/IndexTeam/Index-TTS/resolve/main/dvae.pth -P checkpoints
wget https://huggingface.co/IndexTeam/Index-TTS/resolve/main/gpt.pth -P checkpoints
wget https://huggingface.co/IndexTeam/Index-TTS/resolve/main/unigram_12000.vocab -P checkpoints


```
### 方式四：下载工具下载

可以使用IDM等下载工具，在hf-mirror网站下载模型，对于大文件效果更好，速度刚刚的。
在hf-mirror下载
- https://hf-mirror.com/IndexTeam/Index-TTS/tree/main
或者魔塔社区下载
- https://modelscope.cn/models/IndexTeam/IndexTTS-1.5

## Command Line Tool
```bash
# Make sure pytorch has been installed before running this command
pip install -e .
indextts "大家好，我是一个超人！" --voice prompts/Lei.mp3 --model_dir checkpoints --config checkpoints/config.yaml --output output.wav

# Use --help to see more options.
indextts --help
```


## Web Demo

```bash

pip install -e ".[webui]"
python webui.py

```
打开你的浏览器，访问 http://127.0.0.1:7860 查看演示。

## 使用技巧

### Pip缓存路径修改
```bash
# 查看现有pip缓存路径
pip cache dir
# 默认路径为下面，占用C盘空间，建议修改
c:\users\lei\appdata\local\pip\cache
# powershell执行下面命令，注意修改缓存路径
# 为当前用户修改pip缓存路径
[System.Environment]::SetEnvironmentVariable("PIP_CACHE_DIR", "D:\Development\Python\cache", [System.EnvironmentVariableTarget]::User)
# 为整个系统级修改缓存路径
[System.Environment]::SetEnvironmentVariable("PIP_CACHE_DIR", "D:\Development\Python\cache", [System.EnvironmentVariableTarget]::Machine)

# 重开一个powershell，执行下面命令，查看设置是否生效
echo $env:PIP_CACHE_DIR
# 下面这个路径的缓存，可以删除了
C:\Users\Lei\AppData\Local\pip\cache
# 注意下面这个路径，全局用户级pip会安装到这里
C:\Users\Lei\AppData\Roaming\Python\Python312
```

## 参考文章
- [Mamba--快速且跨平台的软件包管理器（conda的替代品）](https://mp.weixin.qq.com/s/8GXV_xiW5XVOtFaFqgfWbg)
- [抄了AI语音克隆的家！本地部署、6G显存搞定、一键启动包免费放送、支持win10/win11](https://mp.weixin.qq.com/s/qfm1kYhjQN6RdKB5xedWpA)
- [声音克隆：B站IndexTTS本地安装和运行，Windows+GTX1660S！](https://mp.weixin.qq.com/s/NHAGAk2FjtboaDmjn70b1A)
