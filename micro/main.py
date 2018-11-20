import machine
import utime
import _thread

# i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))
# oled = ssd1306.SSD1306_I2C(128, 64, i2c)
dac = machine.DAC(machine.Pin(25, machine.Pin.OUT), bits=12)
adc = machine.ADC(machine.Pin(36, machine.Pin.IN))


def input_thread():
    while True:
        value_in = adc.read()
        print(value_in)
        utime.sleep_ms(1)


_thread.start_new_thread(input_thread, ())
while True:
    try:
        value_out = input()
        dac.write(int(value_out))
        utime.sleep_ms(1)
    except KeyboardInterrupt:
        break
    except:
        print('100')
