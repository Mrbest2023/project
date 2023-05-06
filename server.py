import paho.mqtt.client as mqtt 
import socket 
import time
from notes import frequency_spectrum, note
import json


def on_connect(client, userdata, flags, rc): 
    print("Connected to server "+str(rc)) 
    client.subscribe("btbest/sensor_data") 
    client.message_callback_add("btbest/sensor_data", on_message_from_pong)

"""This function is the default callback for messages receieved"""
def on_message(client, userdata, msg): 
    print("default callback - topic: " + msg.topi + " msg: " + str(msg.payload, "utf-8"))

def on_message_from_pong(client, userdata, message): 
   print("Custom callback - sensor_data: "+message.payload.decode())
   var=json.loads(message.payload.decode())
   sr=2000
   abc=frequency_spectrum(var, sr)
   
   type=note(abc)
   print("type ")
   print(type)
   client.publish("btbest/Note", type)


if __name__ == '__main__':

    client = mqtt.Client() 
    client.on_connect = on_connect 
    client.on_message = on_message 
    client.connect(host="broker.hivemq.com", port=1883, keepalive=60)
    client.loop_forever()