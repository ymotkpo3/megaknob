from python_app.test import audio
from python_app.test import appBuilder
from python_app.test.overlay import overlay

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