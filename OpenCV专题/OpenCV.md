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
Numpy 是经过优化了的进行快速矩阵运算的软件包。能用矩阵运算就不用循环

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

所有绘制函数的返回值都是 None，所以不能赋值

- cv2.line()
- cv2.circle()
- cv2.rectangle()
- cv2.ellipse()
- cv2.putText()

- img：你想要绘制图形的那幅图像

- color：形状颜色，以RGB 为例，需要传入一个元组，例如：（255,0,0）代表蓝色。对于灰度图只需要传入灰度值

- thickness：线条的粗细，如果给一个闭合图形设置为-1，那么这个图形就会被填充。默认值是1

- linetype：线条的类型，8连接，抗锯齿等。默认情况是 8连接。cv2.LINE_AA为抗锯齿，这样看起来会非常平滑

画线 指定起点和终点
line(img, pt1, pt2, color, thickness=None, lineType=None, shift=None)

画矩形 指定左上角顶点和右下角顶点
rectangle(img, pt1, pt2, color, thickness=None, lineType=None, shift=None)

画圆 指定中心的坐标和半径大小
circle(img, center, radius, color, thickness=None, lineType=None, shift=None)

画椭圆 指定中心点坐标，长轴，短轴，逆时针旋转角度，顺时针起始角度，顺时针结束角度
ellipse(img, center, axes, angle, startAngle, endAngle, color, thickness=None, lineType=None, shift=None)

画多边形 指定每个顶点的坐标，构建一个数组，数据类型为int32
pts=np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts=pts.reshape((-1,1,2)) 

这里reshape 的第一个参数为-1, 表明这一维的长度是根据后面的维度的计算出来的。
如果第三个参数是False，我们得到的多边形是不闭合的（首尾不相连)

```python
import numpy as np
import cv2

img = np.zeros((512,512,3), np.uint8)
cv2.line(img, (0,0), (511,511), (0,0,255), 3)
cv2.rectangle(img, (384,0), (510,128), (0,255,0), 3)
cv2.circle(img, (447,63), 63, (0,0,255), -1)
cv2.ellipse(img, (256,256), (100,50), 0, 0, 180, 255, -1)

cv2.imshow("Image", img)
k = cv2.waitKey (0)
```

## 图像上添加文字
指定 显示文字，显示位置，字体类型，字体大小，一般属性如颜色|粗细|线条类型(linetype=cv2.LINE_AA)

putText(img, text, org, fontFace, fontScale, color, thickness=None, lineType=None, bottomLeftOrigin=None):

```python
import numpy as np
import cv2

img = np.zeros((512,512,3), np.uint8)

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10,300), font, 4, (255,255,255), 2)

cv2.imshow("Image", img)
k = cv2.waitKey (0)
```

## 监听鼠标画图

setMouseCallback(windowName, onMouse, param=None)

```
import cv2
import numpy as np

drawing=False
mode=True
ix,iy=-1,-1

def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
    # 当按下左键是返回起始位置坐标
    if event==cv2.EVENT_LBUTTONDOWN: # 当鼠标按下时变为True
        drawing=True
        ix,iy=x,y
    elif event==cv2.EVENT_MOUSEMOVE and flags==cv2.EVENT_FLAG_LBUTTON: # 当鼠标左键按下并移动是绘制图形。event 可以查看移动，flag 查看是否按下
        if drawing==True:
            if mode==True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                # 绘制圆圈，小圆点连在一起就成了线，3 代表了笔画的粗细
                # cv2.circle(img,(x,y),3,(0,0,255),-1)
                # 起始点为圆心，起点到终点为半径的
                r=int(np.sqrt((x-ix)**2+(y-iy)**2))
                cv2.circle(img,(x,y),r,(0,0,255),-1)

        elif event==cv2.EVENT_LBUTTONUP: # 当鼠标松开停止绘画。
            drawing==False
        # if mode==True:
        # cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        # else:
        # cv2.circle(img,(x,y),5,(0,0,255),-1)

img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle) # 创建图像与窗口并将窗口与回调函数绑定
while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'): # 如果mode 为true 绘制矩形。按下'm' 变成绘制曲线。 
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()
```

