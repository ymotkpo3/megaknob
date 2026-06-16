import audio as au
import appBuilder as ab

def handleSerialCom(msg, apps, sel_index):
    if msg == "update":
        apps = ab.refreshApps(apps)

        if sel_index >= len(apps):
            sel_index = 0

        return apps, sel_index, "update"
        

    elif msg == "click":
        return apps, sel_index, "select"
    
    elif msg == "master":

        apps = ab.refreshApps(apps)

        return apps, 0, "master"

    elif msg == "appUP":

        sel_index = (sel_index + 1) % len(apps)

        return apps, sel_index, "appUP"

    elif msg == "appDWN":

        sel_index = (sel_index - 1) % len(apps)

        return apps, sel_index, "appDWN"

    elif msg == "volUP":
        if apps[sel_index].isMaster:
            au.masterVolUp()
            return apps, sel_index, "master volUP"

        au.volumeUp(apps[sel_index])
        return apps, sel_index, "volUP"
  
    elif msg == "volDWN":
        if apps[sel_index].isMaster:
            au.masterVolDown()
            return apps, sel_index, "master volDWN"

        au.volumeDown(apps[sel_index])
        return apps, sel_index, "volDWN"
    else:
        return apps,sel_index, f"Unknown message: {msg}"