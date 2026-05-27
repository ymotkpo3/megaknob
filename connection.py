import serial.tools.list_ports
import serial

def findArduinoPort():
    for port in serial.tools.list_ports.comports():
        if 'Arduino' in port.description or 'CH340' in port.description:
            return port.device
    return None

def createSerialConnection(puerto):
    ser = serial.Serial(
        port= puerto,
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=2
        )
    
    return ser

def readSerial():

    line = createSerialConnection(findArduinoPort()).readline()
    
    if line:
        return line.decode().strip()
    
    return None