import sys
from math import *
from PIL import Image, ImageDraw

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTabWidget, QLabel
from PyQt5.QtGui import QPixmap

def gr(a):
    im = Image.new("RGB", (1000, 1000), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    draw.line((500, 0, 500, 1000), fill=(0, 0, 0), width=3)
    draw.line((0, 500, 1000, 500), fill=(0, 0, 0), width=3)
    for i in range(0, 1001, 50):
        draw.line((i, 505, i, 495), fill=(0, 0, 0), width=3)
        draw.line((495, i, 505, i), fill=(0, 0, 0), width=3)
    cht = ''
    for irt in range(-10000, 10000):
        a = a.replace('x', 'irt')

        try:
            a = a.replace('cht', 'irt')

            irt /= 1000
            cht = irt - (1 / 1000)
            draw.line((irt * 50 + 500, (0 - eval(a)) * 50 + 500, irt * 50 + 500, (0 - eval(a)) * 50 + 500),
                      fill=(0, 0, 0),
                      width=2)
            a = a.replace('irt', 'cht')
            if abs(((0 - eval(a.replace('cht', 'irt'))) * 50 + 500) - ((0 - eval(a)) * 50 + 500)) < 100:
                draw.line(
                    (irt * 50 + 500, (0 - eval(a.replace('cht', 'irt'))) * 50 + 500, cht * 50 + 500,
                     (0 - eval(a)) * 50 + 500),
                    fill=(0, 0, 0),
                    width=2)

        except Exception as e:
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



    def gra(self):
        gr(self.lineEdit.text())
        self.pixmap = QPixmap('gr.jpg')
        self.image = self.label
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())