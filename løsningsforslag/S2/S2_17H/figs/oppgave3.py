# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 13:16:53 2017

@author: Tommy O, for ENT3R 
"""

import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-3, 5, num = 500)

def f(x):
    return x**3 - 6*x**2 + 32


def f_deriv(x):
    return 3*x**2 - 12*x

def f_deriv2(x):
    return 6*x - 12

plt.style.use('seaborn-ticks')
plt.rc('text', usetex = True)
plt.plot(x, f(x), label = r'f(x)', linewidth = 2.5)
plt.plot(x, f_deriv(x), label = r"f'(x)", linewidth = 1.75)
plt.plot(x, f_deriv2(x), label = r"f''(x)", linewidth = 1)
plt.scatter([2], [16], label = 'Vendepunkt')
plt.grid(True)
plt.legend(loc = 'best')
plt.show()
    