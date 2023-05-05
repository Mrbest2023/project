import grovepi
from grovepi import *
from grove_rgb_lcd import *
import time
import paho.mqtt.client as mqtt
import socket


def on_connect(client, userdata, flags, rc): 
    print("Connected to server "+str(rc)) 
    client.subscribe("btbest/type") 
    client.message_callback_add("btbest/type", on_message)

def on_message(client, userdata, msg): 
    print("Custom callback - Note: "+msg.payload.decode())
    note=str(msg)
    SetText("Note: " + note)

#def recieving(strng): 
   # printing_variable = int(message.payload.decode()) 
    #print("custom callback - Note: "+str(note)) 



button = 3
flag=1

sound_sensor=0
grovepi.pinMode(sound_sensor, "INPUT")
grovepi.pinMode(button,"INPUT")

led=5
sensor_data=[]

if __name__ == '__main__': 
    

    while True:
        ip_address='68.181.32.115' 
        client = mqtt.Client() 
        client.on_connect = on_connect 
        client.on_message = on_message 
        client.connect(host="broker.hivemq.com", port=1883, keepalive=60)
        
        if grovepi.digitalRead(button) == 1:
            sensor_data.appened(grovepi.analogRead(sound_sensor))
            flag=0
        else:
            if flag==0:
                client.publish("btbest/sensor_data", sensor_data)
                flag=1