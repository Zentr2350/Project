import sys
from math import *
from PIL import Image, ImageDraw

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtGui import QPixmap
import sqlite3




def gr(a, o):
    k = a
    con = sqlite3.connect("fp.sqlite")
    cur = con.cursor()
    cht = ''
    im = Image.new("RGB", (1000, 1000), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    draw.line((500, 0, 500, 1000), fill=(0, 0, 0), width=3)
    draw.line((0, 500, 1000, 500), fill=(0, 0, 0), width=3)
    for i in range(0, 1001, 50):
        draw.line((i, 505, i, 495), fill=(0, 0, 0), width=3)
        draw.line((495, i, 505, i), fill=(0, 0, 0), width=3)
    cht = ''
    s = []
    if o >= 1:
        for irt in range(int(-10000 // o), int(10000 // o)):
            a = a.replace('x', 'irt')

            try:
                a = a.replace('cht', 'irt')

                irt /= 1000
                cht = irt - (1 / 1000)
                draw.line(
                    (irt * 50 * o + 500, (0 - eval(a)) * o * 50 + 500, irt * o * 50 + 500, (0 - eval(a)) * o * 50 + 500),
                    fill=(0, 0, 0),
                    width=2)
                s.append(irt)
                s.append(eval(a))
                a = a.replace('irt', 'cht')
                if abs(((0 - eval(a.replace('cht', 'irt'))) * 50 * o + 500) - ((0 - eval(a)) * o * 50 + 500)) < 100:
                    draw.line(
                        (irt * 50 * o + 500, (0 - eval(a.replace('cht', 'irt'))) * o * 50 + 500, cht * o * 50 + 500,
                         (0 - eval(a)) * 50 * o + 500),
                        fill=(0, 0, 0),
                        width=2)


            except Exception as e:
                pass
        if o == 1:
            cur.execute(f"""insert into fpqt(function, points) values('{k}', '{s}')""")
            con.commit()
            con.close()
        im.save('gr.jpg')
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
                s.append(irt)
                s.append(eval(a))
                a = a.replace('irt', 'cht')
                # if abs(((0 - eval(a.replace('cht', 'gt'))) * 50 * o + 500) - ((0 - eval(a.replace('cht', 'cy'))) * o * 50 + 500)) < 100:
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

        im.save('gr.jpg')


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gr.ui', self)  # Загружаем дизайн

        self.tabWidget.setTabText(2, 'ШАБЛОН')
        self.tabWidget.setTabText(0, 'Построение графика по функции')
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

    def y(self):
        self.ff = DataBase()
        self.ff.show()


    def x(self):
        if self.comboBox.currentText() == 'Увеличить':
            self.k *= int(self.lineEdit_2.text())
        else:
            self.k /= int(self.lineEdit_2.text())
        gr(self.lineEdit.text(), self.k)
        self.label_12.setText(str(1 / self.k))
        self.label_13.setText(str(1 / self.k))

        self.pixmap = QPixmap('gr.jpg')
        self.image = self.label
        self.image.setPixmap(self.pixmap)





    def gra(self):
        gr(self.lineEdit.text(), 1)
        self.k = 1
        self.label_12.setText(str(1 / self.k))
        self.label_13.setText(str(1 / self.k))
        self.pixmap = QPixmap('gr.jpg')
        self.image = self.label
        self.image.setPixmap(self.pixmap)
        self.label_11.show()
        self.label_12.show()
        self.label_13.show()


class DataBase(QDialog):
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
            for i in range(1, self.b, 2):
                a += f'{i}) x = {self.r[i - 1]}\ty = {self.r[i]}\n'
            self.label_8.setText(a)
            self.label_6.hide()
            self.pushButton_2.hide()
            self.spinBox.hide()
            self.a = True

    def ok1(self):
        if self.comboBox.currentText() == 'Точки у которых у Х n знаков после запятой':
            self.label_8.setText('Точки у которых у Х n знаков после запятой')
        elif self.comboBox.currentText() == 'Точки у кторых у Y n знаков после запятой':
            self.label_8.setText('Точки у кторых у Y n знаков после запятой')
        else:
            self.label_8.setText('qq')

    def right(self):
        self.b += 50
        a = ''
        for i in range(self.b - 49, self.b, 2):
            a += f'{i}) x = {self.r[i - 1]}\ty = {self.r[i]}\n'
        self.label_8.setText(a)

    def left(self):
        if self.b == 50:
            pass
        else:
            self.b -= 50
            a = ''
            for i in range(self.b - 49, self.b, 2):
                a += f'{i}) x = {self.r[i - 1]}\ty = {self.r[i]}\n'
            self.label_8.setText(a)



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
