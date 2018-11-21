# OpenCV 开源计算机视觉库

[项目地址](https://github.com/opencv/opencv) https://github.com/opencv/opencv

[官方文档总地址](https://docs.opencv.org) https://docs.opencv.org 

[3.0-beta 官方文档 ](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html) https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html 

[中文社区](http://www.opencv.org.cn/forum.php?gid=7) http://www.opencv.org.cn/forum.php?gid=7 

https://arxiv.org

## 安装使用
```
pip install numpy Matplotlib
pip install opencv-python
```

## cv2.imread()，cv2.imshow()，cv2.imwrite()

```python
import cv2

img = cv2.imread(r"D:\2.png", 0)
cv2.namedWindow("Image")
cv2.imshow("Image", img)
k = cv2.waitKey (0)
if k == 27: # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite(r"D:\12.jpg",img)
    cv2.destroyAllWindows()
    cv2.destroyAllWindows()
```

cv2.imread() # 读入图像
- cv2.IMREAD_COLOR # 彩色图，默认
- cv2.IMREAD_GRAYSCALE # 以灰度模式读入图像，值为0的时候也就是这个模式
- cv2.IMREAD_UNCHANGED # 读入一幅图像，并且包括图像的alpha 通道

cv2.imshow(参数1, 参数2) # 显示图像
- 参数1 # 窗口的名字
- 参数2 # 图像

cv2.imwrite(r"D:\12.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 85])
- 参数1 保存的路径及文件名
- 参数2 图像矩阵
- 参数3 可选
  对于 jpeg 表示图像的质量为0-100的整数，默认95，cv2.IMWRITE_JPEG_QUALITY 类型为Long，必须转换为int
  对于 png 表示压缩级别为 0-9的整数，默认3，数字越大，压缩级别越高，尺寸越小 
  

cv2.waitKey() 是一个键盘绑定函数，函数等待特定的几毫秒，看是否有键盘输入
特定的几毫秒之内，如果按下任意键，这个函数会返回按键的ASCII 码值，程序将会继续运行
如果没有键盘输入，返回值为-1，如果我们设置这个函数的参数为0，那它将会无限期的等待键盘输入

cv2.destroyAllWindows() 可以轻易删除任何我们建立的窗口
如果你想删除特定的窗口可以使用cv2.destroyWindow()，在括号内输入你想删除的窗口名

指定打开的窗口大小
```
import numpy as np
import cv2

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

## 摄像头捕获视频
```
import numpy as np
import cv2

cap = cv2.VideoCapture(0) # 笔记本内置摄像头为0，选择其他数字为其他摄像头

while(True):
  ret, frame = cap.read() # Capture frame-by-frame
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Our operations on the frame come here
  cv2.imshow('frame',gray) # Display the resulting frame
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release() # When everything done, release the capture
cv2.destroyAllWindows()
```
cap.read() 返回一个布尔值（True/False）。如果帧读取的是正确的，就是True。所以最后你可以通过检查他的返回值来查看视频文件是否已经到了结尾。

有时cap 可能不能成功的初始化摄像头设备。这种情况下上面的代码会报错。你可以使用cap.isOpened()，来检查是否成功初始化了。
如果返回值是True，那就没有问题。否则就要使用函数cap.open()。

你可以使用函数cap.get(propId) 来获得视频的一些参数信息。

这里propId 可以是0 到18 之间的任何整数。
每一个数代表视频的一个属性，见下表其中的一些值可以使用cap.set(propId,value) 来修改，value 就是你想要设置成的新值。

例如，我可以使用cap.get(3) 和cap.get(4) 来查看每一帧的宽和高。
默认情况下得到的值是640X480。但是我可以使用ret=cap.set(3,320)和ret=cap.set(4,240) 来把宽和高改成320X240。

## 保存视频
1. 创建一个VideoWriter 的对象
2. 指定一个输出文件的名字
3. 指定FourCC 编码
4. 指定播放频率和帧的大小
5. isColor 标签，是True，每一帧就是彩色图，否则就是灰度图
```
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# Define the codec and create VideoWriter object

fourcc = cv2.cv.FOURCC(*'DIVX')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while(cap.isOpened()):
  ret, frame = cap.read()

  if ret==True:
    frame = cv2.flip(frame, 0)

    # write the flipped frame
    out.write(frame)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
    else:
      break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
```

## 绘制函数
- cv2.line()
- cv2.circle()
- cv2.rectangle()
- cv2.ellipse()
- cv2.putText()

- img：你想要绘制图形的那幅图像

- color：形状颜色，以RGB 为例，需要传入一个元组，例如：（255,0,0）代表蓝色。对于灰度图只需要传入灰度值

- thickness：线条的粗细，如果给一个闭合图形设置为-1，那么这个图形就会被填充。默认值是1

- linetype：线条的类型，8连接，抗锯齿等。默认情况是 8连接。cv2.LINE_AA为抗锯齿，这样看起来会非常平滑

画线
line(img, pt1, pt2, color, thickness=None, lineType=None, shift=None)


