import connection as con
import app_builder as ab
import debug as deb
import serial
import communication as com

appsNoMaster = ab.createAllAppsObjectsList()

apps = [ab.createAppObject("master", None, None, [None], None)]
apps += appsNoMaster

deb.appDebug(apps)

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


        if connected:
            msg = con.readSerial(ser)
            if msg:
                apps, selected_index, debmsg = com.handleSerialCom(msg, apps, selected_index)
                deb.debMsgRead(apps, selected_index, debmsg)
  


    except(serial.SerialException):
        if connected == True:
            connected = False
            print("DISCONNECTED")
        continue