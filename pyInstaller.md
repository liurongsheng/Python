# pyInstaller

PyInstaller 是一个用于将 Python 脚本打包成可执行文件的工具，它可以将 Python 程序打包成独立的可执行文件，而不需要安装 Python 解释器

## 安装

`pip install pyinstaller`

## 使用

### 命令行中运行

`pyinstaller yourscript.py`

在当前目录中生成一个 dist 目录，其中包含打包后的可执行文件

### 参数

-w：生成一个不显示命令行窗口的 Windows 可执行文件
--onefile：生成单个可执行文件
-i：指定程序图标
--hidden-import：指定要导入但没有被检测到的模块
--additional-hooks-dir：指定一个目录，用于放置额外的钩子脚本
--exclude-module：排除指定的模块