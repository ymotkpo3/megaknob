import psutil
from config import SYSTEM, IGNORED

def resolveFriendlyProcessPID(PID):

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

def getProcessName(PID):
    session = psutil.Process(PID)
    return session.name()