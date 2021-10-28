class RouletteGameResponder:
    def __init__(self, main_responder):
        self.main_responder = main_responder

    def set_interface(self, interface):
        self.interface = interface

    def check_bets(self):
        # этот метод - своеобразный assert(), так как выбрасывает ошибку, а не обрабатывает ее
        table = self.interface.get_bets_table()
        sum = 0
        for key in table.keys():
            if not table[key][1].text().isdigit():
                raise Exception("Некорректная ставка")
            sum += int(table[key][1].text())
        if sum > self.main_responder.get_balance():
            raise Exception("Недостаточно средств для данной ставки")

    def spin_start(self):
        try:
            self.check_bets()
            self.interface.roulette.spin()
            self.interface.set_bets_enable(False)
        except Exception as e:
            self.main_responder.set_error(str(e))

    def spin_end(self):
        win_keys = self.get_win_keys()

        money_plus = self.count_plus(win_keys)
        max_bet = self.max_bet()

        self.main_responder.check_max_bet(
            max_bet)  # а вдруг обновили максимальну ставку?? передадим ее, пусть main_responder
        # ее обработает, info_table - его сфера деятельности. Далее по аналогии. Вычисляем
        # значение, которое могли изменить, а обрабатывает его пусть main_responder. На самом
        # деле, вот в этом моменте я не был уверен, но не придумал, как можно сделать его лучше.
        self.main_responder.check_max_gain(money_plus)

        self.main_responder.add_money(money_plus)
        self.main_responder.add_total_gain(money_plus)

        self.main_responder.check_max_balance()

        self.main_responder.update_info()  # здесь я тоже не уверен. Вообще, наверное,
        # стоит вызовать это метод при каждом изменении информации в классе CasinoResponder.

        self.interface.bets_table.setEnable(True)

    def get_win_keys(self):
        value = int(self.interface.get_value())
        color = self.interface.get_color()
        win_keys = list()
        if value < 18:
            win_keys.append(("меньше 18", 2))
        else:
            win_keys.append(("18 и больше", 2))
        if value % 2 == 0:
            win_keys.append(("четное(x2)", 2))
        else:
            win_keys.append(("нечетное(x2)", 2))
        if color == "фиолетовый":
            win_keys.append(("фиолетовое (x2)", 2))
        elif color == "розовый":
            win_keys.append(("розовое (x2)", 2))
        else:
            win_keys.append(("золотое (x50)", 50))
        return win_keys

    def count_plus(self, win_keys):
        total = 0
        for key in self.interface.get_keys():
            bet = int(self.interface.get_bets_table()[key][1].text())
            total -= bet

            flag = False
            coefficient = 0
            for win_key in win_keys:
                if key == win_key[0]:
                    flag = True
                    coefficient = win_key[1]
            if flag:
                total += bet * coefficient
        return total

    def max_bet(self):
        max_bet = 0
        for key in self.interface.get_keys():
            bet = int(self.interface.get_bets_table()[key][1].text())
            max_bet += bet
        return max_bet
