import paho.mqtt.client as mqtt 
import socket 
import time
from notes import frequency_spectrum, note
import json
import pathlib
from pydub import AudioSegment
import argparse 

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

def on_connect(client, userdata, flags, rc): 
    print("Connected to server "+str(rc)) 
    client.subscribe("btbest/sensor_data") 
    client.message_callback_add("btbest/sensor_data", on_message_from_pong)

"""This function is the default callback for messages receieved"""
def on_message(client, userdata, msg): 
    print("default callback - topic: " + msg.topi + " msg: " + str(msg.payload, "utf-8"))

def on_message_from_pong(client, userdata, message): 
   print("Custom callback - sensor_data: "+message.payload.decode())
   var=samples     #json.loads(message.payload.decode()) 
   sr = audio.frame_rate
   abc=frequency_spectrum(var, sr)
   
   type=note(abc)
   print(type)
   client.publish("btbest/Note", type)


if __name__ == '__main__':

    client = mqtt.Client() 
    client.on_connect = on_connect 
    client.on_message = on_message 
    client.connect(host="broker.hivemq.com", port=1883, keepalive=60)
    client.loop_forever()