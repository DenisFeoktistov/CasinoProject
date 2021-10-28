from PyQt5.QtWidgets import QMainWindow

from ScreenSize import SCREENSIZE


# Этот класс создает окно, которое находится ровно посередине экрана (с моим разрешением).
# В документации QT к QMainWindow я прочитал, что "If the position is left uninitialized,
# then the platform window will allow the windowing system to position the window." Поэтому решил
# сделать такой класс, чтобы уж точно размещать окно ровно.
class CenteredWindow(QMainWindow):
    def __init__(self, width, height):
        super().__init__()
        self.setFixedSize(width, height)
        self.move((SCREENSIZE.width() - self.width()) / 2,
                  (SCREENSIZE.height() - self.height()) / 2)
