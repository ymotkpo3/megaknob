from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QPainter, QPen


class Overlay(QWidget):

    def __init__(self):
        super().__init__()

        # ----------------------------
        # DATOS DEL OVERLAY
        # ----------------------------

        self.volume = 0

        self.icon = None

        self.mode = "volume"

        # ----------------------------
        # CONFIGURACIÓN DE LA VENTANA
        # ----------------------------

        self.setFixedSize(50, 50)

        self.setWindowFlags(
            Qt.Tool
            | Qt.FramelessWindowHint
            | Qt.WindowStaysOnTopHint
        )

    def paintEvent(self, event):

        # ==================================================
        # PREPARAR EL DIBUJANTE
        # ==================================================

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.Antialiasing,
            True
        )

        painter.setRenderHint(
            QPainter.SmoothPixmapTransform,
            True
        )

        painter.fillRect(
            self.rect(),
            Qt.black
        )

        # ==================================================
        # DEFINIR GEOMETRÍA DEL ANILLO
        # ==================================================

        ringRect = QRect(
            3,
            3,
            44,
            44
        )

        # ==================================================
        # DIBUJAR CÍRCULO DE FONDO
        # ==================================================

        background_pen = QPen(Qt.white)

        background_pen.setWidth(3)

        painter.setPen(background_pen)

        painter.drawEllipse(ringRect)

        # ==================================================
        # DIBUJAR PROGRESO DE VOLUMEN
        # ==================================================

        if self.mode == "volume":

            progress_pen = QPen(Qt.white)

            progress_pen.setWidth(3)

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

        # ==================================================
        # DIBUJAR ICONO
        # ==================================================

        if self.icon:

            iconSize = 24

            x = (self.width() - iconSize) // 2
            y = (self.height() - iconSize) // 2

            painter.drawPixmap(
                x,
                y,
                iconSize,
                iconSize,
                self.icon
            )
    def showVolume(self, icon, volume):

        self.mode = "volume"
        self.icon = icon
        self.volume = volume

        self.update()

    def showSelection(self, icon):

        self.mode = "selection"
        self.icon = icon

        self.update()