## 获取像素值

img[x行、列、通道]

px=img[100, 100]
print px # 输出 [57 63 68]
blue=img[100, 100, 0]
print blue # 输出 BGR 通道的第一个 57

Numpy array.item() 和array.itemset()

img.item(10, 10, 2)
print img.item(10,10,2) # 输出 BGR 通道的R通道 50
img.itemset((10,10,2),100)
print img.item(10,10,2) # 输出 100

## 获取图像属性
属性包括行、列、通道、图像数据类型、像素数目

img.shape 获取图像形状，返回值是包含行数、列数、通道数的元组。灰度图返回值只有行数和列数，
可以判断是灰度图还是彩色图
img.shape # 输出 (280, 450, 3)

img.size 获取像素数目
img.size # 输出 378000

img.dtype 获取图像的数据类型
img.dtype # 输出 uint8

## 图像 ROI 
截取指定区域图像

ball=img[280:340,330:390]
img[273:333,100:160]=bal
获取指定区域图像，覆盖该区域

## 图像通道拆分与合并

b,g,r=cv2.split(img)
img=cv2.merge(b,g,r)

下面使用 numpy 操作，是推荐用法

import numpy as np
b=img[:,:,0] # 取 b 通道
img[:,:,2]=0 # 设置红色通道所有值为0

## 图像的算术运算

加法操作
cv2.add()
cv2.addWeighted()

OpenCV的加法和 Numpy 的加法不一样，前者是饱和操作，后者是模操作，一般选择前者进行操作
OpenCV -- cv2.add() 
Numpy -- res=img1+img2
 
x = np.uint8([250])
y = np.uint8([10])
print cv2.add(x,y) # 250+10 = 260 => 255
[[255]]
print x+y # 250+10 = 260 % 256 = 4
[4]

比例混合
按照不同权重叠加图片，注意大小尺寸要一样，图片无需指定类型，可同为jpg

```
import cv2
import numpy as np
img1=cv2.imread('1.png')
img2=cv2.imread('2.jpg')
dst=cv2.addWeighted(img1,0.7,img2,0.5,0)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindow()
```

## 按位运算
AND、OR、NOT、XOR
要把一个标志放到另一幅图像上，如果是矩形可以使用ROI，不过不是矩形可以使用按位运算实现

```
import cv2
import numpy as np
img1 = cv2.imread('roi.jpg')
img2 = cv2.imread('opencv_logo.png')

# I want to put logo on top-left corner, So I create a ROI
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols ]

# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 175, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
# 取roi 中与mask 中不为零的值对应的像素的值，其他值为0
# 注意这里必须有mask=mask 或者mask=mask_inv, 其中的mask= 不能忽略
img1_bg = cv2.bitwise_and(roi,roi,mask = mask)

# 取roi 中与mask_inv 中不为零的值对应的像素的值，其他值为0。
# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask_inv)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst
cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

## 颜色空间转换
OpenCV中有超过150种进行颜色空间转换的方法。常用的是BGR<-->Gray和BGR<-->HSV

cv2.cvtColor()，cv2.inRange()

cv2.cvtColor(input_image，flag)
flag 是转换类型
BGR<-->Gray 使用的 flag 是cv2.COLOR_BGR2GRAY
BGR<-->HSV  使用的 flag 是cv2.COLOR_BGR2HSV

OpenCV 的HSV 格式中
- H（色彩/色度）的取值范围是[0，179]
- S（饱和度）的取值范围[0，255]
- V（亮度）的取值范围[0，255]

将BGR转为HSV后可以简单的获取特定的颜色
```
import cv2
import numpy as np
img = cv2.imread(r'D:\1.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red = np.array([0,43,46])
upper_red = np.array([10,255,255])

mask = cv2.inRange(hsv, lower_red, upper_red) # 根据阈值构建掩模
res = cv2.bitwise_or(img, img, mask=mask) # 对原图像和掩模进行位运算

cv2.imshow('img',img)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

## 旋转图像
cv2.getRotationMatrix2D(center, angle, scale)
- 参数1旋转中心
- 参数2旋转角度
- 旋转后的缩放因子

cv2.warpAffine(src, M, dsize, dst=None, flags=None, borderMode=None, borderValue=None)

```
import cv2
import numpy as np
img = cv2.imread(r'D:\1.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

rows, cols = gray.shape

M = cv2.getRotationMatrix2D((rows/2, cols/2), 45, 0.6)
dst=cv2.warpAffine(img, M, (rows, cols))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

## 透视变化
输入图上找到4个点坐标，任意3个点都不能共线 
cv2.getPerspectiveTransform(src, dst)

## 图像阈值

简单阈值
当像素值高于阈值时，给像素赋予一个新值，否则赋予另一种颜色
cv2.threshold(src, thresh, maxval, type, dst=None)
- 参数1是原图像，应该是灰度图
- 参数2对像素值进行分类的阈值
- 参数3当像素值高于或低于阈值时应赋予的新值
- 参数4阈值方法
  - cv2.THRESH_BINARY # 二值阈催化
  - cv2.THRESH_BINARY_INV # 反向二值阈催化 
  - cv2.THRESH_TRUNC # 截断阈值化
  - cv2.THRESH_TOZERO # 超过阈值被设置为0
  - cv2.THRESH_TOZERO_INV # 低于阈值被置为0
```
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread(r'D:\1.jpg', 0)
ret,thresh1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2,3,i+1),
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),
    plt.yticks([])
