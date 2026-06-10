import psutil
from config import SYSTEM, IGNORED
from win32.win32gui import *
import win32com.shell.shell as shell
import win32com.shell.shellcon as shellcon

def resolveFriendlyProcessPID(PID):
    try:
        current = psutil.Process(PID)
        
        best_match = None

        while current:

            if current.name() in SYSTEM:

                if best_match:
                    break

            elif current.name() not in IGNORED:

                best_match = current

            current = current.parent()

        return best_match.pid
    except(
        AttributeError,
        psutil.NoSuchProcess,
        psutil.AccessDenied,
        psutil.ZombieProcess):
        return None

def getProcessName(PID):

    session = psutil.Process(PID)
    
    return session.name()

def getProcessPath(pid):

    try:
        process = psutil.Process(pid)

        return process.exe()

    except (
        psutil.NoSuchProcess,
        psutil.AccessDenied
    ):
        return None
    
def getProcessIcon(path):

    success, info = shell.SHGetFileInfo(
        path,
        0,
        shellcon.SHGFI_ICON |
        shellcon.SHGFI_LARGEICON
    )

    if not success:
        return None

    return info[0]