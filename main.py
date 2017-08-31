from tools import functions as fn
from scikits.audiolab import wavread, wavwrite

originalArray, noisyArray, fs = fn.noiseMixer(10)
print "snr estimado: " + str(fn.snrCalculation(originalArray, noisyArray)) + " Db"


order = 6
cutoff = 500 # Hz

btt_filtered = fn.butter_lowpass_filter(originalArray + noisyArray, cutoff, fs, order)
print "fintered data snr: " + str(fn.snrCalculation(originalArray, btt_filtered))

wavwrite(btt_filtered, 'butterworth_lowpass.wav', fs)

wv_filtered = fn.wavelet(originalArray + noisyArray, cutoff, fs, order)
print "fintered data snr: " + str(fn.snrCalculation(originalArray, wv_filtered))

wavwrite(wv_filtered, "wavelet_filtered.wav", fs)
