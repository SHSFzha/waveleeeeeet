from tools import functions as fn
from scikits.audiolab import wavwrite
from matplotlib import pyplot as plt
from numpy import fft

def main():
    originalArray, noisyArray, fs = fn.noisemixer(0)
    print 'snr original: ' + str(fn.snrcalculation(originalArray, noisyArray)) + ' Db'

    order = 2
    butterworthcutoff = 700  # Hz
    walevetcutoff = 11025

    btt_filtered = fn.butter_lowpass_filter(originalArray + noisyArray, butterworthcutoff, fs, order)
    print 'butterworth filtered data snr: ' + str(fn.snrcalculation(originalArray, originalArray - btt_filtered))

    wavwrite(btt_filtered, 'butterworth_lowpass.wav', fs)

    wv_filtered = fn.wavelet(originalArray + noisyArray, walevetcutoff, fs, order)
    print 'wavelet filtered data snr: ' + str(fn.snrcalculation(originalArray, originalArray - wv_filtered))

    plt.plot(fft.fft(abs(wv_filtered)))
    plt.show()
if __name__ == '__main__':
    main()
