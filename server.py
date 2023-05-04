import paho.mqtt.client as mqtt 
from notes import frequency_spectrum, note


def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("btbest/sensor_value")

    client.message_callback_add("btbest/sensor_value", send)

def send(data):
    sr=32
    freq=frequency_spectrum(data, sr)
    type=note(freq)
    client.publish(type)

def on_message(client, userdata, msg): 
    print("Default callback - topic: " + msg.topic + " msg: " + str(msg.payload, "utf-8"))

if __name__ == '__main__':

    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="68.181.32.115", port=11000, keepalive=60)
    client.loop_forever()
