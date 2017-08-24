from scipy.io import wavfile
import numpy as np

#make a noise audio with same length and sampling rate as the give one
filename = "audios/Fur Elise (original).wav"
noisyFileName = "noise.wav"

fs, data = wavfile.read(filename)
assert (fs == 44100)

dataNoisy = np.random.normal(1, 1, len(data.T[0]))
wavfile.write(noisyFileName, fs, dataNoisy)

