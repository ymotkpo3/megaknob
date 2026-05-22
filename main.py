from pycaw.pycaw import AudioUtilities
import connection
sessions = AudioUtilities.GetAllSessions()

unique_sessions = {}

port = connection.find_arduino_port()

for session in sessions:
    if not session.Process:
        continue

    name = session.Process.name()

    if name not in unique_sessions:
        unique_sessions[name] = session


for name in unique_sessions:
    print(name)

while True:
    print(connection.readSerial())