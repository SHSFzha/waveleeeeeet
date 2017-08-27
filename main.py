from scikits.audiolab import wavread, wavwrite
from tools import functions

data2, fs2, enc2 = wavread("audios/noise.waf")
data1, fs1, enc1 = wavread("audios/Fur Elise (original).wav")

#both tracks must have same encoding and sampling frequency
assert fs1 == fs2
assert enc1 == enc2

#write the ruslt do an other audio file
originalArray = 1 * data1.T[0] #just to scale the arrays faster
noisyArray = 1 * data2

result = originalArray + noisyArray
wavwrite(result, 'result.wav', fs=fs1)

functions.snrCalculation(originalArray, noisyArray)
