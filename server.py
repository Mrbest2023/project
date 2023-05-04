import paho.mqtt.client as mqtt 
from notes import frequency_spectrum, note


def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("btbest/sensor_value")

    client.message_callback_add("btbest/sensor_value", on_message_from_ipinfo)

def on_message(client, userdata, msg): 
    print("Default callback - topic: " + msg.topic + " msg: " + str(msg.payload, "utf-8"))

def on_message_from_ipinfo(client, userdata, message):
    print("Custom callback - Sensor_value: "+message.payload.decode()) 
if __name__ == '__main__':

    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="68.181.32.115", port=11000, keepalive=60)
    client.loop_forever()