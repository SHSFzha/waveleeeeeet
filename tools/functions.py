import numpy as np

def snrCalculation(original, noise):
    avgPower1 = 0
    avgPower2 = 0
    for i in original:
        avgPower1 += i ** 2
    for i in noise:
        avgPower2 += i ** 2
    snr = np.log10(avgPower1 / len(original) / (avgPower2 / len(noise)))

    print "SNR estimado: " + str(10 * snr)


