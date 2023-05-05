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

    #grab the sample slice and perform FFT on it
    x = np.fft.fft(x)/n
    
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
