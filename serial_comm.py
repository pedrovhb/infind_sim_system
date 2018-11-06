import serial


def init_serial(device='/dev/ttyUSB0'):
    ser = serial.Serial(device, 115200)
    return ser


def write_serial(value, device):
    device.write(str(value).encode('ascii'))


def read_serial(device):
    return int(device.readline())


def close_serial(device):
    device.close()
