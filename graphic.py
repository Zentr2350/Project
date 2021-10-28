from math import *
from PIL import Image, ImageDraw

im = Image.new("RGB", (1000, 1000), (255, 255, 255))
draw = ImageDraw.Draw(im)
draw.line((500, 0, 500, 1000), fill=(0, 0, 0), width=5)
draw.line((0, 500, 1000, 500), fill=(0, 0, 0), width=5)
for i in range(0, 1001, 50):
    draw.line((i, 505, i, 495), fill=(0, 0, 0), width=5)
    draw.line((495, i, 505, i), fill=(0, 0, 0), width=5)
c = ''
a = input()
for i in range(-10000, 10000):
    a = a.replace('x', 'i')

    try:
        a = a.replace('c', 'i')


        i /= 1000
        c = i - (1/1000)
        draw.line((i * 50 + 500, (0 - eval(a)) * 50 + 500, i * 50 + 500, (0 - eval(a)) * 50 + 500), fill=(0, 0, 0), width=3)
        a = a.replace('i', 'c')
        draw.line((i * 50 + 500, (0 - eval(a.replace('c', 'i'))) * 50 + 500, c * 50 + 500, (0 - eval(a)) * 50 + 500), fill=(0, 0, 0),
                  width=3)

    except Exception as e:
        # print(e)
        pass
im.save('gr.jpg')

