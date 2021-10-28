from RegistrationWindowResponder import RegistrationWindowResponder
from CasinoWindowResponder import CasinoWindowResponder
from LoginWindowResponder import LoginWindowResponder


class CasinoResponder:
    def __init__(self):
        self.login_window_responder = LoginWindowResponder(self)
        self.registration_window_responder = RegistrationWindowResponder(self)
        self.casino_window_responder = CasinoWindowResponder(self)

    def set_interface(self, interface):
        self.interface = interface
        self.registration_window_responder.set_interface(interface.registration_window)
        self.login_window_responder.set_interface(interface.login_window)
        self.casino_window_responder.set_interface(interface.casino_window)

    def set_info(self, info):
        self.info = info
        self.registration_window_responder.set_info(info)
        self.login_window_responder.set_info(info)
        self.casino_window_responder.set_info(info)
