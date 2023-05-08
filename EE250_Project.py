import grovepi
from grovepi import *
from grove_rgb_lcd import *
import time
import paho.mqtt.client as mqtt
import socket
import json
from grove_rgb_lcd import *
from pydub import AudioSegment
import argparse 
import pathlib

grove_vcc=5


def on_connect(client, userdata, flags, rc): 
    print("Connected to server "+str(rc)) 
    client.subscribe("btbest/type") 
    client.message_callback_add("btbest/type", on_message)

def on_message(client, userdata, msg): 
    print("Custom callback - Note: "+msg.payload.decode())
    note=str(msg)
    grove_rgb_lcd.setText("Note: " + note)
    print("It works")
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


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Analyze an audio file")
    parser.add_argument("file", type=pathlib.Path, help="The file to analyze")
    parser.add_argument("start_time", type=float, help="The start time of the slice to analyze")
    parser.add_argument("-o", "--output", help="The output file to save the plot to")
    return parser

parser = get_parser()
args = parser.parse_args()

audio = AudioSegment.from_mp3(args.file)
samples = audio.get_array_of_samples()

if __name__ == '__main__': 
    
    ip_address='68.181.32.115' 
    client = mqtt.Client() 
    client.on_connect = on_connect 
    client.on_message = on_message 
    client.connect(host="broker.hivemq.com", port=1883, keepalive=60)
    while True:
        if grovepi.digitalRead(button) == 1:
            #s = grovepi.analogRead(sound_sensor) #Would be used with a microphone
            """if s>0:
                #sensor_data.append(s)"""
            flag=0
        else:
            if flag==0:
                samples_=1
                client.publish("btbest/sensor_data", json.dumps(samples_))
                time.sleep(1)
                flag=1
        #client.loop.forever()
        