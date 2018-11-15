import subprocess

MEDIA_PLAYER = r'C:\ProgramData\PureCodec\PurePlayer.exe'
MEDIA_FILE = r'E:\于文文+-+体面.flac'
CHROME = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
URL = r'www.baidu.com'

def notify():
    subprocess.Popen([MEDIA_PLAYER, MEDIA_FILE])
    subprocess.Popen([CHROME, URL])
    print("打开网页")

if __name__ == '__main__':
    notify()