plt.show()
```

自适应阈值
简单阈值是全局阈值，整幅图像采用一个值作为阈值，针对不同区域不同亮度情况下，采用不同的阈值
adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C, dst=None)
- adaptiveMethod 指定计算阈值的方法
  - cv2.ADPTIVE_THRESH_MEAN_C：阈值取自相邻区域的平均值
  - cv2.ADPTIVE_THRESH_GAUSSIAN_C：阈值取值相邻区域的加权和，权重为一个高斯窗口。
- blockSize - 邻域大小（用来计算阈值的区域大小)
- C 一个常数，阈值就等于的平均值或者加权平均值减去这个常数。
```
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread(r'D:\1.jpg', 0)
# 中值滤波
img = cv2.medianBlur(img, 5)
ret,th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
#11 为Block size, 2 为C 值
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
titles = ['Original Image', 'Global Thresholding (v = 127)',
'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]
for i in range(4):
    plt.subplot(2,2,i+1),
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),
    plt.yticks([])
plt.show()
```

Otsu's 二值化
在全局阈值是，随便取一个数来做阈值，如何判断选择的数好坏，只能是不停的尝试。
如果是一副双峰图像(图像直方图存在两个峰)，理论上应该在两个峰之间的峰谷选择一个最优值，这就使用Otsu's 二值化

cv2.threshold()，但是需要多传入一个参数
（flag）：cv2.THRESH_OTSU。这时要把阈值设为0。然后算法会找到最
优阈值，这个最优阈值就是返回值retVal。如果不使用Otsu 二值化，返回的
retVal 值与设定的阈值相等。
```
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r'D:\1.jpg', 0)
# global thresholding
ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# Otsu's thresholding
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Otsu's thresholding after Gaussian filtering
#（5,5）为高斯核的大小，0 为标准差
blur = cv2.GaussianBlur(img,(5,5),0)

# 阈值一定要设为0！
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# plot all the images and their histograms
images = [img, 0, th1, img, 0, th2, blur, 0, th3]
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
          'Original Noisy Image','Histogram',"Otsu's Thresholding",
          'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

# 这里使用了pyplot 中画直方图的方法，plt.hist, 要注意的是它的参数是一维数组
# 所以这里使用了（numpy）ravel 方法，将多维数组转换成一维，也可以使用flatten 方法
#ndarray.flat 1-D iterator over an array.
#ndarray.flatten 1-D array copy of the elements of an array in row-major order.

