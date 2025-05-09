
尝试使用了别人整合的index-tts项目，感觉蛮适合自己使用需求的，就想着尝试自己修改完善，做一个更适合自己使用的工具。

## TODO
- 测试项目如何调用
- 编制工具，调用项目进行txt生成语音。



## 更新日志
### v0.0.2(20250509)
- 新增：
    - 新增indextts Command Line Tool
- 更新：
    - 更新 torch==2.6.0、 torchvision==0.21.0（之前为指定版本，安装了最新版本torch 2.8.0），于项目有些地方不兼容
    - 更新requirements.txt依赖，使其与目前项目安装一致。
    - 更新setup.py依赖，使其于requirements.txt一致


### v0.0.1(20250508)
- 新增：
    - 使用Micromamba在项目文件夹创建`py312`项目虚拟环境，python版本为3.12.10
    - 下载模型文件到checkpoints文件夹
    - docs文件夹增加`index-tts-Windows安装教程.md`
    - docs文件夹增加`CHANGELOG.md`文件，记录项目版本更新
    - 制作脚本文件“启动.bat”，一键启动webui
- 更新：
    - 安装自己安装过程，修改requirements.txt