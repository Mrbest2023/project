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

sound_sensor=0
grovepi.pinMode(sound_sensor, "INPUT")
grovepi.pinMode(button,"INPUT")

led=5
sensor_value=[]

if __name__ == '__main__': 
  
    while True:
        #subscribe
        client = mqtt.Client()
        client.on_message = on_message
        client.on_connect = on_connect
        client.connect(host="68.181.32.115", port=11000, keepalive=60)
    

        #publish
        ip_address='68.181.32.115' 
        client = mqtt.Client()
        time.sleep(1)
        
        if grovepi.digitalRead(button) == 1:
            sensor_value.appened(grovepi.analogRead(sound_sensor))
            flag=0
        else:
            if flag==0:
                client.publish(sensor_value)
                flag=1

        #print to led
        note=str(printing_variable)
        setText("Note: " + note)
