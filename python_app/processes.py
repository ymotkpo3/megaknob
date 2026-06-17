import psutil
from python_app.config import SYSTEM, IGNORED
import win32com.shell.shell as shell
import win32com.shell.shellcon as shellcon

def resolveFriendlyProcessPID(PID: int) -> int | None:
    """
    Resolves the user-facing process associated with an audio session.

    Starting from the provided PID, the process tree is traversed
    upwards until a suitable parent process is found.

    Processes listed in IGNORED are skipped.
    Traversal stops when a process listed in SYSTEM is reached.

    Audio sessions are often attached to helper or child processes
    instead of the application visible to the user.

    This function walks the process hierarchy to identify the most
    representative application process.

    Args:
        PID:
            Audio session process ID.

    Returns:
        int | None:
            PID of the best matching application process,
            or None if no suitable process can be resolved.
    """
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

def getProcessName(PID: int) -> str:
    """
    Returns the executable name of a process.

    Args:
        PID:
            Target process ID.

    Returns:
        Process executable name.
    """

    session = psutil.Process(PID)
    
    return session.name()

def getProcessPath(pid: int) -> str | None:
    """
    Returns the executable path of a process.

    Args:
        pid:
            Target process ID.

    Returns:
        Full executable path if available,
        otherwise None.
    """

    try:
        process = psutil.Process(pid)

        return process.exe()

    except (
        psutil.NoSuchProcess,
        psutil.AccessDenied
    ):
        return None
    
# def getProcessIcon(path: str):
#     """
#     Retrieves the Windows icon associated with an executable.

#     Args:
#         path:
#             Executable file path.

#     Returns:
#         Native Windows icon handle if successful,
#         otherwise None.
#     """

#     success, info = shell.SHGetFileInfo(
#         path,
#         0,
#         shellcon.SHGFI_ICON |
#         shellcon.SHGFI_LARGEICON
#     )

#     if not success:
#         return None

#     return info[0]