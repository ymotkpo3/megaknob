import serial.tools.list_ports
import serial

def findDevicePort():
    for port in serial.tools.list_ports.comports():

        if (
            port.vid == 0x2E8A
            and
            port.pid == 0x000A
        ):

            return port.device

    return None

def createSerialConnection(puerto):
    return serial.Serial(
        port= puerto,
        baudrate=115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=2
    )

def readSerial(ser):

    line = ser.readline()
    
    if line:
        return line.decode().strip()
    
    return None