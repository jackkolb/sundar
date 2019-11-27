# performs an FFT

import numpy as np
import numpy.fft as npfft
import pylab
import matplotlib.pyplot as plt
import math

# reads file
data = []
x = []
y = []
filen = input("File to Analyze")
with open(filen, "r") as data_file:
    while True:
        entry = data_file.readline().split(",")       
        if entry == ['']:
            break
        data.append([int(entry[0]), int(entry[1])])
        x.append(int(entry[0]))
        y.append(int(entry[1]))

# determine average timestamp spacing
spacing = sum([x[i+1] - x[i] for i in range(len(x))[:-1]]) / len(x)
spacing = spacing / 1000000

# number of points
N = len(x)

# generate fft from y (acceleration)
yf = npfft.fft(y)

# make linear spacing along x
xf = np.linspace(1.0, 1.0/(2.0*spacing), int(N/2))

plt.subplot(1, 1, 1)
plt.plot(xf[1:], 2.0/N * np.abs(yf[0:int(N/2)])[1:])

plt.show()
