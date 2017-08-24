from scipy.io import wavfile
import numpy as np

#audio we are going to test
filename = "audios/Für Elise (original).wav"
noisyFileName = "noisy.wav"
#can we read it?
fs, data = wavfile.read(filename)
assert (fs == 44100)
print(abs(data))
dataNoisy = data + np.random.standard_normal((len(data),2))

wavfile.write(noisyFileName, fs, dataNoisy)
#
print(data - dataNoisy)