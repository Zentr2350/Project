from math import *
from PIL import Image, ImageDraw

img = Image.open(input())

colorPixel = []
for i in range(img.size[0]):
    for g in range(img.size[1]):
        pixel = img.getpixel((i, g))
        colorPixel.append(pixel)
a = 0
b = False
c = False
d = 0
for i in colorPixel[:img.size[0]]:
    if i != (255, 255, 255):
        c = True
        for g in colorPixel[a:1000000:1000]:
            if g == (255, 255, 255):
                b = True
                break
    if b:
        b = False
        c = False
    elif c:
        print(a)
        b = c = False
        break
    a += 1

for i in colorPixel[0:1000000:1000]:
    if i != (255, 255, 255):
        c = True
        for g in colorPixel[d:d + 1000]:
            if g == (255, 255, 255):
                b = True
                break
    if b:
        b = False
        c = False
    elif c:
        d /= 1000
        b = c = False
        break
    d += 1000