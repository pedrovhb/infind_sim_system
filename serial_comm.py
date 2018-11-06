import serial


def init_serial(device='/dev/ttyUSB0'):
    ser = serial.Serial(device, 115200, timeout=1)
    return ser


def write_serial(value, device):
    device.write(str(value).encode('ascii') + b'\n')


def read_serial(device):
    reading = int(device.readline())
    device.reset_input_buffer()
    return reading


def close_serial(device):
    device.close()
