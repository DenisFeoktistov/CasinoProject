from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
from PyQt5 import QtCore

from AuthorizationWindow import AuthorizationWindow
import Fonts


class LoginWindow(AuthorizationWindow):
    def __init__(self, main_interface_class):
        super().__init__(main_interface_class, main_label_text="Войти в систему")
        self.create_interface()

    def close(self):
        self.clear()
        super().close()

    def show(self):
        super().show()
        self.clear()

    def create_interface(self):
        self.login_btn = QPushButton("Войти", self)
        self.login_btn.setFont(Fonts.apex_24)
        self.login_btn.setStyleSheet(
            "font-size: 16px; color: rgb(170, 170, 170); border-style: outset; border-width: 2px; "
            "border-radius: 10px; border-color: beige; min-width: 10em; padding: 6px;")
        self.login_btn.adjustSize()
        self.login_btn.move((self.width() - self.login_btn.width()) / 2, self.height() - 150)

        self.registration_btn = QPushButton("Зарегистрироваться", self)
        self.registration_btn.setFont(Fonts.apex_24)
        self.registration_btn.setStyleSheet(
            "font-size: 16px; color: rgb(170, 170, 170); border-style: outset; border-width: 2px; "
            "border-radius: 10px; border-color: beige; min-width: 10em; padding: 6px;")
        self.registration_btn.adjustSize()
        self.registration_btn.move((self.width() - self.registration_btn.width()) / 2,
                                   self.height() - 90)

    def set_responder(self, responder):
        self.responder = responder

        self.login_btn.clicked.connect(self.responder.login)
        self.registration_btn.clicked.connect(self.responder.registration)

    def get_login_text(self):
        return self.login_line.text()

    def get_password_text(self):
        return self.password_line.text()
