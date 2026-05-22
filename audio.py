from pycaw.pycaw import AudioUtilities

def getSessions():

    unique_sessions = {}

    sessions = AudioUtilities.GetAllSessions()

    for session in sessions:

        if not session.Process:
            continue

        name = session.Process.name()

        if name not in unique_sessions:
            unique_sessions[name] = session

    result = ["MASTER"]

    result.extend(unique_sessions.keys())

    return result

def volumeUp(session):
    pass

def volumeDown(session):
    pass
