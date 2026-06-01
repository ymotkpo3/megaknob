import connection as con
import app_builder 
import audio as au
import extra_logic as log

apps = app_builder.createAllAppsObjectsList()

for app in apps:
    print(
        app.friendlyName,
        app.audioSessionPIDs,
        app.topProcessPID,
        len(app.sessions)
    )

selected_index = 0

print(apps[selected_index])

ser = con.createSerialConnection(con.findArduinoPort())

while True:
    msg = con.readSerial(ser)

    if msg == "update":
        newApps = app_builder.createAllAppsObjectsList()
        apps = log.mergeApps(apps, newApps)
        for app in apps:
            print(
                app.friendlyName,
                app.audioSessionPIDs,
                app.topProcessPID,
                len(app.sessions)
            )
        print(apps[selected_index])
    if msg == "click":
        
        print("select")

    if msg == "appUP":

        selected_index = (selected_index + 1) % len(apps)

        print(apps[selected_index])

    if msg == "appDWN":

        selected_index = (selected_index - 1) % len(apps)

        print(apps[selected_index])

    if msg == "volUP":

        au.volumeUp(apps[selected_index])

    if msg == "volDWN":

        au.volumeDown(apps[selected_index])
