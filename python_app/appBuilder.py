from python_app.models.audio_app import AudioApp
from python_app import audio as au
from python_app.processes import getProcessName, getProcessPath

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

        fname = getProcessName(friendlyPID)

        audioPIDs = audioSessions[friendlyPID]["audioPIDs"]

        sessions = audioSessions[friendlyPID]["sessions"]

        exec = getProcessPath(friendlyPID)

        output.append(createAudioApp(fname, audioPIDs, friendlyPID, sessions, exec, False))

    return output

def mergeApps(oldApps: list[AudioApp],newApps: list[AudioApp]) -> list[AudioApp]:
    """
    Preserves the ordering of the previous application list.

    Args:
        oldApps:
            Previously displayed applications.

        newApps:
            Newly discovered applications.

    Returns:
        Updated application list with:
        - closed applications removed,
        - existing applications kept in their previous order,
        - new applications appended at the end.
    """


    old_ids = []
    new_ids = []

    for app in oldApps:
        old_ids.append(app.topProcessPID)

    for app in newApps:
        new_ids.append(app.topProcessPID)
        
    new = []
    result = []


    for app1 in oldApps:
        for app2 in newApps:
            if app1.topProcessPID == app2.topProcessPID:
                result.append(app2)
                break
    
    for new_id in new_ids:
        if new_id not in old_ids:
            for app in newApps:
                if app.topProcessPID == new_id:
                    new.append(app)
                    break

    result += new

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
