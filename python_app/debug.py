def appDebug(apps):
    for app in apps:
        print(
            app.friendlyName,
            app.audioSessionPIDs,
            app.topProcessPID,
            len(app.sessions),
            app.execPath
        )

def debMsgRead(apps, index, msg):

    if msg == None:
        pass
    
    elif msg == "update":
        appDebug(apps)

    elif msg == "master":
        print("long press master")

    elif msg == "appUP":
        print(apps[index])
        
    elif msg == "appDWN":
        print(apps[index])

    else:
        print(msg)