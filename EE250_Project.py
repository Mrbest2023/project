import grovepi
from grovepi import *
from grove_rgb_lcd import *
from gpiozero import Button

buton = Button(2)

sound_sensor=0
grovepi.pinMode(sound_sensor, "INPUT")

led=5



if __name__ == '__main__':

    if     : 
        while True:
            try:
                sensor_value=grovepi.analogRead(sound_sensor)
                setText_norefresh()

            except KeyboardInterrupt as e:
                print(str(e))
                setText("")
                break

            sleep(0.05)
