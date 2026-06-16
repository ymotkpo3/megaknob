from models.audio_app import AudioApp
from audio import getGroupedAudioSessions
from processes import getProcessName, getProcessPath

def createAudioApp(name, audio_pids, top_pid, sessions, exec_path, is_master):
    return AudioApp(

        friendlyName = name,

        audioSessionPIDs = audio_pids,

        topProcessPID = top_pid,

        sessions = sessions,

        execPath = exec_path,

        isMaster = is_master



    )

def discoverAudioApps():

    audioSessions = getGroupedAudioSessions()

    output = []

    for friendlyPID in audioSessions:

        fname = getProcessName(friendlyPID)

        audioPIDs = audioSessions[friendlyPID]["audioPIDs"]

        sessions = audioSessions[friendlyPID]["sessions"]

        exec = getProcessPath(friendlyPID)

        output.append(createAudioApp(fname, audioPIDs, friendlyPID, sessions, exec, False))

    return output

def mergeApps(oldApps, newApps):

    """
    Merges two AudioApp lists while preserving the user's previous ordering.

    Parameters
    ----------
    oldApps : list[AudioApp]
        Previously displayed application list.

    newApps : list[AudioApp]
        Newly discovered application list.

    Returns
    -------
    list[AudioApp]
        Updated application list preserving the previous order,
        removing closed applications and appending new applications
        at the end.
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

def refreshApps(oldApps=None):

    newApps = [createAudioApp("master", None, None, [None], None, True)]
    newApps += discoverAudioApps()

    if oldApps is None:
        return newApps

    return mergeApps(oldApps, newApps)
