import time
import serial

from python_app.test import connection as con
from python_app.test import appBuilder as ab
from python_app.test import communication as com
from python_app.test import debug as deb


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
            result = com.handleSerialCom(msg, apps, selected_index)
            apps = result.apps
            selected_index = result.selected_index
            
            deb.printDebugMessage(apps, selected_index, result.debug_message)

    except(serial.SerialException):

        if ser is not None:
            print("DISCONNECTED")

        ser = None