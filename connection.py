import serial.tools.list_ports

def find_arduino():
    for port in serial.tools.list_ports.comports():
        if 'Arduino' in port.description or 'CH340' in port.description:
            return port.device
    return None
    
port = find_arduino()

# if port:
#     print(f"Found Arduino on {port}")
# else:
#     print("Arduino not found")