from python_app.overlay.overlay import Overlay

_overlay = None


def init():
    global _overlay

    if _overlay is None:
        _overlay = Overlay()


def get():
    return _overlay