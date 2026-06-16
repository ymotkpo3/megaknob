from dataclasses import dataclass


@dataclass
class AudioApp:
    """
    Represents an audio-producing application or the master volume control.

    Attributes:
        friendlyName:
            Display name of the application.

        topProcessPID:
            Top-level process PID associated with the application.

        audioSessionPIDs:
            Audio session process IDs grouped under this application.

        sessions:
            Audio sessions associated with the application.

        execPath:
            Path to the application's executable.

        isMaster:
            True if this object represents the master volume control.
    """

    friendlyName: str
    topProcessPID: int | None
    audioSessionPIDs: list[int] | None
    sessions: list
    execPath: str | None
    isMaster: bool

    def __repr__(self) -> str:
        return self.friendlyName