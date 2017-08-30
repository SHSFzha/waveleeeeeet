import numpy as np
from scikits.audiolab import wavread, wavwrite

def noiseMixer(outputSnr):
    # both tracks must have same encoding and sampling frequency
    data2, fs2, enc2 = wavread("audios/noise.waf")
    data1, fs1, enc1 = wavread("audios/Fur Elise (original).wav")
    assert fs1 == fs2
    assert enc1 == enc2

    # write the result do an other audio file
    # just to scale the arrays faster
    originalArray = 1 * data1.T[0]  # this one has two channels, I'm taking just the first

    if outputSnr == 10:
        noisyArray = 0.015 * data2
    elif outputSnr == 0:
        noisyArray = 0.0475 * data2
    elif outputSnr == -10:
        noisyArray = 0.15 * data2
    else:
        raise ValueError('Unexpected value passed')

    result = originalArray + noisyArray
    wavwrite(result, 'result.wav', fs=fs1)

    return originalArray, noisyArray

def snrCalculation(original, noise):
    avgPower1 = 0
    avgPower2 = 0
    for i in original:
        avgPower1 += i ** 2
    for i in noise:
        avgPower2 += i ** 2

    return 10 * np.log10(avgPower1 / len(original) / (avgPower2 / len(noise)))

def butterWorth():
    pass

def wavelet():
    pass



