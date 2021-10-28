from PyQt5.QtWidgets import QPushButton, QLabel, QSlider, QLineEdit
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore

import Fonts


# класс, который реализует вторую игру. Содержит слайдер, кнопку запуска, поле для ставки,
# поле с овозможным выигрышем, а также некоторые лейблы
class DiceGame:
    def __init__(self, parent):
        self.parent = parent
        self.initUI()
        self.set_slider_values()
        self.move(0, 0)

    def initUI(self):
        self.slider = QSlider(Qt.Horizontal, self.parent)

        self.slider.resize(800, 60)
        self.slider.setStyleSheet("""
                    QSlider::groove:horizontal {  
                        height: 16px;
                        margin: 0px;
                        border: 3px solid black;
                        border-radius: 5px;
                        background: rgb(206, 55, 201);
                    }
                    QSlider::handle:horizontal {
                        background: rgb(235, 195, 80);
                        border: 1px solid rgb(70, 70, 70);
                        width: 27px;
                        margin: -7px 0; 
                        border-radius: 14px;
                    }
                    QSlider::sub-page:horizontal {
                        background: rgb(138, 43, 226);
                        border: 3px solid black;
                        border-radius: 5px;
                    }
                """)

        self.zero_label = QLabel("1%", self.parent)
        self.zero_label.setFont(Fonts.profont_36)
        self.zero_label.adjustSize()
        self.zero_label.setStyleSheet("color: rgb(206, 55, 201)")

        self.hundred_label = QLabel("99%", self.parent)
        self.hundred_label.setFont(Fonts.profont_36)
        self.hundred_label.adjustSize()
        self.hundred_label.setStyleSheet("color: rgb(138, 43, 226)")

        self.run_btn = QPushButton("Запустить", self.parent)
        self.run_btn.resize(400, 70)
        self.run_btn.setFont(Fonts.profont_36)
        self.run_btn.setStyleSheet(
            "background: rgb(235, 195, 80); border: 3px solid rgb(175, 155, 40); border-radius: "
            "10px; font-size: 50px;")

        self.bet_label = QLabel("Ставка", self.parent)
        self.bet_label.setFont(Fonts.profont_36)
        self.bet_label.adjustSize()

        self.bet_line = QLineEdit("0", self.parent)
        self.bet_line.setFont(Fonts.apex_24)
        self.bet_line.resize(130, 35)
        self.bet_line.setStyleSheet(":disabled { color: rgb(70, 70, 70)}")

        self.possible_gain_label = QLabel("Возможный выигрыш", self.parent)
        self.possible_gain_label.setFont(Fonts.profont_36)
        self.possible_gain_label.adjustSize()

        self.possible_gain_line = QLineEdit("0", self.parent)
        self.possible_gain_line.setFont(Fonts.apex_24)
        self.possible_gain_line.resize(130, 35)
        self.possible_gain_line.setEnabled(False)
        self.possible_gain_line.setStyleSheet(":disabled { color: rgb(70, 70, 70)}")

    def set_slider_values(self):
        self.slider.setMinimum(1)
        self.slider.setMaximum(99)
        self.slider.setValue(50)

    def move(self, x, y):
        # здесь метод move отвечает не только за перемещение, но и за корректное
        # взаиморасположение виджетов. Вероятно, это не очень хорошо, но как мне кажется,
        # в данном случае понятно, так как взаимное расположение задано просто добавлением пикселей
        self.slider.move(10 + x, 40 + y)
        self.zero_label.move(90, 160)
        self.hundred_label.move(780 + x, y)
        self.run_btn.move(210 + x, 140 + y)
        self.bet_label.move(270 + x, 290 + y)
        self.bet_line.move(420 + x, 290 + y)
        self.possible_gain_label.move(155 + x, 390 + y)
        self.possible_gain_line.move(540 + x, 390 + y)

    def set_responder(self, responder):
        self.responder = responder

        self.run_btn.clicked.connect(self.responder.run)
        self.bet_line.textChanged.connect(self.responder.text_changed)
        self.slider.valueChanged.connect(self.responder.slider_value_changed)

    def get_bet(self):
        return self.bet_line.text()

    def get_value(self):
        return self.slider.value()

    def set_possible_gain(self, possible_gain):
        self.possible_gain_line.setText(str(possible_gain))

    def get_possible_gain(self):
        return self.possible_gain_line.text()

    def clear(self):
        self.bet_line.setText("0")
        self.possible_gain_line.setText("0")
        self.slider.setValue(50)

    def setEnable(self, value):
        self.slider.setEnabled(value)
        self.zero_label.setEnabled(value)
        self.hundred_label.setEnabled(value)
        self.run_btn.setEnabled(value)
        self.bet_label.setEnabled(value)
        self.bet_line.setEnabled(value)
        self.possible_gain_label.setEnabled(value)

    def setVisible(self, value):
        self.slider.setVisible(value)
        self.zero_label.setVisible(value)
        self.hundred_label.setVisible(value)
        self.run_btn.setVisible(value)
        self.bet_label.setVisible(value)
        self.bet_line.setVisible(value)
        self.possible_gain_label.setVisible(value)
        self.possible_gain_line.setVisible(value)
