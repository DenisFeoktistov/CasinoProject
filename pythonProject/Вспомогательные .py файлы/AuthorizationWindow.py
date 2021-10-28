from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QTimer
from PyQt5 import QtCore

from TemplateSmallWindow import TemplateSmallWindow
import Fonts


# при написании заметил, что у окон логина и регистрации очень много общего: заголовок,
# лейблы "логин" и "пароль", а также соответствующие поля ввода, поэтому сделал такой класс,
# который эти свойства объединит. Можно было добавить и две кнопки снизу, которые есть в обоих
# окнах, но я подумал, что их идеологически лучше делать в соответствующих классах, так как даже
# сам не был уверен, что их стоит делать одинаковыми, т.е. это скорее совпадение, что я захотел
# сделать их похожими, а не правило, а вот, например, поля логин и пароль по смыслу привязаны к
# классу окна авторизации.
class AuthorizationWindow(TemplateSmallWindow):
    def __init__(self, main_interface_class, main_label_text):
        super().__init__()
        self.main_label_text = main_label_text
        AuthorizationWindow.initUI(self)
        self.main_interface_class = main_interface_class

    def initUI(self):
        AuthorizationWindow.create_interface(self)

    def create_interface(self):
        self.label = QLabel(self.main_label_text, self)
        self.label.setFont(Fonts.facon_36)
        self.label.resize(self.width(), 70)
        self.label.move(0, 200)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("color: rgb(205, 205, 0)")

        self.login_label = QLabel("Логин", self)
        self.login_label.move(70, 340)
        self.login_label.setFont(Fonts.intro_24)
        self.login_label.adjustSize()
        self.login_label.setStyleSheet("color: rgb(0, 0, 0)")

        self.login_line = QLineEdit("", self)
        self.login_line.move(190, 337)
        self.login_line.resize(230, 25)
        self.login_line.setStyleSheet("font-size: 15px")

        self.password_label = QLabel("Пароль", self)
        self.password_label.move(70, 390)
        self.password_label.setFont(Fonts.intro_24)
        self.password_label.adjustSize()
        self.password_label.setStyleSheet("color: rgb(0, 0, 0)")

        self.password_line = QLineEdit("", self)
        self.password_line.move(190, 387)
        self.password_line.resize(230, 25)
        self.password_line.setStyleSheet("font-size: 15px")

    def clear(self):
        self.password_line.setText(
            "")  # так как я не создаю каждый раз новое окно авторизации, то необходимо очищать
        # это, чтобы при новом открытии не отображалась старая информация
        self.login_line.setText("")
