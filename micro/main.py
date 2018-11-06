import machine
import utime

# i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))
# oled = ssd1306.SSD1306_I2C(128, 64, i2c)
dac = machine.DAC(machine.Pin(25, machine.Pin.OUT), bits=12)
adc = machine.ADC(machine.Pin(36, machine.Pin.IN))

while True:
    try:
        value_out = input()
        dac.write(int(value_out))
        value_in = adc.read()
        # utime.sleep_ms(30)
        print(value_in)
    except KeyboardInterrupt:
        break
    except:
        print('100')

