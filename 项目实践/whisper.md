# whisper

pip install -r requirements.txt

git clone https://huggingface.co/spaces/aadnk/whisper-webui

git clone https://github.com/Mumujianguang/whisper-demo-for-web.git

简单使用，模型和音频都放在 `whisper\whisper` 目录下，和 `__main__.py` 文件同一级

```py
import whisper

modal = whisper.load_model('medium.pt')

result = modal.transcribe('') 

print(result["text"])
```