# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 13:16:53 2017
"""

import numpy as np
import matplotlib.pyplot as plt

def P(x):
    return x**3 - 6*x**2 + 32

def Pd(x):
    return 3*x**2 - 12*x

x = np.linspace(-3, 6, num = 500)

plt.style.use('seaborn-ticks')
plt.rc('text', usetex = True)
plt.plot(x, P(x), label = 'P(x)', linewidth=1.5)
plt.plot(x, Pd(x), label = r"P'(x)", linewidth=1)
plt.grid(True)
plt.legend(loc = 'best')
plt.show()
    