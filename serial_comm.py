import serial


def init_serial(device='/dev/ttyUSB0'):
    ser = serial.Serial(device, 115200, timeout=1)
    return ser


def write_serial(value, device):
    device.write(str(value).encode('ascii') + b'\r\n')
    device.flush()


def read_serial(device):
    try:
        reading = device.read_all().split(b'\r\n')[1]
    except IndexError:
        reading = 0
    reading = int(reading)
    device.reset_input_buffer()
    return reading


def close_serial(device):
    device.close()
