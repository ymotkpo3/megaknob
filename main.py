import connection as con
import app_builder


apps = app_builder.createAllAppsObjectsList()

selected_index = 0

print(apps[selected_index])

ser = con.createSerialConnection(con.findArduinoPort())

while True:
    msg = con.readSerial(ser)

    if msg and msg == "select":
        selected_index = (selected_index + 1) % len(apps)
        print(apps[selected_index])