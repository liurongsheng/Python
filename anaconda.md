# anaconda 
[清华镜像](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/?C=M&O=D)
安装软件需要把 anaconda 配置到全局环境 path
```
C:\Users\Administrator\Anaconda3
C:\Users\Administrator\Anaconda3\Scripts
C:\Users\Administrator\Anaconda3\Library\bin
C:\Users\Administrator\Anaconda3\Library\usr\bin
C:\Users\Administrator\Anaconda3\Library\mingw-w64\bin
```

## 创建新环境失败
失败原因：长城防火墙限制，需要换源

- 清华源
```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes
```

- 中科大源
```
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/bioconda/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/menpo/
conda config --set show_channel_urls yes
```

配置后查看信息
```
conda info
```
## 包管理命令
```
- 安装
conda install matplotlib

- 卸载
conda remove matplotlib

- 更新
conda update matplotlib

- 查询安装列表
conda list 

- 创建环境 
conda create -n py36 python=3.6

- 删除环境
conda env remove -n py36

- 激活环境 
conda activate py36

- 离开环境
deactivat
```
