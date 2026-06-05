import psutil
from config import SYSTEM, IGNORED
from win32.win32gui import *

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

    large, small = ExtractIconEx(path, 0)

    if large:
        return large[0]

    return None