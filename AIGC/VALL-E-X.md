# VALL-E-X

[说明](https://github.com/Plachtaa/VALL-E-X/blob/master/README-ZH.md)

[模型](https://huggingface.co/Plachta/VALL-E-X/resolve/main/vallex-checkpoint.pt)

安装需求

```
git clone https://github.com/Plachtaa/VALL-E-X.git
cd VALL-E-X
pip install -r requirements.txt
```

第一次运行程序时，会自动下载相应的模型。如果下载失败并报错，请按照以下步骤手动下载模型。

（请注意目录和文件夹的大小写）

1.检查安装目录下是否存在checkpoints文件夹，如果没有，在安装目录下手动创建checkpoints文件夹（./checkpoints/）。

2.检查checkpoints文件夹中是否有vallex-checkpoint.pt文件。如果没有，请从这里 手动下载vallex-checkpoint.pt文件并放到checkpoints文件夹里。

3.检查安装目录下是否存在whisper文件夹，如果没有，在安装目录下手动创建whisper文件夹（./whisper/）。

4.检查whisper文件夹中是否有medium.pt文件。如果没有，请从这里 手动下载medium.pt文件并放到whisper文件夹里。

配置要求

```
VALL-E X 可以在CPU或GPU上运行 (pytorch 2.0+, CUDA 11.7 ~ CUDA 12.0).

若使用GPU运行，你需要至少6GB的显存。
```

## 基本使用

```py
from utils.generation import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio

# download and load all models
preload_models()

# generate audio from text
text_prompt = """
Hello, my name is Nose. And uh, and I like hamburger. Hahaha... But I also have other interests such as playing tactic toast.
"""
audio_array = generate_audio(text_prompt)

# save audio to disk
write_wav("vallex_generation.wav", SAMPLE_RATE, audio_array)

# play text in notebook
Audio(audio_array, rate=SAMPLE_RATE)
```

## 启用用户界面

`python -X utf8 launch-ui.py`

