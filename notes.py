from scipy import fft, arange
import numpy as np
import os
import time 
from statistics import mean



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

    #grab the sample slice and perform FFT on it
    x = np.fft.fft(x)/n
    
    return frqarr, abs(x)

def note(freq):
    print("freq ", freq)
    ave = mean(freq)
    print (ave)
    if ave > 80 and ave < 86:
        return("E")
    if ave > 87 and ave < 93:
        return("F")
    if ave > 94 and ave < 103:
        return("G")
    if ave > 104 and ave < 115:
        return("A")
    if ave > 116 and ave < 124:
        return("B")
    if ave > 125 and ave < 138:
        return("C")
    if ave > 139 and ave < 155:
        return("D")
    if ave > 156 and ave < 174:
        return("E")
    else:
        return("OUT OF RANGE")
