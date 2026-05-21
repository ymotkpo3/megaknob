import serial.tools.list_ports
import serial

def find_arduino_port():
    for port in serial.tools.list_ports.comports():
        if 'Arduino' in port.description or 'CH340' in port.description:
            return port.device
    return None

ser = serial.Serial(
    port= find_arduino_port(),
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=2
    )

def readSerial():
    while True:
        line = ser.readline()
        if line:
            text = line.decode()
            return text