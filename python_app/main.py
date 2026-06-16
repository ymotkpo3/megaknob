import time
import connection as con
import appBuilder as ab
import debug as deb
import serial
import communication as com

apps = ab.refreshApps()
selected_index = 0

deb.appDebug(apps)
print(apps[selected_index])

ser = con.connect()

while True:
    try:
        if ser is None:
            ser = con.reconnect()
            if ser is not None:
                selected_index = 0
                print(apps[selected_index])
            else:
                time.sleep(1)
                continue


        msg = con.readSerial(ser)
        if msg:
            apps, selected_index, debmsg = com.handleSerialCom(msg, apps, selected_index)
            deb.debMsgRead(apps, selected_index, debmsg)

  


    except(serial.SerialException):
        if ser is not None:
            print("DISCONNECTED")
        ser = None