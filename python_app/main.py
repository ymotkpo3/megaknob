import connection as con
import app_builder as ab
import audio as au
import extra_logic as log
import serial

appsNoMaster = ab.createAllAppsObjectsList()

apps = [ab.createAppObject("master", None, None, [None])]
apps += appsNoMaster

for app in apps:
    print(
        app.friendlyName,
        app.audioSessionPIDs,
        app.topProcessPID,
        len(app.sessions)
    )

selected_index = 0

print(apps[selected_index])

port = con.findDevicePort()

if port is not None:
    ser = con.createSerialConnection(port)
    connected = True
else:
    ser = None
    connected = False

while True:
    try:
        if connected == False:
            ser = con.createSerialConnection(con.findDevicePort())
            if ser.port != None:
                connected = True
                print("RECONNECTED")
                selected_index = 0
                print(apps[selected_index])


        if connected == True:
            msg = con.readSerial(ser)
            if msg == "update":
                newApps = [ab.createAppObject("master", None, None, [None])] + ab.createAllAppsObjectsList()
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
            
            if msg == "master":
                newApps = [ab.createAppObject("master", None, None, [None])] + ab.createAllAppsObjectsList()
                apps = log.mergeApps(apps, newApps)
                for app in apps:
                    print(
                        app.friendlyName,
                        app.audioSessionPIDs,
                        app.topProcessPID,
                        len(app.sessions)
                    )
                selected_index = 0
                print(apps[selected_index])

            if msg == "appUP":

                selected_index = (selected_index + 1) % len(apps)

                print(apps[selected_index])

            if msg == "appDWN":

                selected_index = (selected_index - 1) % len(apps)

                print(apps[selected_index])

            if msg == "volUP" and apps[selected_index].friendlyName == "master":

                au.masterVolUp()
                continue

            if msg == "volDWN" and apps[selected_index].friendlyName == "master":
                
                au.masterVolDown()
                continue

            if msg == "volUP":

                au.volumeUp(apps[selected_index])

            if msg == "volDWN":

                au.volumeDown(apps[selected_index])
    except(serial.SerialException):
        if connected == True:
            connected = False
            print("DISCONNECTED")
        continue
    except(IndexError):
        selected_index = len(apps)