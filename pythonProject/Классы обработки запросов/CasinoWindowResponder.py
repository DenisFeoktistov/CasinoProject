from datetime import datetime

from RouletteGameResponder import RouletteGameResponder
from DiceGameResponder import DiceGameResponder


class CasinoWindowResponder:
    def __init__(self, main_responder):
        self.main_responder = main_responder
        self.roulette_game_responder = RouletteGameResponder(self)
        self.dice_game_responder = DiceGameResponder(self)

    def set_actual_user(self, id):
        self.actual_user_id = id  # этот метод вызывается из LoginWindowResponder или
        # RegistrationWindowResponder, я не уверен, что это хорошо, но идею по исправлению не
        # придумал. Была мысль обновлять, например, поле в базе данных, а в этом классе его
        # брать, но создавать табличку для одного значения...

    def show_preprocess(self):
        self.update_info()

        self.mode = 0  # пусть по умолчанию открывается рулетка, как самая классическая игра
        self.open_game_mode()

    def open_game_mode(self):
        self.modes[self.mode]()
        for index, func in enumerate(self.close_modes):
            if index != self.mode:
                func()

    def open_next_mode(self):
        self.mode = (self.mode + 1) % len(self.modes)
        self.open_game_mode()

    def open_previous_mode(self):
        self.mode = (self.mode - 1) % len(self.modes)
        self.open_game_mode()

    def set_info(self, info):
        self.info = info

    def set_interface(self, interface):
        self.interface = interface

        self.roulette_game_responder.set_interface(self.interface.roulette_game)
        self.dice_game_responder.set_interface(self.interface.dice_game)
        self.modes = [self.interface.open_roulette_game, self.interface.open_dice_game]
        self.close_modes = [self.interface.close_roulette_game, self.interface.close_dice_game]

    def set_error(self, text):
        self.interface.set_error(text)

    def set_success(self, text):
        self.interface.set_success(text)

    def give_daily_money(self):  # этот метод отвечает только за добавления эжедневного бонуса
        last_date = self.info.get_last_date(self.actual_user_id)
        today = str(datetime.today().date())
        if last_date == today:
            self.set_error("Вы уже забрали сегодняшний бонус")
        else:
            total_days = self.info.get_total_days(self.actual_user_id)
            money = 300
            extra_money = 50 * total_days
            money += extra_money
            self.add_money(money)
            self.info.update_last_date(self.actual_user_id)
            self.info.update_total_days(self.actual_user_id)

    def add_money(self, money):
        self.info.add_money(self.actual_user_id, money)
        self.check_max_balance()  # вдруг данный баланс стал максимальный? давайте его обновим
        self.update_info()  # информацию тоже надо обновлять
        if money > 0:
            self.set_success(f"На баланс успешно зачислено {money}")
        elif money == 0:
            self.set_success(f"Ваши ставки сыграли нейтрально")
        else:
            self.set_error(f"Вы проиграли {money}")

    def add_total_gain(self, money):
        if money > 0:
            self.info.add_total_gain(self.actual_user_id, money)

    def check_max_bet(self, max_bet):
        previous = self.info.get_max_bet(self.actual_user_id)
        if previous < max_bet:
            self.info.set_max_bet(self.actual_user_id, max_bet)

    def check_max_gain(self, max_gain):
        previous = self.info.get_max_gain(self.actual_user_id)
        if previous < max_gain:
            self.info.set_max_gain(self.actual_user_id, max_gain)

    def check_max_balance(self):
        if self.info.get_balance(self.actual_user_id) > self.info.get_max_balance(
                self.actual_user_id):
            self.info.set_max_balance(self.actual_user_id,
                                      self.info.get_balance(self.actual_user_id))

    def update_info(self):
        self.update_balance()
        self.update_table_info()

    def update_balance(self):
        self.interface.update_balance()

    def update_table_info(self):
        max_gain = self.info.get_max_gain(self.actual_user_id)
        max_bet = self.info.get_max_bet(self.actual_user_id)
        total_gain = self.info.get_total_gain(self.actual_user_id)
        max_balance = self.info.get_max_balance(self.actual_user_id)
        self.interface.info_table.update("наибольший выигрыш", max_gain)
        self.interface.info_table.update("наибольшая ставка", max_bet)
        self.interface.info_table.update("общий выигрыш", total_gain)
        self.interface.info_table.update("наибольший баланс", max_balance)

    def get_balance(self):
        return self.info.get_balance(self.actual_user_id)

    def logout(self):
        self.interface.main_interface_class.close_casino_window()
        self.interface.main_interface_class.show_login_window()
