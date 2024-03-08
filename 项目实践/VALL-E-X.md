# VALL-E-X

[项目地址](https://github.com/Plachtaa/VALL-E-X)

checkpoints 目录下 [vallex-checkpoint.pt]

whisper 目录下 [medium.pt]

## 运行问题

`Please install `ffmpeg` in your system to use non-WAV audio file formats and make sure `ffprobe` is in your PATH`

下载 ffmpeg

路径一：[ffmpeg](https://www.gyan.dev/ffmpeg/builds/) 点击 `release builds` 链接，然后下载 `ffmpeg-release-full.7z` 文件

路径二：[ffmpeg.org](https://ffmpeg.org/download.html)

解压 `D:\Program Files\ffmpeg\bin` 添加到环境 `Path`

## 使用 GPU 加速

查看安装的包

```py
import torch
print(torch.cuda.is_available())
print(torch.__version__)
```

如果是 false 先卸载掉原先的依赖

`pip3 uninstall torch torchvision torchaudio`

`pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121`