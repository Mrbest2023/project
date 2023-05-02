import grovepi
from grovepi import *
from grove_rgb_lcd import *

sound_sensor=0
grovepi.pinMode(sound_sensor, "INPUT")

led=5






while True:
    try:
        sr=32
        sensor_value=grovepi.analogRead(sound_sensor)
        frequency,X=frequency_spectrum(sensor_value, sr)
        type=note(frequency)
        setText_norefresh(type)

    except KeyboardInterrupt as e:
        print(str(e))
        setText("")
        break

    sleep(0.05)
