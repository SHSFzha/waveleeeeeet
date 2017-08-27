from tools import functions

originalArray, noisyArray = functions.noiseMixer(0)
print "snr estimado: " + str(functions.snrCalculation(originalArray, noisyArray)) + " db"
