from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QTimer
from PyQt5 import QtCore

from CenteredWindow import CenteredWindow
import Fonts


# Этот класс создает маленькое окно, которое я использую, например, для создания окон входа в
# систему и регистрации. Изначально я думал, что буду его использовать еще для каких-то целей,
# но, хоть этого и не случилось, мне кажется, что это полезный класс, который может пригодиться
# при доработке. Например, какие-нибудь пользовательские соглашения или важные сообщения можно
# выводить в него.
class TemplateSmallWindow(CenteredWindow):
    def __init__(self):
        super().__init__(500, 600)
        TemplateSmallWindow.initUI(
            self)  # насколько я понял, когда речь заходит о наследовании, то лучше указывать
        # явно, метод какого класса мы используем, чтобы не возникло проблем. Предпологается,
        # что у этого класса будут наследники у которых, возможно, будет одноименный метод,
        # поэтому, чтобы не возникало путаницы и ошибок при вызове конструктора у дочернего
        # класса, я использую такой способ вызова. Впоследствии такой синаксис будет встречаться
        # и в других классах.
        self.set_error_timer()

    def set_error_timer(self):
        self.timer = QTimer(self)
        self.timer.setInterval(
            1500)  # на мой взгляд, полутора секунд хватает на прочтение ошибки, поэтому она не
        # висит долго, надоедая юзеру
        self.timer.timeout.connect(self.clear_error)

    def initUI(self):
        TemplateSmallWindow.tune_window(
            self)  # метод tune_window используется только для модификации конкретно окна,
        # т.е. добавление название и фона, ничего более
        TemplateSmallWindow.add_pictures(self)
        TemplateSmallWindow.create_interface(self)

    def tune_window(self):
        self.back_pixmap = QPixmap("всякая всячина/картинки/фон логин.jpeg")
        self.back_pixmap = self.back_pixmap.scaled(self.width() * 2, self.height(),
                                                   QtCore.Qt.IgnoreAspectRatio,
                                                   QtCore.Qt.SmoothTransformation)
        self.back_label = QLabel(self)
        self.back_label.setFixedSize(self.width(), self.height())
        self.back_label.setPixmap(self.back_pixmap)

    def add_pictures(self):
        self.casino_pixmap = QPixmap("всякая всячина/картинки/казино надпись.png")
        self.casino_pixmap = self.casino_pixmap.scaled(300, 150, QtCore.Qt.IgnoreAspectRatio,
                                                       QtCore.Qt.SmoothTransformation)
        self.casino_label = QLabel(self)
        self.casino_label.setPixmap(self.casino_pixmap)
        self.casino_label.adjustSize()
        self.casino_label.move(self.width() / 2 - 150, 20)

    def create_interface(self):
        self.error_box = QPushButton("", self)
        self.error_box.setFont(Fonts.sports_12)
        self.error_box.setStyleSheet(
            "font-size: 16px; color: rgb(250, 0, 0); border-style: solid; border-width: 2px; "
            "border-radius: 10px; border-color: rgb(250, 0, 0); min-width: 22em; padding: 6px;")
        self.error_box.adjustSize()
        self.error_box.move((self.width() - self.error_box.width()) / 2, 275)
        self.error_box.setEnabled(True)
        self.error_box.setVisible(False)

    def set_error(self, text):
        self.timer.start()
        self.error_box.setText(text)
        self.error_box.setVisible(True)

    def clear_error(self):
        self.error_box.setText("")
        self.error_box.setVisible(False)
        self.timer.stop()
