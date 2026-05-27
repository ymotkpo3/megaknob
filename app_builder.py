from models import audio_app as app
from audio import getGroupedAudioSessions
from processes import resolveFriendlyProcessPID, getProcessName

def createAppObject(NAME, APID, FPID, ASESS):
    return app.AudioApp(

        friendlyName = NAME,

        audioSessionPID = APID,

        topProcessPID = FPID,

        sessions = ASESS

    )

def createAllAppsObjectsList():
    audioSessions = getGroupedAudioSessions()

    output = []



    for audioPID in audioSessions:
        toprocPID = resolveFriendlyProcessPID(audioPID)
        fname = getProcessName(toprocPID)
        sec = audioSessions[audioPID]
        output.append(createAppObject(fname, audioPID, toprocPID, sec))

    return output
        

