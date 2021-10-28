from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtCore import Qt, QTimer
from PyQt5 import QtCore

from CenteredWindow import CenteredWindow
from ScreenSize import SCREENSIZE
import Fonts

from random import randint, choice

TIME_COEFFICIENT = 1.08
CHANGE_TIME_LIMIT = 300
START_TIME_INTERVAL = 60


# этот класс реализует поле со сменяющимися значениями и рамку вокруг него. Этот класс
# самодостаточный и не очень большой, поэтому для него нет отдельного Responder.
class ClassicRoulette:
    def __init__(self, game, parent, width=0, height=0):
        self.game = game
        self.parent = parent
        self.value_label = RouletteValue(self.parent, width, height)
        self.frame_label = RouletteFrame(self.parent, width, height)
        self.set_timer()

    def set_timer(self):
        self.timer = QTimer(self.parent)
        self.timer.setInterval(START_TIME_INTERVAL)
        self.timer.timeout.connect(self.spin)

    def move(self, *args):
        self.value_label.move(*args)
        self.frame_label.move(*args)

    def resize(self, *args):
        self.value_label.resize(*args)
        self.frame_label.resize(*args)

    def spin(self):
        if self.timer.interval() < CHANGE_TIME_LIMIT:
            self.timer.setInterval(int(self.timer.interval() * TIME_COEFFICIENT))
            self.timer.start()

            self.set_random_value()
        else:
            self.timer.stop()
            self.timer.setInterval(START_TIME_INTERVAL)
            self.spin_end()

    def spin_end(self):
        self.game.spin_end()

    def set_random_value(self):
        self.value_label.set_random_value()

    def get_value(self):
        return self.value_label.get_value()

    def get_color(self):
        return self.value_label.get_color()

    def setEnable(self, value):
        self.value_label.setEnabled(value)
        self.frame_label.setEnabled(value)

    def setVisible(self, value):
        self.value_label.setVisible(value)
        self.frame_label.setVisible(value)


# данный класс реализует лэйбл с числом, которое может меняться
class RouletteValue(QLabel):
    def __init__(self, parent, width=0, height=0):
        super().__init__(parent)
        self.resize(width, height)
        self.set_random_value()
        self.setAlignment(Qt.AlignCenter)
        self.setFont(Fonts.wonder_36)

    def set_random_value(self):
        value = randint(1, 36)
        colors = ["rgb(235, 195, 80)", *(["rgb(206, 55, 201)"] * 18), *(["rgb(138, 43, 226)"] * 18)]
        # я почти уверен, что это костыльный метод, зато интуитивно понятный.
        color = choice(colors)
        self.color = {"rgb(235, 195, 80)": "золотой", "rgb(206, 55, 201)": "розовый",
                      "rgb(138, 43, 226)": "фиолетовый"}[color]
        self.setText(str(value))
        self.setStyleSheet(
            f"background: {color}; border: 2px solid black; color: black; font-size: "
            "120px; "
            "border-radius: 30px")

    def get_value(self):
        return self.text()

    def get_color(self):
        return self.color


# просто класс рамочки. Возможно (даже вероятно), не стоит выносить в отдельный класс,
# но мое внутреннее чувство подсказало сделать так. Во всяком случае, это, кажется, не делает код
# сильно хуже. Просто класс с рамочкой, которую можно делать задаваемого размера при
# инициализации. При желании можно добавить метод resize, но мне он не показался нужным.
class RouletteFrame(QLabel):
    def __init__(self, parent, width=0, height=0):
        super().__init__(parent)
        self.pixmap = QPixmap("всякая всячина/картинки/рамка.png")
        self.pixmap = self.pixmap.scaled(width, height,
                                         QtCore.Qt.IgnoreAspectRatio,
                                         QtCore.Qt.SmoothTransformation)
        self.setPixmap(self.pixmap)
        self.resize(width, height)
