# anaconda

安装软件需要把 anaconda 配置到全局环境 path

```config
C:\Users\Administrator\Anaconda3
C:\Users\Administrator\Anaconda3\Scripts
C:\Users\Administrator\Anaconda3\Library\bin
C:\Users\Administrator\Anaconda3\Library\usr\bin
C:\Users\Administrator\Anaconda3\Library\mingw-w64\bin
```

## 创建新环境失败

- 清华源

```shell
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --set show_channel_urls yes
```

- 中科大源

```shell
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/bioconda/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/menpo/
conda config --set show_channel_urls yes
```

## 包管理命令

```shell
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/ // 添加源
conda config –-remove channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/ // 删除源
conda config –remove-key channels // 恢复默认源
```

- conda info // 配置后查看信息
- conda install matplot // 安装
- conda install blendmodes
- conda remove matplotlib // 卸载
- conda update matplotlib // 更新
- conda list // 查询安装列表
- conda create -n py310 python=3.10 // 创建环境
- conda env remove -n py310 // 删除环境

- conda activate py310 // 激活环境
- conda deactivat // 离开环境

## 错误提示

问题1. conda install无法安装安装，提示 `CondaSSLError: OpenSSL appears to be unavailable on this machine. OpenSSL is required to
download and install packages.`

```text
到 `Anaconda3\Library\lib` 目录下复制 `liblibssl-1_1-x64.dll` 和 `libcrypto-1_1-x64.dll` 到 `Anaconda3\DLLs` 然后重启解决
```
## [conda pytorch](https://pytorch.org/)

### Nvidia CUDA 

`conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia`

### CPU only

`conda install pytorch torchvision torchaudio cpuonly -c pytorch`

[示例](https://github.com/pytorch/examples)


