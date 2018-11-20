# OpenCV 开源计算机视觉库

[项目地址](https://github.com/opencv/opencv) https://github.com/opencv/opencv

[中文社区](http://www.opencv.org.cn/forum.php?gid=7) http://www.opencv.org.cn/forum.php?gid=7 

https://arxiv.org

## 安装使用
```
pip install numpy Matplotlib
pip install opencv-python
```

## 打开本地图片
```python
import cv2

img = cv2.imread(r"C:\Users\Administrator\Pictures\Camera Roll\1.jpg")
cv2.namedWindow("Image")
cv2.imshow("Image", img)
cv2.waitKey (0)
cv2.destroyAllWindows()
```

## 保存图片

cv2.imwrite(r"D:\12.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 85])
- 参数1 保存的路径及文件名
- 参数2 图像矩阵
- 参数3 可选
  对于 jpeg 表示图像的质量为0-100的整数，默认95，cv2.IMWRITE_JPEG_QUALITY 类型为Long，必须转换为int
  对于 png 表示压缩级别为 0-9的整数，默认3，数字越大，压缩级别越高，尺寸越小 

## 模拟椒盐
```
import cv2
import numpy as np

def salt(img, n):
    for i in range(n):
        j = int(np.random.random() * img.shape[1])
        k = int(np.random.random() * img.shape[0])
        if img.ndim == 2:  # 灰度图
            img[k, j] = 255
        else:
            img[k, j, 0] = 255
            img[k, j, 1] = 255
            img[k, j, 2] = 255
    return img

if __name__=='__main__':
    img = cv2.imread(r"C:\Users\Administrator\Pictures\Camera Roll\1.jpg")
    saltImage = salt(img, 10000)
    cv2.imshow("Image", saltImage)
    cv2.imwrite(r"D:\12.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
    cv2.waitKey (0)
    cv2.destroyAllWindows()
```
## 分离通道与合并

```
b, g, r = cv2.split(img)  # b = cv2.split(img)[0]
merged = cv2.merge([b,g,r]) 
cv2.imshow("Image1", b)
cv2.imshow("Image2", g)
cv2.imshow("Image3", r)
cv2.imshow("Image4", merged)
```
## Canny 边缘检测

def Canny(image, threshold1, threshold2, edges=None, apertureSize=None, L2gradient=None):
  pass
  
- 第一个参数是需要处理的原图像，该图像必须为单通道的灰度图；
- 第二个参数是阈值1，数值较小，用于将间隔的边缘连接起来
- 第三个参数是阈值2，数值较大，用于检测图像中明显的边缘
- apertureSize，Sobel算子的大小
- L2gradient，布尔值，为真使用更精确L2范数进行计算（即两个方向的倒数的平方和再开方），否则使用L1范数（直接将两个方向导数的绝对值相加）

```
import cv2

if __name__=='__main__':
    img = cv2.imread(r"D:\1.jpg")
    img2 = cv2.imread(r"D:\1.jpg", 0)
    cv2.imshow('Img', img)
    img2 = cv2.GaussianBlur(img2, (3, 3), 0)
    canny = cv2.Canny(img2, 50, 150)
    cv2.imshow('Canny', canny)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```
动态调整 Canny 参数
```
import cv2

def CannyThreshold(lowThreshold):
    detected_edges = cv2.GaussianBlur(gray, (3, 3), 0)
    detected_edges = cv2.Canny(detected_edges, lowThreshold, lowThreshold * ratio, apertureSize=kernel_size)
    dst = cv2.bitwise_and(img, img, mask=detected_edges)  # just add some colours to edges from original image.
    cv2.imshow('canny demo', dst)


if __name__=='__main__':
    lowThreshold = 0
    max_lowThreshold = 100
    ratio = 3
    kernel_size = 3
    img = cv2.imread('D:/1.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.namedWindow('canny demo')
    cv2.createTrackbar('Min threshold', 'canny demo', lowThreshold, max_lowThreshold, CannyThreshold)
    CannyThreshold(0)  # initialization
    if cv2.waitKey(0) == 27:
        cv2.destroyAllWindows()

```
