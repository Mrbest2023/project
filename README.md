# project

Team Memebers
1. Brendan Best
2. Marina Braga

To execute our program first run the server.py file on your computer. Then run the EE250_Project.py on your rpi. With both programs running our project should be good to go. Just push the button to record your sound and begin.

import paho.mqtt.client as mqtt 
import socket 
import json
import pathlib
from pydub import AudioSegment
import argparse 
import grovepi
from grovepi import *
from grove_rgb_lcd import *
import time
import paho.mqtt.client as mqtt
import socket
from grove_rgb_lcd import *
from pydub import AudioSegment
import argparse 
import pathlib
from scipy import fft, arange
import numpy as np
import os
import time 
from typing import Iterable
from statistics import mean
