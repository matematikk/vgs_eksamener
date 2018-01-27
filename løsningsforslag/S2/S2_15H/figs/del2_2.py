# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 13:16:53 2017

@author: Tommy O, for ENT3R 
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt


menn_aar = [9,13,20,35,60,70,88]
menn_tider = [4.38, 4.51, 4.61, 4.81, 5.2, 5.43, 5.55]

kvinner_aar = [63,67,70,73,75,79,85]
kvinner_tider = [3.24, 3.75, 3.85, 4.22, 4.44, 4.77, 4.98]

def func(x, a, b):
    return x*a + b

plt.figure(figsize=(5.75, 2.75))
plt.style.use('seaborn-ticks')
plt.rc('text', usetex = True)
markersize = 35
    
funcargs, _ = opt.curve_fit(func, menn_aar, menn_tider)   
funcargs = tuple(funcargs)
x = np.linspace(min(menn_aar + kvinner_aar), max(menn_aar + kvinner_aar)+20)
plt.subplot(1,1,1)
plt.scatter(menn_aar, menn_tider, label=r'Data menn', s = markersize, edgecolor = 'k')
plt.plot(x, func(x, *funcargs), '--', label=r'Modell menn')

funcargs, _ = opt.curve_fit(func, kvinner_aar, kvinner_tider)   
funcargs = tuple(funcargs)
plt.scatter(kvinner_aar, kvinner_tider, label=r'Data kvinner', s = markersize, edgecolor = 'k')
plt.plot(x, func(x, *funcargs), '--', label=r'Modell kvinner')

plt.legend(loc = 'best')
plt.grid(True)
plt.tight_layout()
#plt.savefig('del2_2_modeller.pdf')
plt.show()
    