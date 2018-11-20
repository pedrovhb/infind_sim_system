import machine
import utime
import _thread
import ssd1306

i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
dac = machine.DAC(machine.Pin(25, machine.Pin.OUT), bits=12)
adc = machine.ADC(machine.Pin(36, machine.Pin.IN))


def input_thread():
    while True:
        value_in = adc.read()
        print(value_in)
        utime.sleep_ms(10)


#t = _thread.start_new_thread(input_thread, ())
i = 0
while True:
    try:
        value_in = str(adc.read()) + '\n'
        value_out = input(value_in)
        dac.write(int(value_out))
        print(value_out)
        utime.sleep_ms(10)
        oled.fill(0)
        oled.text(str(value_out), 1, 1)
        oled.text(str(value_in), 1, 20)
        oled.text(str(i), 1, 40)
        oled.show()

        i += 1
    except KeyboardInterrupt:
        break
    except Exception as e:
        print('100')
