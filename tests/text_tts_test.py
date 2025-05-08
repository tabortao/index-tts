import sys
sys.path.append("..") # 添加项目根目录到搜索路径
from indextts.infer import IndexTTS

if __name__ == "__main__":
    prompt_wav="prompts/Lei.mp3"
    tts = IndexTTS(cfg_path="checkpoints/config.yaml", model_dir="checkpoints", is_fp16=True, use_cuda_kernel=False)
    # 单音频推理测试
    tts.infer(audio_prompt=prompt_wav, text=text, output_path=f"outputs/{text[:20]}.wav", verbose=True)
    text='大家好，我现在正在bilibili 体验 ai 科技，说实话，来之前我绝对想不到！AI技术已经发展到这样匪夷所思的地步了！'

    # 并行推理测试
    text="亲爱的伙伴们，大家好！每一次的努力都是为了更好的未来，要善于从失败中汲取经验，让我们一起勇敢前行,迈向更加美好的明天！"
    tts.infer_fast(audio_prompt=prompt_wav, text=text, output_path=f"outputs/{text[:20]}.wav", verbose=True)

    # 长文本推理测试
    text = """《盗梦空间》是由美国华纳兄弟影片公司出品的电影，由克里斯托弗·诺兰执导并编剧，
莱昂纳多·迪卡普里奥、玛丽昂·歌迪亚、约瑟夫·高登-莱维特、艾利奥特·佩吉、汤姆·哈迪等联袂主演，
2010年7月16日在美国上映，2010年9月1日在中国内地上映，2020年8月28日在中国内地重映。
影片剧情游走于梦境与现实之间，被定义为“发生在意识结构内的当代动作科幻片”，
讲述了由莱昂纳多·迪卡普里奥扮演的造梦师，带领特工团队进入他人梦境，从他人的潜意识中盗取机密，并重塑他人梦境的故事。
""".replace("\n", "")
    tts.infer_fast(audio_prompt=prompt_wav, text=text, output_path=f"outputs/{text[:20]}.wav", verbose=True)
