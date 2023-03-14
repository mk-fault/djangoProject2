# -*- coding:utf-8 -*-
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
# 小写字母，去除可能会造成干扰的i，l，o，z
_letter_cases = "abcdefghjkmnpqrstuvwxy"
# 大写字母
_upper_cases = _letter_cases.upper()
# 数字
_numbers = ''.join(map(str, range(3, 10)))
init_chars = ''.join((_letter_cases, _upper_cases, _numbers))


def check_code(width=160,
               height=40,
               char_length=4,
               font_file=r'app01\static\other\monaco.ttf',
               font_size=25,
               chars=init_chars):
    """生成验证码"""


    code = []
    img = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img, mode='RGB')


    def rndChar():
        """
        生成随机字母
        :return:
        """
        return random.choice(chars)

    def rndColor():
        """
        生成随机颜色
        :return:
        """
        return (random.randint(0, 255), random.randint(10, 255), random.randint(64, 255))

    # 写文字
    font = ImageFont.truetype(font_file, font_size)
    for i in range(char_length):
        char = rndChar()
        code.append(char)
        h = random.randint(0, 2)
        draw.text([i * width / (char_length + 1), h], char, font=font, fill=rndColor())

    # 写干扰点
    for i in range(40):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=rndColor())

    # 写干扰圆圈
    for i in range(40):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=rndColor())
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.arc((x, y, x + 4, y + 4), 0, 90, fill=rndColor())

    # 画干扰线
    for i in range(5):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)

        draw.line((x1, y1, x2, y2), fill=rndColor())

    # 图形扭曲参数
    params = [1 - float(random.randint(1, 2)) / 100,
              0,
              0,
              0,
              1 - float(random.randint(1, 10)) / 100,
              float(random.randint(1, 2)) / 500,
              0.001,
              float(random.randint(1, 2)) / 500
              ]
    # 创建扭曲
    img = img.transform((width, height), Image.PERSPECTIVE, params)
    # 滤镜，边界加强（阈值更大）
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)

    return img, ''.join(code)


if __name__ == '__main__':
    img,str = check_code()
    print(str)
    img.save('demo.png')
