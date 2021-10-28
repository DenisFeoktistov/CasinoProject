class RegistrationWindowResponder:
    def __init__(self, main_responder):
        self.main_responder = main_responder

    def set_info(self, info):
        self.info = info

    def set_interface(self, interface):
        self.interface = interface

    def registration(self):
        login = self.interface.get_login_text()
        password = self.interface.get_password_text()
        try:
            self.check_login(login)
            self.check_login_existence(login)
            self.check_password(password)

            self.info.add_user(login, password)
            id = self.info.get_user_id(login,
                                       password)  # опять-таки, есть сомнения по поводу
            # правильности такой конструкции...
            self.main_responder.casino_window_responder.set_actual_user(id)

            self.interface.main_interface_class.close_registration_window()
            self.interface.main_interface_class.show_casino_window()
        except Exception as e:
            self.interface.set_error(str(e))

    def login(self):
        self.interface.main_interface_class.close_registration_window()
        self.interface.main_interface_class.show_login_window()

    def check_login(self, login):
        if login == "":
            raise Exception("Логин не может быть пустой строкой")
        if not login[0].isalpha():
            raise Exception("Логин должен начинаться с буквы")

    def check_password(self, password):
        if len(password) < 5:
            raise Exception("Пароль слишком короткий")
        if not password.isalnum():
            raise Exception("Пароль должен быть из букв и цифр")

    def check_login_existence(self, login):
        if self.info.check_login_existence(login):
            raise Exception("такой логин уже существует")
