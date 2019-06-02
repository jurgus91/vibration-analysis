
import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

from scipy.fftpack import fft

#import data from test
vibro = pd.read_csv(r"C:\Users\Admin\Documents\gears vibro\points.csv")


A = vibro
Fs = int(5120)
n = len(A)
k = 1/Fs
s = (n-1)*k
t = np.arange(0, s, k)

#reading values of acceleration from test
x = vibro['k1']
y = vibro['k2']
z = vibro['k3']
zn = vibro['k4']

#Vibration acceleration in time for X , Y, Z - axis
plt.plot(t,x)
plt.title('Vibration acceleration in time X - axis')
plt.xlabel('Time [s]')
plt.ylabel('Acceleration m/s^2')
plt.show()

plt.plot(t,y)
plt.title('Vibration acceleration in time Y - axis')
plt.xlabel('Time [s]')
plt.ylabel('Acceleration m/s^2')
plt.show()

plt.plot(t,z)
plt.title('Vibration acceleration in time Z - axis')
plt.xlabel('Time [s]')
plt.ylabel('Acceleration m/s^2')
plt.show()

#Transformation from vibration acceleration to amplitude of vibrations
X = fft(x)/n
XX = 2 * np.abs( X[0 : int( np.ceil( n / 2 ))])
Y = fft(y)/n
YY = 2 * np.abs( Y[0 : int( np.ceil( n / 2 ))])
Z = fft(z)/n
ZZ = 2 * np.abs( Z[0 : int( np.ceil( n / 2 ))])

#Tansformation from time to frequency using FFT
f = Fs/2 * np.linspace(0, 1.0, int( np.ceil( n / 2 )))

plt.figure(1)
plt.subplot(211)
plt.plot(f,XX)
plt.title('Vibration acceleration in frequency')

plt.subplot(212)
plt.plot(f,YY,'red')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Acceleration m/s^2')
plt.show()

plt.plot(f,ZZ,'red')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Acceleration m/s^2')
plt.show()
