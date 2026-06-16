import audio as au
import appBuilder as ab
from models.audio_app import AudioApp
from models.serial_com_result import SerialComResult

def handleSerialCom(msg: str, apps: list[AudioApp], selected_index: int) -> SerialComResult:
    """
    Processes a command received from the volume controller.

    Depending on the received command, the application list,
    selected application, or audio volume may be modified.

    Args:
        msg:
            Command received through the serial connection.

        apps:
            Current AudioApp list.

        selected_index:
            Index of the currently selected AudioApp.

    Returns:
        SerialComResult:
            Result containing the updated application list,
            selected application index and debug message.
    """
    if msg == "update":
        apps = ab.refreshApps(apps)

        if selected_index >= len(apps):
            selected_index = 0

        return SerialComResult(apps, selected_index, "update")
    
    elif msg == "click":
        return SerialComResult(apps, selected_index, "select")
    
    elif msg == "master":

        apps = ab.refreshApps(apps)

        return SerialComResult(apps, 0, "master")

    elif msg == "appUP":

        selected_index = (selected_index + 1) % len(apps)

        return SerialComResult(apps, selected_index, "appUP")

    elif msg == "appDWN":

        selected_index = (selected_index - 1) % len(apps)

        return SerialComResult(apps, selected_index, "appDWN")

    elif msg == "volUP":
        if apps[selected_index].isMaster:
            au.masterVolUp()
            return SerialComResult(apps, selected_index, "master volUP")

        au.volumeUp(apps[selected_index])
        return SerialComResult(apps, selected_index, "volUP")
  
    elif msg == "volDWN":
        if apps[selected_index].isMaster:
            au.masterVolDown()
            return SerialComResult(apps, selected_index, "master volDWN")

        au.volumeDown(apps[selected_index])
        return SerialComResult(apps, selected_index, "volDWN")
    else:
        return SerialComResult(apps,selected_index, f"Unknown message: {msg}")