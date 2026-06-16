class AudioApp:

    def __init__(
        self,
        friendlyName,
        topProcessPID,
        audioSessionPIDs,
        sessions,
        execPath,
        isMaster
    ):

        self.friendlyName = friendlyName

        self.topProcessPID = topProcessPID

        self.audioSessionPIDs = audioSessionPIDs

        self.sessions = sessions

        self.execPath = execPath

        self.isMaster = isMaster

    def __repr__(self):
        return self.friendlyName