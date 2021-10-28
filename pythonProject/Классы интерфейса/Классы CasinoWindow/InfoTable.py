from PairTable import PairTable
import Fonts


class InfoTable(PairTable):
    def __init__(self, parent):
        texts = ["наибольший выигрыш", "наибольшая ставка", "общий выигрыш", "наибольший баланс"]
        super().__init__(texts, parent, gaps_x=270, gaps_y=75, line_width=100,
                         line_height=30, label_font=Fonts.profont_24, line_font=Fonts.apex_24)
        self.setEnable(False)

    def update(self, key, value):
        self[key][1].setText(str(value))

    def clear(self):
        self.set_default_values("0")
