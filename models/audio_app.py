class AudioApp:

    def __init__(
        self,
        friendlyName,
        audioSessionPIDs,
        topProcessPID,
        sessions
    ):

        self.friendlyName = friendlyName

        self.audioSessionPIDs = audioSessionPIDs

        self.topProcessPID = topProcessPID

        self.sessions = sessions