from tools import functions as fn
from scikits.audiolab import wavwrite

def main():
    originalArray, noisyArray, fs = fn.noisemixer(10)
    print 'snr original: ' + str(fn.snrcalculation(originalArray, noisyArray)) + ' Db'

    order = 2
    cutoff = 500  # Hz

    btt_filtered = fn.butter_lowpass_filter(originalArray + noisyArray, cutoff, fs, order)
    print 'filtered data snr: ' + str(fn.snrcalculation(originalArray, originalArray - btt_filtered))

    wavwrite(btt_filtered, 'butterworth_lowpass.wav', fs)

    wv_filtered = fn.wavelet(originalArray + noisyArray, cutoff, fs, order)
    print 'filtered data snr: ' + str(fn.snrcalculation(originalArray, originalArray - wv_filtered))

    wavwrite(wv_filtered, 'wavelet_filtered.wav', fs)


if __name__ == '__main__':
    main()
