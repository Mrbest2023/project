from EE250_Project import main 
from notes import frequency_spectrum, note
import paho.mqtt.client as mqtt 
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe()
    client.subscribe("btbest/date")
    client.subscribe("btbest/time")

    client.message_callback_add("btbest/ipinfo", on_message_from_ipinfo)
    client.message_callback_add("btbest/date", on_message_from_date)
    client.message_callback_add("btbest/time", on_message_from_time)
def on_message(client, userdata, msg): 
    print("Default callback - topic: " + msg.topic + " msg: " + str(msg.payload, "utf-8"))

def on_message_from_ipinfo(client, userdata, message): print("Custom callback - IP Message: "+message.payload.decode()) 
def on_message_from_date(client, userdata, message): 
    print("custom callback - Date: "+message.payload.decode()) 
def on_message_from_time(client, userdata, message): 
    print("custom callback - Time: "+message.payload.decode())

if name == 'main':

    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="68.181.32.115", port=11000, keepalive=60)
    client.loop_forever()

        sr=32
        frequency,X=frequency_spectrum(sensor_value, sr)
        type=note(frequency)