for i in range(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()
```

## 图像平滑
使用不同的低通滤波器对图像进行模糊

低通滤波器 LFP ，去除噪声，模糊图像
高通滤波器 HPF ，查找边缘

5*5 平均滤波器核

将核放在图像的像素A上，求与核对应的图像上(5*5)个像素的和，求取平均数，用平均数代替A的值，循环操作

```
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread(r'D:\1.jpg', 0)
kernel = np.ones((5,5),np.float32)/25

#cv.Filter2D(src, dst, kernel, anchor=(-1, -1))
#ddepth –desired depth of the destination image;
#if it is negative, it will be the same as src.depth();
#the following combinations of src.depth() and ddepth are supported:
#src.depth() = CV_8U, ddepth = -1/CV_16S/CV_32F/CV_64F
#src.depth() = CV_16U/CV_16S, ddepth = -1/CV_32F/CV_64F
#src.depth() = CV_32F, ddepth = -1/CV_32F/CV_64F
#src.depth() = CV_64F, ddepth = -1/CV_64F
#when ddepth=-1, the output image will have the same depth as the source.

dst = cv2.filter2D(img,-1,kernel)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()
```

OpenCV 四种模糊技术
- 平均，由一个归一化卷积框完成。用卷积框覆盖区域所有像素的平均值来代替中心元素
  利用函数 cv2.blur() 和 cv2.boxFilter() 来完成
```
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread(r'D:\1.jpg')
blur = cv2.blur(img,(5,5))
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
```

- 高斯模糊，把卷积核换成高斯核。除高斯噪声
简单来说，方框不变，原来每个方框中相等的值，现在变成符合高斯分布的值，方框中心的值最大，
其余方框根据距离中心元素的距离递减，构成一个高斯小山包。原来的求平均数现在变成求加权平均数，全就是方框里的值。

实现函数 cv2.GaussianBlur()，指定高斯核的宽和高(必须是奇数)，高斯函数x,y方向的标准差
如果只指定x方向的标准差，y方向也会取同样的值。如果都为0，函数会根据核函数的大小自己计算。

blur = cv2.GaussianBlur(img,(5,5),0) # 0 是指根据窗口大小（5,5）来计算高斯函数标准差

- 中值模糊，用与卷积框对应像素的中值来替代中心像素的值。除椒盐噪声
中值滤波是中心像素周围的值来取代他，卷积核的大小也是一个奇数

median = cv2.medianBlur(img,5)

- 双边滤波，保持边界清晰条件下有效去除噪声，计算量大，速度慢
高斯滤波器只考虑像素之间的空间关系，不会考虑像素值之间的关系，因此高斯滤波不会考虑像素是否处于边界，导致边界会模糊。

双边滤波使用空间高斯权重和灰度值相似性高斯权重，空间高斯函数确保只有邻近区域的像素对中心点有影响
灰度值相似性高斯函数确保只有与中心像素灰度值相近的才会被用来做高斯模糊。
```
blur = cv2.bilateralFilter(img, 9, 75, 75)

# cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace)
# d – Diameter of each pixel neighborhood that is used during filtering.
# If it is non-positive, it is computed from sigmaSpace
# 9 邻域直径，两个75 分别是空间高斯函数标准差，灰度值相似性高斯函数标准差
```

## 形态转换

```
import cv2
import numpy as np
img = cv2.imread(r'D:\1.jpg', 0)
kernel = np.ones((5,5),np.uint8)
```

- 腐蚀 erosion = cv2.erode(img,kernel,iterations = 1)
- 膨胀 dilation = cv2.dilate(img,kernel,iterations = 1)
- 开运算，先进行腐蚀再进行膨胀，用来除噪声 opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
- 闭运算，先膨胀再腐蚀，用来填充前景物体中的小洞，或者小黑点 closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

形态学梯度，就是一幅图像膨胀与腐蚀的差别，形态上是前景物体的轮廓
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

## 图像梯度
梯度简单来说就是求导

OpenCV 提供三种不同的梯度滤波器，或者说高通滤波器
- Sobel
- Scharr
- Laplacian
Sobel 和 Scharr 本质是求一阶或二阶导数。
Scharr 是对Sobel(使用小的卷积核求解梯度角度时)的优化，Laplacian求二阶倒数

Sobel 算子是高斯平滑与微分操作的结合体


---


## 最小外界圆
找到一个对象的外切圆，是所有能够包含对象的圆中面积最小的一个

cv2.minEnclosingCircle()
