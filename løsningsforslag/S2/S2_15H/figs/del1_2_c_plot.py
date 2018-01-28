# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 13:16:53 2017
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 + 3*x**2 - 9*x

def f_p(x):
    return 3*x**2 + 6*x - 9

plt.figure(figsize=(5.75, 3.25))
plt.style.use('seaborn-ticks')
plt.rc('text', usetex = True)

plt.subplot(2,1,1)
x = np.linspace(-5,3, num = 500)
plt.plot(x, f(x), label = r'f(x)', linewidth=1.5)
plt.grid(True)
plt.legend(loc = 'best')

plt.subplot(2,1,2)
plt.plot(x, f_p(x), label = r"f'(x)", linewidth=1.5)
plt.grid(True)
plt.legend(loc = 'best')

plt.tight_layout()
#plt.savefig('del1_2c_plot.pdf')
plt.show()
    