import grovepi
from grovepi import *
from grove_rgb_lcd import *
from gpiozero import Button
from signal import pause

button = Button(2)

sound_sensor=0
grovepi.pinMode(sound_sensor, "INPUT")

led=5
sensor_value=[]

if __name__ == '__main__':

    while True:
        button.when_pressed = sound_sensor.on
        while True:
            sensor_value.appened(grovepi.analogRead(sound_sensor))
            if button.when_released:
                sound_sensor.off
                break   
        
        pause()
