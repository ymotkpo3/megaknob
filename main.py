from audio import getSessions
from connection import readSerial

apps = getSessions()

selected_index = 0

print(apps[selected_index])

while True:
    msg = readSerial()

    if msg and msg == "select":
        selected_index = (selected_index + 1) % len(apps)
        print(apps[selected_index])