import logging
import math
import operator
from functools import reduce

from PIL import Image
from PIL import ImageChops


# 转换图像格式
def img2jpg(imgFile):
    if type(imgFile) == str and imgFile.endswith(('.bmp', '.gif', '.png')):
        with Image.open(imgFile) as im:
            im.convert('RGB').save(imgFile[:-3] + 'jpg')


def compare_images(path_one, path_two, diff_save_location):
    """
    比较图片，如果有不同则生成展示不同的图片
    如果两张图片完全相等，则返回结果为浮点类型“0.0”，如果不相同则返回结果值越大

    @参数一: path_one: 第一张图片的路径
    @参数二: path_two: 第二张图片的路径
    @参数三: diff_save_location: 不同图的保存路径
    """

    # 转换图像格式

    result = 0
    image_one = Image.open(path_one)
    image_two = Image.open(path_two)
    try:
        diff = ImageChops.difference(image_one, image_two)
        # h1 = image_one.histogram()
        # h2 = image_one.histogram()
        # 对比图片，返回浮点数
        # result = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))

        if diff.getbbox() is None:
            # 图片间没有任何不同则直接退出
            print("【+】We are the same!")
        else:
            diff.save(diff_save_location)
    except ValueError as e:
        text = ("表示图片大小和box对应的宽度不一致，参考API说明：Pastes another image into this image."
                "The box argument is either a 2-tuple giving the upper left corner, a 4-tuple defining the left, upper, "
                "right, and lower pixel coordinate, or None (same as (0, 0)). If a 4-tuple is given, the size of the pasted "
                "image must match the size of the region.使用2纬的box避免上述问题")
        print("【{0}】{1}".format(e, text))

    # 记录日志
    # file_handler = logging.FileHandler(filename='x1.log', mode='a', encoding='utf-8', )
    # logging.basicConfig(
    #     format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
    #     datefmt='%Y-%m-%d %H:%M:%S %p',
    #     handlers=[file_handler, ],
    #     level=logging.ERROR)
    # logging.error(str(result))


# 截图
# im = ImageGrab.grab((0, 0, 800, 200))  # 截取屏幕指定区域的图像
# im = ImageGrab.grab()  # 不带参数表示全屏幕截图
# 裁剪粘贴图像
# box = (120, 194, 220, 294)  # 定义裁剪区域
# region = im.crop(box)  # 裁剪
# region = region.transpose(Image.ROTATE_180)
# im.paste(region, box)  # 粘贴


if __name__ == '__main__':
    compare_images('D:\desktop\image\1.png',
                   'D:\desktop\image\2.png',
                   'D:\desktop\image\3.png')
