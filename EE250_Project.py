import grovepi
from grovepi import *
from grove_rgb_lcd import *
import time
import paho.mqtt.client as mqtt
import socket

def on_connect(client, userdata, flags, rc): 
    print("Connected to server (i.e., broker) with result code "+str(rc))

button = 3
flag=1
led=5
sound_sensor=0
grovepi.pinMode(sound_sensor, "INPUT")
grovepi.pinMode(button,"INPUT")

sensor_value=[]

if __name__ == '__main__': 
    client = mqtt.Client()
    client.loop_start()
    time.sleep(1)

    while True:
        if grovepi.digitalRead(button) == 1:
            sensor_value.appened(grovepi.analogRead(sound_sensor))
            flag=0
        else:
            if flag==0:
                client.publish(sensor_value)
                flag=1

        #print to led
