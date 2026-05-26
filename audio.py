from pycaw.pycaw import AudioUtilities

def getAudioSessions():

    result = {}

    sessions = AudioUtilities.GetAllSessions()

    for session in sessions:

        if not session.Process:
            continue

        pid = session.Process.pid

        if pid not in result:
            result[pid] = []

        result[pid].append(session)

    return result

def volumeUp(session):
    pass

def volumeDown(session):
    pass