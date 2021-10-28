from random import randint


class DiceGameResponder:
    def __init__(self, main_responder):
        self.main_responder = main_responder

    def set_interface(self, interface):
        self.interface = interface

    def text_changed(self):
        self.update_possible_gain()

    def slider_value_changed(self):
        self.update_possible_gain()

    def run(self):
        try:
            self.check_bet()
            self.check_balance()
            result = randint(1, 100)
            bet = int(self.interface.get_bet())
            value = int(self.interface.get_value())
            possible_gain = int(self.interface.get_possible_gain())
            self.main_responder.check_max_bet(bet)
            if value >= result:
                self.main_responder.check_max_gain(possible_gain)
                self.main_responder.check_max_balance()
                self.main_responder.add_money(possible_gain)
                self.main_responder.add_total_gain(possible_gain)
                self.main_responder.update_info()
            else:
                self.main_responder.add_money(-bet)
                self.main_responder.update_info()
        except Exception as e:
            self.main_responder.set_error(str(e))

    def update_possible_gain(self):
        try:
            self.check_bet()
            bet = int(self.interface.get_bet())
            value = self.interface.get_value()
            possible_gain = int(bet * ((100 - value) / value))
            self.interface.set_possible_gain(possible_gain)
        except Exception as e:
            self.interface.set_possible_gain("0")
            # self.main_responder.set_error(str(e)) вообще хорошо бы оставить, но мешает,
            # когда хочешь поменять ставку, стираешь старую, а вылезает ошибка, поэтому пусть
            # будет нейтральная обработка такого случая

    def check_bet(self):
        bet = self.interface.get_bet()
        if not bet.isdigit() or bet == "":
            raise Exception("Некорректная ставка")

    def check_balance(self):
        bet = self.interface.get_bet()
        if int(bet) > self.main_responder.get_balance():
            raise Exception("Недостаточно средств")
