from pycaw.pycaw import AudioUtilities
from connection import port
sessions = AudioUtilities.GetAllSessions()

sesiones_unicas = {}

numero = 0

for session in sessions:
    
    

    if not session.Process:
        continue

    nombre = session.Process.name()

    if nombre not in sesiones_unicas:
        sesiones_unicas[numero] = session
        numero += 1



for nombre in sesiones_unicas:
    print(nombre)

print(port)