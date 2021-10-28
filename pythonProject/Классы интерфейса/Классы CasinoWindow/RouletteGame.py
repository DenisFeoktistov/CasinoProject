from PyQt5.QtWidgets import QPushButton

from ClassicRoulette import ClassicRoulette
from PairTable import PairTable
import Fonts


# это класс, который объединяет рулетку, реализованную в классе ClassicRoulette, кнопку запуска и
# таблицу ставок. Нужная вещь, как мне кажется, так как возникает необходимость работаь с этими
# виджетами как с группой (например, когда нужно поменять режим).
class RouletteGame:
    def __init__(self, parent):
        self.roulette = ClassicRoulette(self,
                                        parent, width=300, height=300)
        self.bets_table = PairTable(
            ["фиолетовое (x2)", "розовое (x2)", "золотое (x50)", "четное(x2)", "нечетное(x2)",
             "меньше 18", "18 и больше"],
            parent)  # тот самый случай, когда пригодилась табличка PairTable. Может также
        # возникнуть вопрос, почему у зотого коэффициент 50, когда шанс его выпадения 1/37. На
        # него не существует ответа :) Просто круглое число.
        self.bets_table.set_default_values("0")

        self.spin_btn = QPushButton("Крутить", parent)
        self.spin_btn.setFont(Fonts.profont_12)
        self.spin_btn.setStyleSheet(
            "background: rgb(235, 195, 80); border: 3px solid rgb(175, 155, 40); border-radius: "
            "10px; font-size: 50px;")
        self.spin_btn.setFixedSize(300, 70)

        self.move(0, 0)

    def move(self, x, y):
        # опять таки, этот move отвечает и за взаимное расположение, но мне кажется, что в данном
        # случае правило простое, поэтому можно оставить и так
        self.roulette.move(x, y)
        self.bets_table.move(x + 370, y)
        self.spin_btn.move(x, y + 400)

    def set_responder(self, responder):
        self.responder = responder

        # У этого класса уже есть обработчик. Привязывать события ко кнопкам лучше во время его
        # привязывания к классу.
        self.spin_btn.clicked.connect(self.responder.spin_start)

    def spin_end(self):
        self.responder.spin_end()

    def get_bets_table(self):
        return self.bets_table

    def get_keys(self):
        return self.bets_table.keys()

    def get_bets(self):
        return dict(map(lambda key: (key, self.bets_table[key][1].text()), self.bets_table.keys()))

    def get_value(self):
        return self.roulette.get_value()

    def get_color(self):
        return self.roulette.get_color()

    def clear(self):
        self.bets_table.set_default_values("0")

    def set_bets_enable(self, value):
        self.bets_table.setEnable(value)

    def setEnable(self, value):
        self.roulette.setEnable(value)
        self.bets_table.setEnable(value)
        self.spin_btn.setEnabled(value)

    def setVisible(self, value):
        self.roulette.setVisible(value)
        self.bets_table.setVisible(value)
        self.spin_btn.setVisible(value)
