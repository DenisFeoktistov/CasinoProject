from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore

from CenteredWindow import CenteredWindow
from RouletteGame import RouletteGame
from ScreenSize import SCREENSIZE
from InfoTable import InfoTable
from DiceGame import DiceGame
import Fonts


class CasinoWindow(CenteredWindow):
    def __init__(self, main_interface_class):
        super().__init__(SCREENSIZE.width(), SCREENSIZE.height())
        self.initUI()
        self.main_interface_class = main_interface_class
        self.set_timer()

    def show(self):
        super().show()  # на всякий случай, окно очищается после каждого закрытия и перед каждым
        # открытием
        self.clear()
        self.responder.show_preprocess()  # этот метод запускает первичную обработку информации,
        # например, необходимо обновить баланс, данные в табличке

    def close(self):
        self.clear()
        super().close()

    def initUI(self):
        self.tune_window()
        self.add_pictures()
        self.create_interface()
        self.create_roulette_game()
        self.create_dice_game()
        self.create_info_table()

    def tune_window(self):
        self.back_pixmap = QPixmap("всякая всячина/картинки/фон казино.jpg")
        self.back_pixmap = self.back_pixmap.scaled(self.width(), self.height(),
                                                   QtCore.Qt.IgnoreAspectRatio,
                                                   QtCore.Qt.SmoothTransformation)
        self.back_label = QLabel(self)
        self.back_label.setPixmap(self.back_pixmap)
        self.back_label.adjustSize()

    def add_pictures(self):
        # Добавление других картинок
        self.carts_pixmap = QPixmap("всякая всячина/картинки/карты.png")
        self.carts_pixmap = self.carts_pixmap.scaled(self.width() / 5, self.height(),
                                                     QtCore.Qt.IgnoreAspectRatio,
                                                     QtCore.Qt.SmoothTransformation)
        self.carts_label = QLabel(self)
        self.carts_label.move(self.width() - 250, self.height() / 2)
        self.carts_label.setPixmap(self.carts_pixmap)
        self.carts_label.adjustSize()

        self.money_pixmap = QPixmap("всякая всячина/картинки/мешок.png")
        self.money_pixmap = self.money_pixmap.scaled(100, 100,
                                                     QtCore.Qt.KeepAspectRatio,
                                                     QtCore.Qt.SmoothTransformation)
        self.money_label = QLabel(self)
        self.money_label.move(100, self.height() - 95)
        self.money_label.setPixmap(self.money_pixmap)
        self.money_label.adjustSize()

    def create_interface(self):
        self.balance_label = QLabel("Баланс:", self)
        self.balance_label.setFont(Fonts.apex_24)
        self.balance_label.setStyleSheet("font-size: 19px; color: rgb(170, 170, 170)")
        self.balance_label.move(self.width() - 210, 10)

        self.balance_line = QLabel("777777 R", self)
        self.balance_line.setFont(Fonts.apex_24)
        self.balance_line.setGeometry(self.width() - 140, 7, 130, 30)
        self.balance_line.setAlignment(Qt.AlignCenter)
        self.balance_line.setStyleSheet("font-size: 40px; color: rgb(100, 250, 100)")
        self.balance_line.adjustSize()

        self.get_money_btn = QPushButton("Получить валюту", self)
        self.get_money_btn.setFont(Fonts.apex_24)
        self.get_money_btn.move(230, 7)
        self.get_money_btn.setStyleSheet(
            "font-size: 16px; color: rgb(170, 170, 170); border-style: outset; border-width: 2px; "
            "border-radius: 10px; border-color: beige; min-width: 10em; padding: 6px;")
        self.get_money_btn.adjustSize()

        self.logout_btn = QPushButton("Выйти из аккаунта", self)
        self.logout_btn.setFont(Fonts.apex_24)
        self.logout_btn.move(30, 7)
        self.logout_btn.setStyleSheet(
            "font-size: 16px; color: rgb(170, 170, 170); border-style: outset; border-width: 2px; "
            "border-radius: 10px; border-color: beige; min-width: 10em; padding: 6px;")
        self.logout_btn.adjustSize()

        self.change_mode = QLabel("Сменить режим", self)
        self.change_mode.setFont(Fonts.apex_24)
        self.change_mode.setStyleSheet("font-size: 19px; color: rgb(170, 170, 170);")
        self.change_mode.adjustSize()
        self.change_mode.move((self.width() - self.change_mode.width()) / 2, self.height() - 50)

        self.next_mode_btn = QPushButton(">>", self)
        self.next_mode_btn.setFont(Fonts.apex_24)
        self.next_mode_btn.setStyleSheet(
            "font-size: 20px; color: rgb(170, 170, 170); border-style: outset; border-width: 2px; "
            "border-radius: 10px; border-color: beige; min-width: 3em; padding: 3px;")
        self.next_mode_btn.adjustSize()
        self.next_mode_btn.move((self.width() - self.next_mode_btn.width()) / 2 + 120,
                                self.height() - 55)

        self.previous_mode_btn = QPushButton("<<", self)
        self.previous_mode_btn.setFont(Fonts.apex_24)
        self.previous_mode_btn.setStyleSheet(
            "font-size: 20px; color: rgb(170, 170, 170); border-style: outset; border-width: 2px; "
            "border-radius: 10px; border-color: beige; min-width: 3em; padding: 3px;")
        self.previous_mode_btn.adjustSize()
        self.previous_mode_btn.move((self.width() - self.previous_mode_btn.width()) / 2 - 120,
                                    self.height() - 55)

        self.messege_box = QPushButton("Это эррор братка это эррор", self)
        self.messege_box.setFont(Fonts.sports_24)
        self.messege_box.setStyleSheet(
            "font-size: 20px; color: rgb(250, 0, 0); border-style: solid; border-width: 2px; "
            "border-radius: 10px; border-color: rgb(250, 0, 0); min-width: 30em; padding: 6px;")
        self.messege_box.adjustSize()
        self.messege_box.move((self.width() - self.messege_box.width()) / 2 + 110, 7)
        self.messege_box.setEnabled(True)
        self.messege_box.setVisible(False)


    def set_responder(self, responder):
        self.responder = responder

        self.next_mode_btn.clicked.connect(self.responder.open_next_mode)
        self.previous_mode_btn.clicked.connect(self.responder.open_previous_mode)
        self.get_money_btn.clicked.connect(self.responder.give_daily_money)
        self.logout_btn.clicked.connect(self.responder.logout)

        self.dice_game.set_responder(responder.dice_game_responder)
        self.roulette_game.set_responder(responder.roulette_game_responder)

    def set_timer(self):
        self.timer = QTimer(self)
        self.timer.setInterval(2500)  # здесь сообщения поинформативнее, поэтому висят не 1,5,
        # а 2,5 секунды
        self.timer.timeout.connect(self.clear_message)

    def set_success(self, text):
        self.messege_box.setStyleSheet(
            "font-size: 20px; color: rgb(0, 250, 0); border-style: solid; border-width: 2px; "
            "border-radius: 10px; border-color: rgb(0, 250, 0); min-width: 30em; padding: 6px;")
        self.messege_box.setText(text)
        self.messege_box.setVisible(True)

        self.timer.start()

    def set_error(self, text):
        self.messege_box.setStyleSheet(
            "font-size: 20px; color: rgb(250, 0, 0); border-style: solid; border-width: 2px; "
            "border-radius: 10px; border-color: rgb(250, 0, 0); min-width: 30em; padding: 6px;")
        self.messege_box.setText(text)
        self.messege_box.setVisible(True)

        self.timer.start()

    def clear_message(self):
        self.messege_box.setText("")
        self.messege_box.setVisible(False)

    def update(self):
        self.update_balance()
        self.update_info()

    def update_balance(self):
        text = self.responder.get_balance()
        self.balance_line.setText(str(text))

    def update_info(self):
        self.responder.update_info()

    def create_roulette_game(self):
        self.roulette_game = RouletteGame(self)
        self.roulette_game.move(80, 120)
        self.roulette_game.setEnable(False)
        self.roulette_game.setVisible(False)

    def create_dice_game(self):
        self.dice_game = DiceGame(self)
        self.dice_game.move(90, 160)

    def create_info_table(self):
        self.info_table = InfoTable(self)
        self.info_table.move(self.width() - 400, 120)

    def open_roulette_game(self):
        self.roulette_game.setEnable(True)
        self.roulette_game.setVisible(True)

    def open_dice_game(self):
        self.dice_game.setVisible(True)
        self.dice_game.setEnable(True)

    def close_roulette_game(self):
        self.roulette_game.setEnable(False)
        self.roulette_game.setVisible(False)

    def close_dice_game(self):
        self.dice_game.setVisible(False)
        self.dice_game.setEnable(False)

    def clear(self):
        self.dice_game.clear()
        self.roulette_game.clear()
        self.info_table.clear()
        self.balance_line.setText("0")
