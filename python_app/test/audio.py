from pycaw.pycaw import AudioUtilities
from python_app.test import processes as proc

from python_app.test.models.audio_app import AudioApp

device = AudioUtilities.GetSpeakers()

def getGroupedAudioSessions() -> dict[int, dict[str, list]]:
    """
    Groups audio sessions by their top-level process.

    Multiple audio sessions may belong to the same application.
    This function resolves the user-facing process and groups all
    related audio sessions under a single PID.

    Returns:
        Dictionary indexed by friendly process PID.

        Each entry contains:
            audioPIDs:
                List of audio session process IDs.

            sessions:
                List of PyCAW audio sessions associated with
                the application.
    """

    result = {}

    sessions = AudioUtilities.GetAllSessions()

    for session in sessions:

        if not session.Process:
            
            continue

        audio_pid = session.Process.pid

        friendly_pid = proc.resolveFriendlyProcessPID(audio_pid)

        if friendly_pid is None:
            continue

        if friendly_pid not in result:

            result[friendly_pid] = {
                "audioPIDs": [],
                "sessions": []
            }


        result[friendly_pid]["audioPIDs"].append(audio_pid)

        result[friendly_pid]["sessions"].append(session)

    return result


def volumeUp(app: AudioApp | None = None) -> None:
    """
    Increases the volume of all audio sessions belonging to an application.

    Args:
        app:
            Target AudioApp.
    """
    if app is None:
        current = device.EndpointVolume.GetMasterVolumeLevelScalar()

        new_volume = min(1.0, current + 0.02)

        device.EndpointVolume.SetMasterVolumeLevelScalar(new_volume, None)
    else:    
        for session in app.sessions:

            volume = session.SimpleAudioVolume

            current = volume.GetMasterVolume()

            new_volume = min(1.0, current + 0.02)

            volume.SetMasterVolume(new_volume, None)

def volumeDown(app: AudioApp | None = None) -> None:
    """
    Decreases the volume of all audio sessions belonging to an application.

    Args:
        app:
            Target AudioApp.
    """
    if app is None:
        current = device.EndpointVolume.GetMasterVolumeLevelScalar()

        if current <= 0.02:
            new_volume = 0
        elif current > 0:
            new_volume = current - 0.02

        device.EndpointVolume.SetMasterVolumeLevelScalar(new_volume, None)
    else:
        for session in app.sessions:

            volume = session.SimpleAudioVolume

            current = volume.GetMasterVolume()

            new_volume = max(0.0, current - 0.02)

            volume.SetMasterVolume(new_volume, None)

def getVolume(app: AudioApp) -> float:
    """
    Returns the current volume level of an application.

    For the master entry, the system master volume is returned.
    For applications, the volume of the first audio session is used.

    Args:
        app:
            Target AudioApp.

    Returns:
        Current volume level in the range [0.0, 1.0].
    """

    if app.isMaster:
        return device.EndpointVolume.GetMasterVolumeLevelScalar()

    if not app.sessions:
        return 0

    return app.sessions[0].SimpleAudioVolume.GetMasterVolume()