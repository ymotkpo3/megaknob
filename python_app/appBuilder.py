from python_app.models.audio_app import AudioApp
from python_app import audio as au
from python_app.processes import getProcessNameAndPath

def createAudioApp(name: str, audio_pids: list[int] | None, top_pid: int | None, sessions: list, exec_path: str | None, is_master: bool) -> AudioApp:
    """
    Creates an AudioApp instance.

    Args:
        name:
            Display name of the application.

        audio_pids:
            Audio session process IDs associated with the application.

        top_pid:
            Top-level process PID representing the application.

        sessions:
            Audio sessions associated with the application.

        exec_path:
            Executable path of the application.

        is_master:
            Whether the AudioApp represents the master volume control.

    Returns:
        Newly created AudioApp instance.
    """
    return AudioApp(

        friendlyName = name,

        audioSessionPIDs = audio_pids,

        topProcessPID = top_pid,

        sessions = sessions,

        execPath = exec_path,

        isMaster = is_master



    )

def discoverAudioApps() -> list[AudioApp]:
    """
    Discovers all active audio applications.

    Returns:
        List of AudioApp objects representing currently active
        audio-producing applications.
    """

    audioSessions = au.getGroupedAudioSessions()

    output = []

    for friendlyPID in audioSessions:

        fname, exec_path = getProcessNameAndPath(friendlyPID)

        audioPIDs = audioSessions[friendlyPID]["audioPIDs"]

        sessions = audioSessions[friendlyPID]["sessions"]

        output.append(createAudioApp(fname, audioPIDs, friendlyPID, sessions, exec_path, False))

    return output

def mergeApps(oldApps: list[AudioApp], newApps: list[AudioApp]) -> list[AudioApp]:

    old_map = {app.topProcessPID: app for app in oldApps}

    new_map = {app.topProcessPID: app for app in newApps}

    result = []

    for app in oldApps:

        pid = app.topProcessPID

        if pid in new_map:
            result.append(new_map[pid])

    for app in newApps:

        pid = app.topProcessPID

        if pid not in old_map:
            result.append(app)

    return result

def refreshApps(oldApps: list[AudioApp] | None = None) -> list[AudioApp]:
    """
    Creates an updated AudioApp list.

    Args:
        oldApps:
            Previous application list. If None, a new list is created.

    Returns:
        List of active AudioApp objects, including the master volume entry.
    """

    newApps = [createAudioApp("master", None, None, [None], None, True)]
    newApps += discoverAudioApps()

    if oldApps is None:
        return newApps

    return mergeApps(oldApps, newApps)
