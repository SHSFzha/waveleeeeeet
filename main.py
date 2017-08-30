from tools import functions as fn

originalArray, noisyArray = fn.noiseMixer(10)
print "snr estimado: " + str(fn.snrCalculation(originalArray, noisyArray)) + " Db"
