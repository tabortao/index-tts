from modelscope import snapshot_download
# 下载1.5版本模型
snapshot_download('IndexTeam/IndexTTS-1.5', local_dir='checkpoints/IndexTTS-1.5')
# 下载1.0版本模型
# snapshot_download('IndexTeam/Index-TTS', local_dir='checkpoints')
