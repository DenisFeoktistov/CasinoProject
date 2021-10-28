from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtCore import Qt, QTimer
from PyQt5 import QtCore

from CenteredWindow import CenteredWindow
from ScreenSize import SCREENSIZE
import Fonts


# очень вероятно, что костыль, но, тем не менее, оправданный класс. Часто приходится встречаться с
# таблицами формата "Label - Line", поэтому сделал такой класс для реализации такой таблички. Он
# используется, например, для вывода информации об успехах данного пользователся.
class PairTable:
    def __init__(self, texts, parent, gaps_x=270, gaps_y=75, line_width=100,
                 line_height=30, label_font=Fonts.profont_36, line_font=Fonts.apex_24):
        self.gaps_x = gaps_x
        self.gaps_y = gaps_y

        self.texts = dict(
            [(text, (QLabel(text, parent), QLineEdit(parent))) for text in texts])

        self.set_style(label_font, line_font, line_height, line_width, texts)

        self.coords = 0, 0
        self.set_correct_positions()

    def set_style(self, label_font, line_font, line_height, line_width, texts):
        for index, key in enumerate(texts):
            self[key][0].setFont(label_font)
            self[key][0].adjustSize()
            self[key][1].setFont(line_font)
            self[key][1].setFixedWidth(line_width)
            self[key][1].setFixedHeight(line_height)
            self[key][1].setStyleSheet(":disabled { color: rgb(70, 70, 70)}")

    def set_correct_positions(self):  # этод метод просто задает корректное расположение класса
        for index, key in enumerate(self.texts):
            self[key][0].move(self.coords[0], self.coords[1] + index * self.gaps_y)
            self[key][1].move(self.coords[0] + self.gaps_x, self.coords[1] + index * self.gaps_y)

    def move(self, x, y):
        self.coords = (x, y)

        self.set_correct_positions()  # поменяли координаты, теперь зададим положение

    def resize(self, gaps_x, gaps_y):
        self.gaps_x = gaps_x
        self.gaps_y = gaps_y

        self.set_correct_position()  # поменяли размер, теперь зададим расположение

    def setEnable(self, value):
        for key in self.texts.keys():
            self[key][1].setEnabled(value)  # выключить взаимодействие достаточно у строк ввода

    def setVisible(self, value):
        for key in self.keys():
            self[key][0].setVisible(value)
            self[key][1].setVisible(value)

    def __getitem__(self, key):
        return self.texts[key]  # такой getitem возвращает кортеж из QLabel и соответствующего
        # QLineEdit

    def keys(self):
        return self.texts.keys()

    def set_default_values(self, value):
        for key in self.keys():
            self[key][1].setText(value)
