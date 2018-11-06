import ssd1306
import machine

i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
dac = machine.DAC(machine.Pin(25, machine.Pin.OUT), bits=12)
adc = machine.ADC(machine.Pin(36, machine.Pin.IN))

oled.text('infind', 0, 0)
oled.show()


while True:
    try:
        value_out = input()
        dac.write(int(value_out))
        value_in = adc.read()
        print(value_in)
    except:
        pass

