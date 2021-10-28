class LoginWindowResponder:
    def __init__(self, main_responder):
        self.main_responder = main_responder

    def set_info(self, info):
        self.info = info

    def set_interface(self, interface):
        self.interface = interface

    def login(self):
        login = self.interface.get_login_text()
        password = self.interface.get_password_text()
        try:
            self.check_user_existence(login, password)

            id = self.info.get_user_id(login, password)
            self.main_responder.casino_window_responder.set_actual_user(id)

            self.interface.main_interface_class.close_login_window()
            self.interface.main_interface_class.show_casino_window()
        except Exception as e:
            self.interface.set_error(str(e))

    def registration(self):
        self.interface.main_interface_class.close_login_window()
        self.interface.main_interface_class.show_registration_window()

    def check_user_existence(self, login, password):
        if not self.info.check_user_existence(login, password):
            if not self.info.check_login_existence(login):
                raise Exception("несуществующий логин")
            raise Exception("неверный пароль")
