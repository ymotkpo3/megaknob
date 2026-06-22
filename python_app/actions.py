from python_app import audio
from python_app import appBuilder
from python_app.overlay import overlay

def refresh(apps):
    
    return appBuilder.refreshApps(apps)

def masterVolUp():

    audio.volumeUp()

def masterVolDown():

    audio.volumeDown()

def volUp(app):

    audio.volumeUp(app)

def volDown(app):

    audio.volumeDown(app)