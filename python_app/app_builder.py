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

def mergeApps(oldApps, newApps):

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

def refreshApps(apps):

    newApps = [createAppObject("master", None, None, [None])]
    newApps += createAllAppsObjectsList()

    return mergeApps(apps, newApps)

