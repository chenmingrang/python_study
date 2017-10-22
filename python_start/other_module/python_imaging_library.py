#除了内建的模块外，Python还有大量的第三方模块。
#基本上，所有的第三方模块都会在PyPI - the Python Package Index上注册，只要找到对应的模块名字，即可用pip安装
#图像处理标准库Pillow

#命令行安装Pillow
#pip install pillow

from PIL import Image

im = Image.open('test.jpg')
#获得尺寸
w, h = im.size

print('original image size:%sX%s' % (w, h))
#图像缩放到50%
im.thumbnail((w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('thumbnail.jpg', 'jpeg')

w1, h1 = im.size
print('thumbnail image size:%sX%s' % (w1, h1))


#其他功能如切片、旋转、滤镜、输出文字、调色板等一应俱全。

#模糊效果

from PIL import Image, ImageFilter

#打开一个文件
im = Image.open('test.jpg')
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')


#PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。比如要生成字母验证码图片

from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

def random_char():
    return chr(random.randint(65,90))#大写字母

def random_color():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def random_color2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


width = 60*4
height = 60
image = Image.new("RGB", (width, height), (255, 255, 255))
font = ImageFont.truetype('ARIALN.TTF', 36)

draw = ImageDraw.Draw(image)

for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=random_color())


for t in range(4):
    draw.text((60*t +10, 10), random_char(), font=font, fill= random_color2())

image = image.filter(ImageFilter.MedianFilter)
image.save('code.jpg', 'jpeg')