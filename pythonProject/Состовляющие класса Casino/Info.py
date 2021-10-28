import sqlite3
from datetime import datetime


class CasinoInfo:
    def __init__(self):
        self.db_name = "casino_db.db"
        self.con = sqlite3.connect(self.db_name)

    def check_user_existence(self, login, password):
        cur = self.con.cursor()

        result = cur.execute("""SELECT id FROM users WHERE login=? AND password=?""",
                             (login, password)).fetchall()

        return bool(result)

    def check_login_existence(self, login):
        cur = self.con.cursor()

        result = cur.execute("""SELECT id FROM users WHERE login=?""", (login,)).fetchall()

        return bool(result)

    def add_user(self, login, password):
        cur = self.con.cursor()

        cur.execute("""INSERT INTO users(login, password) VALUES(?, ?)""",
                    (login, password))
        self.con.commit()

    # --------- дальше методы, которые нужны для работы с CasinoWindow ----------------------------
    # Здесь я сделал много однообразных методов, но я так поступил не просто так. Я думаю,
    # что лучше, когда только Info несет ответственность за поля БД, т.е. не стоит добавлять поля
    # в вызовы методов из других классов, пусть это и приведет к такой вот однообразности.

    def set_parameter(self, actual_user_id, parameter,
                      new_value):  # первые два метода универсальные, основные, далее однообразные
        cur = self.con.cursor()

        cur.execute(f"""UPDATE users SET {parameter} = ? WHERE id=?""",
                    (new_value, actual_user_id))
        self.con.commit()

    def get_parameter(self, actual_user_id, parameter):
        cur = self.con.cursor()

        query = f"""SELECT {parameter} FROM users WHERE id=?"""
        result = cur.execute(query, (actual_user_id,)).fetchone()
        return result[0]

    def update_last_date(self, actual_user_id):
        today = str(datetime.now().date())
        cur = self.con.cursor()

        cur.execute("""UPDATE users SET last_date = ? WHERE id=?""",
                    (today, actual_user_id)).fetchone()
        self.con.commit()

    def get_last_date(self, actual_user_id):
        return self.get_parameter(actual_user_id, "last_date")

    def update_total_days(self, actual_user_id):
        cur = self.con.cursor()

        cur.execute("""UPDATE users SET total_days = total_days + 1 WHERE id=?""",
                    (actual_user_id,)).fetchone()
        self.con.commit()

    def get_total_days(self, actual_user_id):
        return self.get_parameter(actual_user_id, "total_days")

    def get_user_id(self, login, password):
        cur = self.con.cursor()

        result = cur.execute("""SELECT id FROM users WHERE login=? AND password=?""",
                             (login, password)).fetchone()
        return result[0]

    def get_balance(self, actual_user_id):
        return self.get_parameter(actual_user_id, "balance")

    def add_money(self, actual_user_id, money):
        cur = self.con.cursor()

        cur.execute("""UPDATE users SET balance = balance + ? WHERE id=?""",
                    (money, actual_user_id)).fetchone()
        self.con.commit()

    def set_max_gain(self, actual_user_id, max_win):
        self.set_parameter(actual_user_id, "max_win", max_win)

    def get_max_gain(self, actual_user_id):
        return self.get_parameter(actual_user_id, "max_win")

    def set_max_balance(self, actual_user_id, max_balance):
        self.set_parameter(actual_user_id, "max_balance", max_balance)

    def get_max_balance(self, actual_user_id):
        return self.get_parameter(actual_user_id, "max_balance")

    def add_total_gain(self, actual_user_id, money):
        cur = self.con.cursor()

        cur.execute("""UPDATE users SET total_win = total_win + ? WHERE id=?""",
                    (money, actual_user_id,)).fetchone()
        self.con.commit()

    def get_total_gain(self, actual_user_id):
        return self.get_parameter(actual_user_id, "total_win")

    def set_max_bet(self, actual_user_id, max_bet):
        self.set_parameter(actual_user_id, "max_bet", max_bet)

    def get_max_bet(self, actual_user_id):
        return self.get_parameter(actual_user_id, "max_bet")
