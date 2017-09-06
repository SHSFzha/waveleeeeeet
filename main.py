from tools import functions as fn
from scikits.audiolab import wavwrite
from matplotlib import pyplot as plt
from numpy import fft

def main():
    originalArray, noisyArray, fs = fn.noisemixer(10)
    print 'snr original: ' + str(fn.snrcalculation(originalArray, noisyArray)) + ' Db'

    order = 5
    butterworthcutoff = 700  # Hz
    walevetcutoff = 11025

    btt_filtered = fn.butter_lowpass_filter(originalArray + noisyArray, butterworthcutoff, fs, order)
    print 'butterworth filtered data snr: ' + str(fn.snrcalculation(originalArray, originalArray - btt_filtered))

    wavwrite(btt_filtered, 'butterworth_lowpass.wav', fs)

    wv_filtered = fn.wavelet_hard(originalArray + noisyArray, walevetcutoff, fs, order)
    print 'wavelet_hard filtered data snr: ' + str(fn.snrcalculation(originalArray, originalArray - wv_filtered))
    wavwrite(wv_filtered, 'wavelet_hard.wav', fs)

    plt.figure(0)
    plt.plot(abs(fft.fft(originalArray + noisyArray)))

    plt.figure(1)
    plt.plot(abs(fft.fft(wv_filtered)))

    plt.figure(2)
    plt.plot(abs(fft.fft(btt_filtered)))

    plt.figure(3)
    plt.plot(abs(fft.fft(originalArray)))
    plt.show()


if __name__ == '__main__':
    main()
