from scipy.io import wavfile

filename = "audios/Für Elise (original).wav"

fs, data = wavfile.read(filename)
