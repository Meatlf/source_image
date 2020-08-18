# 参考资料：
# [1] [布雷森汉姆直线算法](https://zh.wikipedia.org/wiki/%E5%B8%83%E9%9B%B7%E6%A3%AE%E6%BC%A2%E5%A7%86%E7%9B%B4%E7%B7%9A%E6%BC%94%E7%AE%97%E6%B3%95)
# [2] [布雷森汉姆直线算法](http://www.twinklingstar.cn/2013/293/bresenham-line-algorithm/)
# [3] [NumPy数组初始化（填充相同的值）](http://cn.voidcc.com/question/p-trailrsz-nt.html)
import numpy as np
import cv2
import matplotlib.pyplot as plt
import math

def bresenham_lineV1(img, x0, y0, x1, y1, color):
     deltax = x1 - x0
     deltay = y1 - y0
     error = 0
     deltaerr = deltay / deltax    # 假設deltax != 0（非垂直線），
           # 注意：需保留除法運算結果的小數部份
     y = y0
     for x in range(x0, x1):
         setPixel(img, x,y, color)
         error = error + deltaerr
         if abs (error) >= 0.5:
             y = y + 1
             error = error - 1.0

def swap(a,b):
    temp = a
    a = b
    b = temp

# 最佳化
def bresenham_lineV2(img, x0, y0, x1, y1, color):
    steep = abs(y1 - y0) > abs(x1 - x0)
    if steep:
        swap(x0, y0)
        swap(x1, y1)

    if x0 > x1:
        swap(x0, x1)
        swap(y0, y1)
    deltax = x1 - x0
    deltay = abs(y1 - y0)
    error = deltax / 2
    y = y0
    if y0 < y1:
        ystep = 1
    else:
        ystep = -1

    for x in range(x0, x1):
        if steep:
            setPixel(img, y, x, color)
        else:
            setPixel(img, x, y, color)
        error = error - deltay
        if error < 0:
            y = y + ystep
            error = error + deltax

def bresenham_lineV3(img, x1, y1, x2, y2, color):
    w = x2 - x1
    h = y2 - y1
    dx = ((w > 0) << 1) - 1
    dy = ((h > 0) << 1) - 1
    w = abs(w)
    h = abs(h)

    if w > h:
        f = 2*h - w
        delta1 = 2*h + 0.01
        delta2 = (h-w)*2
        y = y1
        for x in range(x1, x2, dx):
            setPixel(img, x, y, color)
            if f < 0:
                f += delta1
            else:
                y += dy
                f += delta2
        setPixel(img, x, y, color)
    else:
        f = 2*w - h
        delta1 = w*2
        delta2 = (w-h)*2
        x = x1
        for y in range(y1, y2, dy):
            setPixel(img, x, y, color)
            if f < 0:
                f += delta1
            else:
                x += dx
                f += delta2
        setPixel(img, x, y, color)

def setPixel(img, x, y, color):
    img[x][y] = color

width = 90
height = 60
img = np.full((width, height, 3), 255, dtype="uint8")
x1 = 0
y1 = 0
x2 = width - 1
y2 = height - 1
color = 0
bresenham_lineV3(img, x1, y1, x2, y2, color)
plt.imshow(img)
plt.show()