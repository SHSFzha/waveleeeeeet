from scikits.audiolab import wavread, wavwrite

data2, fs2, enc2 = wavread("audios/noise.waf")
data1, fs1, enc1 = wavread("audios/Fur Elise (original).wav")

#here we just mix up the original wave and the noise
assert fs1 == fs2
assert enc1 == enc2
result = 1 * data1.T[0] + 1 * data2
wavwrite(result, 'result.wav', fs=44100)
