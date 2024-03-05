# pip命令

[包管理地址](https://pypi.org/) <https://pypi.org/>

- pip config -v list // 查看pip配置文件
- pip install --upgrade pip // 自我更新

- pip install SomePackage // 安装最新版本
- pip install SomePackage==1.0.4 // 安装指定版本
- pip install 'SomePackage>=1.0.4' // 安装最小版本

- pip install -r requirements.txt // 从文件进行安装，类似 package.json 文件
- pip search SomePackage // 查询包信息
- pip uninstall SomePackage // 卸载包

- pip install --index-url https://pypi.org/project/langchain/ langchain // 指定源
- pip install -r requirements.txt --proxy 127.0.0.1:7890 // 通过本地代理解决

## 常用包

- [Python标准库](https://docs.python.org/3/library/index.html)<https://docs.python.org/3/library/index.html>

- [pytorch](https://pytorch.org/get-started/locally/)

torch包需要指定特定的平台和CUDA版本才能安装，选择操作系统，平台，pip，conda等选项，然后生成相应的安装命令

pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117