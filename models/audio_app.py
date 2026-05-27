class AudioApp:

    def __init__(
        self,
        friendlyName,
        audioSessionPID,
        topProcessPID,
        sessions
    ):

        self.friendlyName = friendlyName

        self.audioSessionPID = audioSessionPID

        self.topProcessPID = topProcessPID

        self.sessions = sessions