import sys
from pathlib import Path

sys.path.append(
    str(
        Path(__file__).resolve().parent.parent
    )
)

from PySide6.QtWidgets import QApplication


from python_app.test.overlay.overlay import Overlay
from python_app.test.overlay import icons

app = QApplication([])

window = Overlay()

window.showVolume(icons.getAppPixmap(r"D:\Programas\Steam\steam.exe"), 0.75)
window.show()

app.exec()