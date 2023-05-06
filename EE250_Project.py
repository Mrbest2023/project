import grovepi
from grovepi import *
from grove_rgb_lcd import *
import time
import paho.mqtt.client as mqtt
import socket
import json
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import RPi.GPIO as GPIO
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.OUT)

print('Reading MCP3008 values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*range(8)))
print('-' * 57)


SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

def on_connect(client, userdata, flags, rc): 
    print("Connected to server "+str(rc)) 
    client.subscribe("btbest/type") 
    client.message_callback_add("btbest/type", on_message)

def on_message(client, userdata, msg): 
    print("Custom callback - Note: "+msg.payload.decode())
    note=str(msg)
    setText("Note: " + note)

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
            s = mcp.read_adc(i)
            #s = grovepi.analogRead(sound_sensor)
            if s>0:
                sensor_data.append(s)
                flag=0
        else:
            if flag==0:
                client.publish("btbest/sensor_data", json.dumps(sensor_data))
                time.sleep(1)
                flag=1