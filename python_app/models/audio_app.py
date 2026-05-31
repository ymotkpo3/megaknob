class AudioApp:

    def __init__(
        self,
        friendlyName,
        topProcessPID,
        audioSessionPIDs,
        sessions
    ):

        self.friendlyName = friendlyName

        self.topProcessPID = topProcessPID

        self.audioSessionPIDs = audioSessionPIDs

        self.sessions = sessions

    def __repr__(self):
        return self.friendlyName