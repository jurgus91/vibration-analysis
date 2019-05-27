# -*- coding: utf-8 -*-
"""
Created on Thu May 23 18:45:01 2019

@author: Admin
"""

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

from scipy.fftpack import fft

vibro = pd.read_csv(r"C:\Users\Admin\Documents\gears vibro\points.csv")

vibro

A = vibro
Fs = int(5120)
n = len(A)
ff= Fs/n

k = 1/Fs
s = (n-1)*k
t = np.arange(0, s, k)


x = vibro.loc[:,['k1']]
y = vibro.loc[:,['k2']]
z = vibro.loc[:,['k3']]
zn = vibro.loc[:,['k4']]
plt.plot(t,x)
plt.show()

X = fft(x)
XX = 2/n * np.abs(X[1:np.int(n/2)])
print(XX)
f = Fs/n*np.linspace(0,1.0/(2.0*k),n/2-1)
#f = np.linspace(0.0,1.0/(2*k),n/2) 
plt.plot(f,XX)

