import sys
from math import *
from PIL import Image, ImageDraw

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog
from PyQt5.QtGui import QPixmap
import sqlite3
from PyQt5.QtCore import Qt
from numpy import *


s = []

def gr(a, o=1, w=(0, 0, 0), name='gr.jpg', new=False, name2='', p=()):  # функция строящая график по заданной функции

    global s

    k = a
    con = sqlite3.connect("fp.sqlite")
    cur = con.cursor()
    cht = ''
    if not new:
        im = Image.new("RGB", (1000, 1000), (255, 255, 255))
    else:
        im = Image.open(name2)
    draw = ImageDraw.Draw(im)
    draw.line((500, 0, 500, 1000), fill=(0, 0, 0), width=3)
    draw.line((0, 500, 1000, 500), fill=(0, 0, 0), width=3)
    for i in range(0, 1001, 50):
        draw.line((i, 505, i, 495), fill=(0, 0, 0), width=3)
        draw.line((495, i, 505, i), fill=(0, 0, 0), width=3)
    cht = ''

    if o >= 1:
        for irt in range(int(-10000 // o), int(10000 // o)):
            a = a.replace('x', 'irt')

            try:
                a = a.replace('cht', 'irt')

                irt /= 1000
                cht = irt - (1 / 1000)
                draw.line(
                    (irt * 50 * o + 500, (0 - eval(a)) * o * 50 + 500, irt * o * 50 + 500, (0 - eval(a)) * o * 50 + 500),
                    fill=w,
                    width=2)
                s.append(irt)
                s.append(eval(a))
                a = a.replace('irt', 'cht')
                if abs(((0 - eval(a.replace('cht', 'irt'))) * 50 * o + 500) - ((0 - eval(a)) * o * 50 + 500)) < 100:
                    draw.line(
                        (irt * 50 * o + 500, (0 - eval(a.replace('cht', 'irt'))) * o * 50 + 500, cht * o * 50 + 500,
                         (0 - eval(a)) * 50 * o + 500),
                        fill=w,
                        width=2)


            except Exception as e:
                pass
        if o == 1:
            if cur.execute(f"select function from fpqt where function = '{k}'").fetchall() == []:
                cur.execute(f"""insert into fpqt(function, points) values('{k}', '{s}')""")
                con.commit()
                con.close()
        a = a.replace('cht', 'i[0]')
        for i in p:
            draw.line(
                (i[0] * 50 * o + 500 + 2, (0 - eval(a)) * o * 50 + 500, i[0] * o * 50 + 500 - 2, (0 - eval(a)) * o * 50 + 500),
                fill=(255, 0, 0),
                width=6)
        im.save(name)
    else:
        for irt in range(int(-10000), int(10000)):
            a = a.replace('x', 'irt')

            try:
                a = a.replace('cht', 'irt')

                irt /= 1000 * o
                gt = irt
                if cht == '':
                    cht = irt - (1 / 1000 * o)
                cy = gt - (1 / 1000)
                draw.line(
                    (
                    irt * 50 * o + 500, (0 - eval(a)) * o * 50 + 500, irt * o * 50 + 500, (0 - eval(a)) * o * 50 + 500),
                    fill=(0, 0, 0),
                    width=2)
                a = a.replace('irt', 'cht')
                if abs(((0 - eval(a.replace('cht', 'gt'))) * 50 * o + 500) - ((0 - eval(a.replace('cht', 'cy'))) * o * 50 + 500)) < 100:
                    draw.line(
                        (irt * 50 * o + 500, (0 - eval(a.replace('cht', 'irt'))) * o * 50 + 500, cht * o * 50 + 500,
                         (0 - eval(a)) * 50 * o + 500),
                        fill=(0, 0, 0),
                        width=2)
                # print(irt * 50 * o + 500, (0 - eval(a.replace('cht', 'irt'))) * o * 50 + 500, cht * o * 50 + 500,
                #          (0 - eval(a)) * 50 * o + 500)
                cht = irt

            except Exception as e:
                print(e)
                pass

        im.save(name)

def func(u):  # функция определяющая квадратичную функцию по графику параболы
    img = Image.open(u)
    x, y = img.size

    colorPixel = []
    for i in range(img.size[0]):
        for g in range(img.size[1]):
            pixel = img.getpixel((g, i))
            colorPixel.append(pixel)
    v = 0
    w = False
    e = False
    d = 0
    for i in colorPixel[:img.size[0]]:
        if i != (255, 255, 255):
            e = True
            for g in colorPixel[v:x * y:x]:
                if g == (255, 255, 255):
                    w = True
                    break
        if w:
            w = False
            e = False
        elif e:
            w = e = False
            break
        v += 1

    for i in colorPixel[0:x * y:x]:
        if i != (255, 255, 255):
            e = True
            for g in colorPixel[d:d + x]:
                if g == (255, 255, 255):
                    w = True
                    break
        if w:
            w = False
            e = False
        elif e:
            d /= y
            w = e = False
            break
        d += x
    d += 1
    v += 1
    j = 0
    for i in colorPixel[int(d * x - x * 3):int(d * x - 2 * x)]:
        if sum(i) < 750 and j > 5:
            if sum(colorPixel[int(d * x - 3 * x) + j * 2]) < 750:
                j += 1
                break
        j += 1
    g = 0
    k = []
    w = False
    e = True
    r = False
    m = n = 0
    q = False
    for i in range(1, x + 1):
        for t in colorPixel[i * x - x:i * x]:
            if sum(t) < 650 and (g < d - 8 or g > d + 8) and not w:
                w = True
                e = False
                q = True
                for z in range(g - 5, g + 5):
                    if z in k or z - (z - 500) * 2 in k:
                        r = True
                if not r and len(k) != 4 and (i < 495 or i > 507):
                    k.append(g)
                    k.append(-i + 501)
                r = False
            if sum(t) < 650 and (g < d - 8 or g > d + 8) and w and not q:
                w = False
                e = True
                for z in range(g - 5, g + 5):
                    if z in k or z - (z - 500) * 2 in k:
                        r = True
                if not r and len(k) != 4 and (i < 495 or i > 507):
                    k.append(g)
                    k.append(-i + 501)
                r = False
            g += 1
            q = False
        g = 0
        if not e or len(k) == 4:
            break

    if not e or len(k) == 4:
        for i in range(x + 1, 1, -1):
            for t in colorPixel[i * x - x:i * x]:
                if sum(t) < 650 and (g < d - 8 or g > d + 8):
                    for z in range(g - 5, g + 5):
                        if z in k:
                            r = True
                    if not r and len(k) != 6 and (i < 495 or i > 507):
                        k.append(g)
                        k.append(-i + 501)
                r = False
                g += 1
            g = 0

    k[0] -= 498
    k[2] -= 499
    k[4] -= 499

    for i in range(len(k)):
        k[i] /= 50
    x0 = k[0]
    y0 = k[1]
    x1 = k[2]
    y1 = k[3]
    x2 = k[4]
    y2 = k[5]
    q0 = (y0 - y1) * (x2 ** 2 - x0 ** 2)
    q1 = q0 / (x0 ** 2 - x1 ** 2) * (x0 + x1)
    q2 = y0 - y2
    q3 = q2 * (x0 + x1) + q1
    q4 = (x2 - x0) * (x0 + x1)
    q5 = (x2 ** 2 - x0 ** 2) - q4
    b = q3 / q5
    a = (b * (x1 - x0) + y0 - y1) / (x0 ** 2 - x1 ** 2)
    c = y0 - x0 ** 2 * a - x0 * b
    gr(f'{a:.2f} * x ** 2 + {b:.2f} * x + {c:.2f}', 1, (255, 0, 0), name='gr1.jpg', new=True, name2=u)
    return f'y = {a:.2f} * x ** 2 + {b:.2f} * x + {c:.2f}'

def lfunc(u):  # функция определяющаяя линейную функцию по ее графику
    img = Image.open(u)
    x, y = img.size

    colorPixel = []
    for i in range(img.size[0]):
        for g in range(img.size[1]):
            pixel = img.getpixel((g, i))
            colorPixel.append(pixel)
    v = 0
    w = False
    e = False
    d = 0
    for i in colorPixel[:img.size[0]]:
        if i != (255, 255, 255):
            e = True
            for g in colorPixel[v:x * y:x]:
                if g == (255, 255, 255):
                    w = True
                    break
        if w:
            w = False
            e = False
        elif e:
            w = e = False
            break
        v += 1

    for i in colorPixel[0:x * y:x]:
        if i != (255, 255, 255):
            e = True
            for g in colorPixel[d:d + x]:
                if g == (255, 255, 255):
                    w = True
                    break
        if w:
            w = False
            e = False
        elif e:
            d /= y
            w = e = False
            break
        d += x
    d += 1
    v += 1
    j = 0
    for i in colorPixel[int(d * x - x * 3):int(d * x - 2 * x)]:
        if sum(i) < 750 and j > 5:
            if sum(colorPixel[int(d * x - 3 * x) + j * 2]) < 750:
                j += 1
                break
        j += 1
    g = 0
    k = []
    w = False
    e = True
    r = False
    m = n = 0
    for i in range(1, x + 1):
        for t in colorPixel[i * x - x:i * x]:
            if sum(t) < 650 and (g < d - 8 or g > d + 8) and not w:
                for z in range(g - 5, g + 5):
                    if z in k:
                        r = True
                if i < 495 or i > 507:
                    k.append(g)
                    k.append(-i + 501)
                    e = False
                    break
                r = False
            g += 1
        if not e:
            break
    g = 0
    for i in range(x + 1, 1, -1):
        for t in colorPixel[i * x - x:i * x]:
            if sum(t) < 650 and (g < d - 8 or g > d + 8):
                for z in range(g - 5, g + 5):
                    if z in k:
                        r = True
                if i < 495 or i > 507:
                    k.append(g)
                    k.append(-i + 501)
                    w = True
                    break
            g += 1
        if w:
            break
    k[0] -= 498
    k[2] -= 499
    for i in range(len(k)):
        k[i] /= 50
    x0 = k[0]
    y0 = k[1]
    x1 = k[2]
    y1 = k[3]
    k = (y0 - y1) / (x0 - x1)
    b = y0 - (k * x0)
    gr(f'{k:.2} * x + {b:.2}', 1, (255, 0, 0), name='gr1.jpg', new=True, name2=u)
    return f'y = {k:.2} * x + {b:.2}'

def polinom(b):  # функция построения графика по точкам
    a = len(b)
    c = []
    d = []
    f = 1
    p = 0
    for i in range(a):
        for g in range(a):
            if g != i:
                e = poly1d([1, -b[g][0]])
                s = b[i][0] - b[g][0]
                c.append(e / s)
        for g in c:
            f = polymul(f, g)
        d.append(f * b[i][1])
        f = 1
        c = []
    for i in d:
        p += i
    p = str(p).split('\n')
    f = [i for i in p[1]]
    for i in range(len(p[0])):
        if p[0][i] != ' ':
            f.insert(i, f' ** {p[0][i]}')
    f = ''.join(f)
    f = f.replace('x', '* x')
    gr(f, p=b)
    return f


class MyWidget(QMainWindow):  # основное окно
    def __init__(self):
        super().__init__()
        uic.loadUi('gr.ui', self)  # Загружаем дизайн

        self.tabWidget.setTabText(2, 'ШАБЛОН')
        self.tabWidget.setTabText(0, 'Построение графика по функции')
        self.tabWidget.setTabText(1, 'Нахождение функции по графику')
        self.tabWidget.setTabText(3, 'Построение графика по точкам')
        self.pushButton.clicked.connect(self.gra)
        self.pixmap = QPixmap('shablon.jpg')
        self.image = self.label_7
        self.image.setPixmap(self.pixmap)
        self.pushButton_2.clicked.connect(self.x)
        self.k = 1
        self.label_12.hide()
        self.label_13.hide()
        self.label_11.hide()
        self.pushButton_3.clicked.connect(self.y)
        self.pushButton_5.clicked.connect(self.im)
        self.pushButton_4.clicked.connect(self.im1)
        self.label_20.hide()
        self.label_21.hide()
        self.label_22.hide()
        self.label_23.hide()
        self.label_24.hide()
        self.label_25.hide()
        self.label_30.hide()
        self.pushButton_5.hide()
        self.pushButton_6.clicked.connect(self.vibor)
        self.comboBox_2.hide()
        self.pushButton_6.hide()
        self.label_33.hide()
        self.label_34.hide()
        self.label_35.hide()
        self.lineEdit_3.hide()
        self.pushButton_8.hide()
        self.label_37.hide()
        self.label_38.hide()
        self.pushButton_7.clicked.connect(self.npoints)
        self.n = 0
        self.points = []
        self.pushButton_8.clicked.connect(self.polinomm)
        self.label_39.hide()
        self.label_40.hide()
        self.label_41.hide()
        self.label_42.hide()
        self.label_43.hide()
        self.label_44.hide()

    def y(self):
        self.ff = DataBase()
        self.ff.show()


    def x(self):
        if self.comboBox.currentText() == 'Увеличить':
            self.k *= int(self.lineEdit_2.text())
        else:
            self.k /= int(self.lineEdit_2.text())
        gr(self.lineEdit.text(), self.k, (0, 0, 0))
        self.label_12.setText(str(1 / self.k))
        self.label_13.setText(str(1 / self.k))

        self.pixmap = QPixmap('gr.jpg')
        self.image = self.label
        self.image.setPixmap(self.pixmap)

    def gra(self):
        gr(self.lineEdit.text(), 1, (0, 0, 0))
        self.k = 1
        self.label_12.setText(str(1 / self.k))
        self.label_13.setText(str(1 / self.k))
        self.pixmap = QPixmap('gr.jpg')
        self.image = self.label
        self.image.setPixmap(self.pixmap)
        self.label_11.show()
        self.label_12.show()
        self.label_13.show()

    def im(self):
        if self.bb == 'Линейной':
            a = lfunc(self.aa)
        else:
            a = func(self.aa)


        self.pixmap = QPixmap('gr1.jpg')
        self.image = self.label_17
        self.image.setPixmap(self.pixmap)
        self.label_39.show()
        self.label_40.show()
        self.label_41.show()
        self.label_25.setText(a)
        self.label_20.show()
        self.label_21.show()
        self.label_22.show()
        self.label_23.show()
        self.label_24.show()
        self.label_25.show()

    def im1(self):
        self.aa = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.pixmap = QPixmap(self.aa)
        self.image = self.label_17
        self.image.setPixmap(self.pixmap)
        self.label_39.show()
        self.label_40.show()
        self.label_41.show()
        self.label_30.show()
        self.comboBox_2.show()
        self.pushButton_6.show()

    def vibor(self):
        self.pushButton_5.show()
        self.bb = self.comboBox_2.currentText()

    def npoints(self):
        self.label_33.show()
        self.label_34.show()
        self.label_35.show()
        self.lineEdit_3.show()
        self.pushButton_8.show()
        self.n = int(self.spinBox.text())
        self.label_35.setText('')
        self.points = []

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter:
            try:
                if len(self.lineEdit_3.text().split(';')) == 2 and self.n != 0:
                    self.points.append((int(self.lineEdit_3.text().split(';')[0]), int(self.lineEdit_3.text().split(';')[1])))
                    self.n -= 1
                    self.label_35.setText(self.label_35.text() + f'{(int(self.lineEdit_3.text().split(";")[0]), int(self.lineEdit_3.text().split(";")[1]))}\n')
                    self.lineEdit_3.setText('')

            except Exception as e:
                pass

    def polinomm(self):
        a = polinom(self.points)
        self.label_38.setText(a)
        self.pixmap = QPixmap('gr.jpg')
        self.image = self.label_36
        self.image.setPixmap(self.pixmap)
        self.label_42.show()
        self.label_43.show()
        self.label_44.show()
        self.label_37.show()
        self.label_38.show()





class DataBase(QDialog):  # диаолговое окно
    def __init__(self):
        super().__init__()
        uic.loadUi('dtbs.ui', self)  # Загружаем дизайн
        self.con = sqlite3.connect("fp.sqlite")
        self.tabWidget.setTabText(1, 'Points')
        self.tabWidget.setTabText(0, 'Ввод')
        self.label_6.hide()
        self.pushButton_2.hide()
        self.spinBox.hide()
        self.pushButton.clicked.connect(self.ok)
        self.a = False
        self.pushButton_2.clicked.connect(self.ok1)
        self.b = 50
        self.pushButton_4.clicked.connect(self.right)
        self.pushButton_3.clicked.connect(self.left)
        self.m = self.n = self.v = False
        self.label_7.hide()

    def ok(self):
        cur = self.con.cursor()
        if self.comboBox.currentText() != 'Все точки':
            self.label_6.show()
            self.pushButton_2.show()
            self.spinBox.show()
        else:
            a = ''
            self.r = cur.execute(f"SELECT points FROM fpqt WHERE function = '{self.lineEdit.text()}'").fetchall()
            self.r = self.r[0][0][1:-1].split(', ')
            self.c = 1
            for i in range(1, self.b, 2):
                a += f'{self.c}) x = {self.r[i - 1]}\ty = {self.r[i]}\n'
                self.c += 1
            self.label_8.setText(a)
            self.label_6.hide()
            self.pushButton_2.hide()
            self.spinBox.hide()
            self.a = True
            self.label_7.show()
            self.pushButton_3.show()
            self.pushButton_4.show()

    def ok1(self):
        a = ''
        cur = self.con.cursor()
        self.b = 50
        self.c = 1
        d = []
        self.r = cur.execute(f"SELECT points FROM fpqt WHERE function = '{self.lineEdit.text()}'").fetchall()
        self.r = self.r[0][0][1:-1].split(', ')
        if self.comboBox.currentText() == 'Точки у которых у Х n знаков после запятой':
            for i in range(1, len(self.r), 2):
                if float(self.r[i - 1]) == float(f'{float(self.r[i - 1]):.{self.spinBox.text()}f}'):
                    d.append(self.r[i - 1])
                    d.append(self.r[i])
            self.r = d
            try:
                for i in range(1, self.b, 2):
                    a += f'{self.c}) x = {self.r[i - 1]}\ty = {self.r[i]}\n'
                    self.c += 1
            except Exception:
                pass
        elif self.comboBox.currentText() == 'Точки у кторых у Y n знаков после запятой':
            for i in range(1, len(self.r), 2):
                if float(self.r[i]) == float(f'{float(self.r[i]):.{self.spinBox.text()}f}'):
                    d.append(self.r[i - 1])
                    d.append(self.r[i])
            self.r = d
            try:
                for i in range(1, self.b, 2):
                    a += f'{self.c}) x = {self.r[i - 1]}\ty = {self.r[i]}\n'
                    self.c += 1
            except Exception:
                pass
        else:
            for i in range(1, len(self.r), 2):
                if float(self.r[i - 1]) == float(f'{float(self.r[i - 1]):.{self.spinBox.text()}f}') and float(self.r[i]) \
                        == float(f'{float(self.r[i]):.{self.spinBox.text()}f}'):
                    d.append(self.r[i - 1])
                    d.append(self.r[i])
            self.r = d
            try:
                for i in range(1, self.b, 2):
                    a += f'{self.c}) x = {self.r[i - 1]}\ty = {self.r[i]}\n'
                    self.c += 1
            except Exception:
                pass
        if self.c <= 25:
            self.pushButton_3.hide()
            self.pushButton_4.hide()
        else:
            self.pushButton_3.show()
            self.pushButton_4.show()
        self.label_8.setText(a)
        self.label_7.show()


    def right(self):
        if self.b > len(self.r) - 50:
            pass
        else:
            self.b += 50
            a = ''
            for i in range(self.b - 49, self.b, 2):
                a += f'{self.c}) x = {self.r[i - 1]}\ty = {self.r[i]}\n'
                self.c += 1
            self.label_8.setText(a)

    def left(self):
        if self.b == 50:
            pass
        else:
            self.b -= 50
            self.c -= 50
            a = ''
            for i in range(self.b - 49, self.b, 2):
                a += f'{self.c}) x = {self.r[i - 1]}\ty = {self.r[i]}\n'
                self.c += 1
            self.label_8.setText(a)



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
