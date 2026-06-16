from dataclasses import dataclass

from models.audio_app import AudioApp


@dataclass
class SerialComResult:
    """
    Result returned by handleSerialCom().

    Attributes:
        apps:
            Updated application list.

        selected_index:
            Index of the selected application.

        debug_message:
            Message describing the performed action.
    """
    apps: list[AudioApp]
    selected_index: int
    debug_message: str