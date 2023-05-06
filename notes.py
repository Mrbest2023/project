from scipy import fft, arange
import numpy as np
import os
import time 
from typing import Iterable
from statistics import mean

MAX_FRQ = 200
SLICE_SIZE = 0.15 #seconds
WINDOW_SIZE = 0.25 #seconds



def get_max_frq(frq: Iterable[float], fft: Iterable[float]) -> float:
    """Returns the frequency with the highest amplitude in the given FFT array.

    Works by iterating through the FFT array and comparing the current amplitude
    to the maximum amplitude. If the current amplitude is greater than the
    maximum amplitude, the current frequency is saved as the maximum frequency
    and the current amplitude is saved as the maximum amplitude.
    
    Args:
        frq (Iterable[float]): The frequency array (x-axis in plots)
        fft (Iterable[float]): The FFT array (y-axis in plots)

    Returns:
        float: The frequency with the highest amplitude in the given FFT array
    """
    max_frq = 0
    max_fft = 0
    for idx in range(len(fft)):
        if abs(fft[idx]) > max_fft:
            max_fft = abs(fft[idx])
            max_frq = frq[idx]
    return max_frq

def get_peak_frqs(frq, fft):
    """Returns the two frequencies with the highest amplitudes in the given FFT array.
    
    Works by splitting the FFT array into two arrays, one for the lower frequencies
    and one for the higher frequencies. Then, it finds the frequency with the
    highest amplitude in each array and returns them as a tuple.

    Args:
        frq (Iterable[float]): The frequency array (x-axis in plots)
        fft (Iterable[float]): The FFT array (y-axis in plots)

    Returns:
        tuple: A tuple containing the two frequencies with the highest amplitudes in the given FFT array
    """
    #TODO: implement an algorithm to find the two maximum values in a given array
    
    #get the high and low frequency by splitting it in the middle (1000Hz)

    

    #spliting the FFT to high and low frequencies

    low_frq_fft = fft[frq<1000]
    high_frq_fft = fft[frq>1000]
    
    low_frq = frq[frq<1000]
    high_frq = frq[frq>1000]
    
    
    
    return (get_max_frq(low_frq, low_frq_fft), get_max_frq(high_frq, high_frq_fft))



def frequency_spectrum(x, sf):
    """
    Derive frequency spectrum of a signal from time domain
    :param x: signal in the time domain
    :param sf: sampling frequency
    :returns frequencies and their content distribution
    """



    
    sample_rate = sf
    samples = x




    slice_sample_size = int(SLICE_SIZE*sample_rate)   #get the number of elements expected for [SLICE_SIZE] seconds

    n = slice_sample_size                            #n is the number of elements in the slice

    #generating the frequency spectrum
    k = np.arange(n)                                #k is an array from 0 to [n] with a step of 1
    slice_duration = n/sample_rate                   #slice_duration is the length of time the sample slice is (seconds)
    frq = k/slice_duration                          #generate the frequencies by dividing every element of k by slice_duration

    max_frq_idx = int(MAX_FRQ*slice_duration)       #get the index of the maximum frequency (2000)
    frq = frq[range(max_frq_idx)]                   #truncate the frequency array so it goes from 0 to 2000 Hz


    start_index = 0                                 #set the starting index at 0
    end_index = start_index + slice_sample_size      #find the ending index for the slice
    output = ''

    print()
    i = 1
    lower=(0, 0)
    upper=(0, 0)
    print ("samples length: ", len(samples), " end index: ", end_index)
    #while end_index < len(samples):
        #print("Sample {}:".format(i), end=' ')
        #i += 1

    sample_slice = samples[start_index:end_index] # get the sample slice

        #TODO: grab the sample slice and perform FFT on it
    sample_slice_fft = np.fft.fft(sample_slice)/n

        #TODO: truncate the FFT to 0 to 2000 Hz
    sample_slice_fft = sample_slice_fft[range(max_frq_idx)]
        
        #TODO: calculate the locations of the upper and lower FFT peak using get_peak_frqs()
    (lower, upper) = get_peak_frqs(frq, sample_slice_fft)
    print("CHECKPOINT")
    """
    #x = x - np.average(x)  # zero-centering

    n = len(x)
    k = arange(n)
    tarr = n / float(sf)
    frqarr = k / float(tarr)  # two sides frequency range

    frqarr = frqarr[range(n // 2)]  # one side frequency range

    #grab the sample slice and perform FFT on it
    x = np.fft.fft(x)/n
    """
    #return frqarr, abs(x)
    hi = (mean(lower) + mean(upper))/2
    return hi

def note(freq):
    print("freq ", freq)
    #ave = max(freq)
    #print (ave)
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
