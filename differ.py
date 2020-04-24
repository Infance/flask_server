import datetime
import math
import operator
import time
from datetime import date
from functools import reduce

import data as data
from PIL import Image, ImageChops, ImageGrab

# 截图生成的RGBA格式的图片无法对比，需要转换成RGB格式
# def img2jpg(imgFile):
#     if type(imgFile) == str and imgFile.endswith(('.bmp', '.gif', '.png')):
#         with Image.open(imgFile) as im:
#             im.convert('RGB').save(imgFile[:-3] + 'jpg')

# img2jpg('D:/desktop/image/1.png')
# img2jpg('D:/desktop/image/2.png')

# im1 = Image.open('D:/desktop/image/1.jpg')
# im2 = Image.open('D:/desktop/image/2.jpg')
# im3 = ImageChops.difference(im1, im2)
# im3.save('D:/desktop/image/3.jpg')
# print(im3.mode)

# 获取当前时间戳
timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')

# 截全屏获取图片
time.sleep(5)
_im1 = ImageGrab.grab()
print(_im1.mode)
print(timestamp)
time.sleep(2)
_im2 = ImageGrab.grab()

# _im1.save('D:/desktop/image/5.jpg')  保存图片

h1 = _im1.histogram()
h2 = _im2.histogram()
# 对比图片，返回浮点数
result = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))

# im1 = Image.open(_im1)
# im2 = Image.open(_im2)

im3 = ImageChops.difference(_im1, _im2)
im3.save('D:/desktop/image/3.jpg')
print(result)

# print(_im1)
# print(im3.mode)
