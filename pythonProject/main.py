from PyQt5.QtWidgets import QApplication

from Responder import CasinoResponder
from Interface import Interface
from Info import CasinoInfo

import sys


class Casino:
    def __init__(self):
        self.responder = CasinoResponder()
        self.interface = Interface()
        self.info = CasinoInfo()

        self.interface.set_responder(self.responder)

        self.responder.set_interface(self.interface)
        self.responder.set_info(self.info)

    def show(self):
        self.interface.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Casino()
    ex.show()
    sys.exit(app.exec())
