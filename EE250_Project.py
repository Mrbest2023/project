import grovepi
from grovepi import *
from grove_rgb_lcd import *
import time

button = 3
flag=1

sound_sensor=0
grovepi.pinMode(sound_sensor, "INPUT")
grovepi.pinMode(button,"INPUT")

led=5
sensor_value=[]

if __name__ == '__main__':
    while True:
        if grovepi.digitalRead(button) == 1:
            sensor_value.appened(grovepi.analogRead(sound_sensor))
            flag=0
        else:
            if flag==0:
                #Analyze
                flag=1

        #print to led
