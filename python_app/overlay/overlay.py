from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QPainter, QPen
# from audio import getVolume

class Overlay(QWidget):

    def __init__(self):
        super().__init__()

        self.volume = 0
        self.icon = None
        self.mode = "volume"

        self.setFixedSize(200, 200)

        self.setWindowFlags(
            Qt.Tool
            | Qt.FramelessWindowHint
            | Qt.WindowStaysOnTopHint
        )

    def paintEvent(self, event):

        painter = QPainter(self)

        ringRect = QRect(
            25,
            25,
            150,
            150
        )

        background_pen = QPen()
        background_pen.setWidth(12)

        painter.setPen(background_pen)

        painter.drawEllipse(ringRect)

        if self.mode == "volume":

            progress_pen = QPen()
            progress_pen.setWidth(12)

            painter.setPen(progress_pen)

            span = int(
                360 *
                self.volume *
                16
            )

            painter.drawArc(
                ringRect,
                90 * 16,
                -span
            )

        if self.icon:

            painter.drawPixmap(
                60,
                60,
                80,
                80,
                self.icon
            )