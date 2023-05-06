import grovepi
from grovepi import *
from grove_rgb_lcd import *
import time
import paho.mqtt.client as mqtt
import socket
import json
from grove_rgb_lcd import *
from pydub import AudioSegment


audio = AudioSegment.from_mp3(Marinas_voice)
samples = audio.get_array_of_samples()

def on_connect(client, userdata, flags, rc): 
    print("Connected to server "+str(rc)) 
    client.subscribe("btbest/type") 
    client.message_callback_add("btbest/type", on_message)

def on_message(client, userdata, msg): 
    print("Custom callback - Note: "+msg.payload.decode())
    note=str(msg)
    setText("Note: " + note)
    time.sleep(1)

#def recieving(strng): 
   # printing_variable = int(message.payload.decode()) 
    #print("custom callback - Note: "+str(note)) 



button = 3
flag=1

sound_sensor=0 #PORT A0
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
            #s = grovepi.analogRead(sound_sensor) #Would be used with a microphone
            if s>0:
                #sensor_data.append(s)
                flag=0
        else:
            if flag==0:
                client.publish("btbest/sensor_data", json.dumps(samples))
                time.sleep(1)
                flag=1