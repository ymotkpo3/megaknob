import serial.tools.list_ports
import serial

def find_arduino():
    for port in serial.tools.list_ports.comports():
        if 'Arduino' in port.description or 'CH340' in port.description:
            return port.device
    return None
    
port = find_arduino()



ser = serial.Serial(
    port= port,
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=0
    )

print("connected to: " + ser.portstr)
count=1

while True:
    line = ser.readline()
    if line:
        text = line.decode()
        print(text)
        



ser.close()