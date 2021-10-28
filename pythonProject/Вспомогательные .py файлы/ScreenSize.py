class ScreenSize:
    def __init__(self):
        pass

    def width(self):
        return 1440

    def height(self):
        return 900 - 124  # учитывается нижняя панелька


SCREENSIZE = ScreenSize()
# сделал такой вот класс и создал его экземпляр, как константу, чтобы упростить код, когда есть
# необходимость использовать мое разрешение экрана
