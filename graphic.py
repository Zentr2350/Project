from math import *
from PIL import Image, ImageDraw

im = Image.new("RGB", (1000, 1000), (255, 255, 255))
draw = ImageDraw.Draw(im)
draw.line((500, 0, 500, 1000), fill=(0, 0, 0), width=3)
draw.line((0, 500, 1000, 500), fill=(0, 0, 0), width=3)
for i in range(0, 1001, 50):
    draw.line((i, 505, i, 495), fill=(0, 0, 0), width=3)
    draw.line((495, i, 505, i), fill=(0, 0, 0), width=3)
a = input()
l = int(input())
cht = ''
for irt in range(-10000, 10000):
    a = a.replace('x', 'irt')

    try:
        a = a.replace('cht', 'irt')

        irt /= 1000
        cht = irt - (1 / 1000)
        draw.line((irt * 50 * l + 500, (0 - eval(a)) * l * 50 + 500, irt * l * 50 + 500, (0 - eval(a)) * l * 50 + 500), fill=(0, 0, 0),
                  width=2)
        a = a.replace('irt', 'cht')
        if abs(((0 - eval(a.replace('cht', 'irt'))) * 50 * l + 500) - ((0 - eval(a)) * l * 50 + 500)) < 100:
            draw.line(
                (irt * 50 * l + 500, (0 - eval(a.replace('cht', 'irt'))) * l * 50 + 500, cht * 50 * l + 500, (0 - eval(a)) * l * 50 + 500),
                fill=(0, 0, 0),
                width=2)

    except Exception as e:
        print(e)
        pass

im.save('gr.jpg')
