from pycaw.pycaw import AudioUtilities
from connection import port
sessions = AudioUtilities.GetAllSessions()

sesiones_unicas = {}

numero = 0

for session in sessions:
    
    

    if not session.Process:
        continue

    name = session.Process.name()

    if name not in sesiones_unicas:
        sesiones_unicas[name] = session
        numero += 1



for name in sesiones_unicas:
    print(name)

print(port)