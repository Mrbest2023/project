import grovepi
from grovepi import *
from grove_rgb_lcd import *
import time
import paho.mqtt.client as mqtt
import socket
from scipy import fft, arange
import numpy as np
import os
import time 



def frequency_spectrum(x, sf):
    """
    Derive frequency spectrum of a signal from time domain
    :param x: signal in the time domain
    :param sf: sampling frequency
    :returns frequencies and their content distribution
    """
    x = x - np.average(x)  # zero-centering

    n = len(x)
    k = arange(n)
    tarr = n / float(sf)
    frqarr = k / float(tarr)  # two sides frequency range

    frqarr = frqarr[range(n // 2)]  # one side frequency range

    x = fft(x) / n  # fft computing and normalization
    x = x[range(n // 2)]

    return frqarr, abs(x)


def note(freq):
    if freq > 80 and freq < 86:
        return("E")
    if freq > 87 and freq < 93:
        return("F")
    if freq > 94 and freq < 103:
        return("G")
    if freq > 104 and freq < 115:
        return("A")
    if freq > 116 and freq < 124:
        return("B")
    if freq > 125 and freq < 138:
        return("C")
    if freq > 139 and freq < 155:
        return("D")
    if freq > 156 and freq < 174:
        return("E")
    else:
        return("OUT OF RANGE")

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
    ip_address='68.181.32.115' 
    client = mqtt.Client()
    client.loop_start()
    time.sleep(1)

    while True:
        
        if grovepi.digitalRead(button) == 1:
            sensor_value.appened(grovepi.analogRead(sound_sensor))
            flag=0
        else:
            if flag==0:
                sr=32
                frequency,X=frequency_spectrum(sensor_value, sr)
                type=note(frequency)
                client.publish(type)
                
                flag=1

        #print to led
