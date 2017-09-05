import numpy as np
from scikits.audiolab import wavread, wavwrite
from scipy.signal import butter, filtfilt
from scipy.stats import threshold


def noisemixer(outputSnr):
    # both tracks must have same encoding and sampling frequency
    data2, fs2, enc2 = wavread('audios/noise.waf')
    data1, fs1, enc1 = wavread('audios/Fur Elise (original).wav')
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

    return originalArray, noisyArray, fs1


def snrcalculation(original, noise):
    avgPower1 = 0
    avgPower2 = 0
    for i in original:
        avgPower1 += i ** 2
    for i in noise:
        avgPower2 += i ** 2

    return 10 * np.log10(avgPower1 / len(original) / (avgPower2 / len(noise)))


def butter_lowpass(cutoff, fs, order=5, ftype='low'):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype=ftype, analog=False)
    return b, a


def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order , ftype='low')
    y = filtfilt(b, a, data)
    return y


def wavelet(data, cutoff, fs, order=5):
    # definir filtros

    # passa altas
    Hb, Ha = butter_lowpass(cutoff, fs, order=order, ftype='high')
    # passa baixas
    Lb, La = butter_lowpass(cutoff, fs, order=order, ftype='low')

    scale = 0
    iterate = True

    H = filtfilt(Hb, Ha, data)
    L = filtfilt(Lb, La, data)

    filtered = threshold(L, threshmin=np.sqrt(2 * np.log(len(H)) * np.std(H)) / 200)
    while iterate:
        H = filtfilt(Hb, Ha, np.delete(H, np.s_[::2], 0), padlen=0)
        L = filtfilt(Lb, La, np.delete(H, np.s_[::2], 0), padlen=0)

        H = threshold(H, threshmin=np.sqrt(2 * np.log(len(H)) * np.std(H)) / 200)
        scale = scale + 2
        for i in range(len(H)):
            if (i%scale == 0):
                filtered[i] += L[i / scale]
        if len(L) <= 1:
            iterate = False

    return filtered
