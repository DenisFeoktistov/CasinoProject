from RegistrationWindow import RegistrationWindow
from CasinoWindow import CasinoWindow
from LoginWindow import LoginWindow


class Interface:
    def __init__(self):
        self.login_window = LoginWindow(self)
        self.registration_window = RegistrationWindow(self)
        self.casino_window = CasinoWindow(self)

    def set_responder(self, responder):
        self.responder = responder
        self.login_window.set_responder(responder.login_window_responder)
        self.registration_window.set_responder(responder.registration_window_responder)
        self.casino_window.set_responder(responder.casino_window_responder)

    def show_login_window(self):
        self.login_window.show()

    def close_login_window(self):
        self.login_window.close()

    def show_registration_window(self):
        self.registration_window.show()

    def close_registration_window(self):
        self.registration_window.close()

    def show_casino_window(self):
        self.casino_window.show()

    def close_casino_window(self):
        self.casino_window.close()

    def show(self):
        self.login_window.show()
