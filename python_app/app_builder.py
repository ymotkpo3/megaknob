from models import audio_app as app
from audio import getGroupedAudioSessions
from processes import getProcessName

def createAppObject(NAME, APID, FPID, ASESS):
    return app.AudioApp(

        friendlyName = NAME,

        audioSessionPIDs = APID,

        topProcessPID = FPID,

        sessions = ASESS

    )

def createAllAppsObjectsList():

    audioSessions = getGroupedAudioSessions()

    output = []

    for friendlyPID in audioSessions:

        fname = getProcessName(friendlyPID)

        audioPIDs = audioSessions[friendlyPID]["audioPIDs"]

        sessions = audioSessions[friendlyPID]["sessions"]

        output.append(createAppObject(fname, audioPIDs, friendlyPID, sessions))

    return output
        

