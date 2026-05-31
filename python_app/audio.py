from pycaw.pycaw import AudioUtilities
import processes as proc

# def getGroupedAudioSessions():

#     result = {}

#     sessions = AudioUtilities.GetAllSessions()

#     for session in sessions:

#         if not session.Process:
#             continue

#         audio_pid = session.Process.pid

#         friendly_pid = proc.resolveFriendlyProcessPID(audio_pid)

#         if friendly_pid not in result:
#             result[friendly_pid] = []

#         result[friendly_pid].append(session)

#     return result

def getGroupedAudioSessions():

    result = {}

    sessions = AudioUtilities.GetAllSessions()

    for session in sessions:

        if not session.Process:
            continue

        audio_pid = session.Process.pid

        friendly_pid = proc.resolveFriendlyProcessPID(audio_pid)

        if friendly_pid not in result:

            result[friendly_pid] = {
                "audioPIDs": [],
                "sessions": []
            }

        result[friendly_pid]["audioPIDs"].append(audio_pid)

        result[friendly_pid]["sessions"].append(session)

    return result

def volumeUp(app):
    for session in app.sessions:
        volume = session.SimpleAudioVolume
        current = volume.GetMasterVolume()
        new_volume = min(1.0, current + 0.02)
        volume.SetMasterVolume(new_volume, None)

def volumeDown(app):
    for session in app.sessions:
        volume = session.SimpleAudioVolume
        current = volume.GetMasterVolume()
        new_volume = max(0.0, current - 0.02)
        volume.SetMasterVolume(new_volume, None)