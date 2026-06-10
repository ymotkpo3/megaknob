from PySide6.QtGui import QImage, QPixmap
import win32com.shell.shell as shell
import win32com.shell.shellcon as shellcon

def getProcessPixmap(path):

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