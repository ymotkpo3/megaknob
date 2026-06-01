import psutil
from config import SYSTEM, IGNORED

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
        psutil.NoSuchProcess,
        psutil.AccessDenied,
        psutil.ZombieProcess):
        return None

def getProcessName(PID):

    session = psutil.Process(PID)
    
    return session.name()