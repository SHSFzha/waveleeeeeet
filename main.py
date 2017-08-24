from scipy.io import wavfile

#audio we are going to test
filename = "audios/Für Elise (original).wav"

#can we read it?
fs, data = wavfile.read(filename)

assert (fs == 44100)