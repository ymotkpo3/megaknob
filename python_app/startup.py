import sys
from pathlib import Path

from win32com.client import Dispatch


APP_NAME = "Megaknob"


def _getStartupFolder() -> Path:
    """
    Returns the current user's Windows Startup folder.
    """

    shell = Dispatch("WScript.Shell")

    return Path(
        shell.SpecialFolders("Startup")
    )


def _getShortcutPath() -> Path:
    """
    Returns the path used for Megaknob's Startup shortcut.
    """

    return _getStartupFolder() / f"{APP_NAME}.lnk"


def _getLaunchConfiguration() -> tuple[Path, str, Path, str]:
    """
    Builds the shortcut configuration for the current environment.

    Returns:
        Tuple containing the target executable, command-line arguments,
        working directory and icon location.
    """

    if getattr(sys, "frozen", False):
        executable = Path(sys.executable).resolve()

        return (
            executable,
            "",
            executable.parent,
            f"{executable},0"
        )

    project_root = Path(__file__).resolve().parent.parent
    python_executable = Path(sys.executable).resolve()

    return (
        python_executable,
        "-m python_app.main",
        project_root,
        f"{python_executable},0"
    )


def isStartupEnabled() -> bool:
    """
    Checks whether Megaknob's Startup shortcut exists.
    """

    return _getShortcutPath().exists()


def enableStartup() -> None:
    """
    Creates or updates Megaknob's shortcut in the Windows Startup folder.
    """

    target, arguments, working_directory, icon_location = (
        _getLaunchConfiguration()
    )

    shell = Dispatch("WScript.Shell")

    shortcut = shell.CreateShortCut(
        str(_getShortcutPath())
    )

    shortcut.TargetPath = str(target)
    shortcut.Arguments = arguments
    shortcut.WorkingDirectory = str(working_directory)
    shortcut.IconLocation = icon_location
    shortcut.Description = "Megaknob volume controller"

    shortcut.Save()


def disableStartup() -> None:
    """
    Removes Megaknob's shortcut from the Windows Startup folder.
    """

    shortcut_path = _getShortcutPath()

    if shortcut_path.exists():
        shortcut_path.unlink()


def refreshStartupShortcut() -> None:
    """
    Updates the shortcut to point to the currently running version.

    This is useful when Megaknob is renamed, moved or updated.
    """

    if isStartupEnabled():
        enableStartup()