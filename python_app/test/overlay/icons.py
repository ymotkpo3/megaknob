from PySide6.QtGui import QImage, QPixmap
from win32com.shell import shell, shellcon

def getAppPixmap(path):

    success, info = shell.SHGetFileInfo(
        path,
        0,
        shellcon.SHGFI_ICON |
        shellcon.SHGFI_LARGEICON
    )

    if not success:
        return None

    hicon = info[0]

    image = QImage.fromHICON(hicon)

    if image.isNull():
        return None

    return QPixmap.fromImage(image)