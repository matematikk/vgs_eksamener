# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 13:16:53 2017
"""

import numpy as np
import matplotlib.pyplot as plt

def O(p):
    return -p**3 + 5.37*p**2 + 341*p - 2356

p = np.linspace(6, 18, num = 500)

plt.style.use('seaborn-ticks')
plt.rc('text', usetex = True)
plt.plot(p, O(p), label = 'O(p)', linewidth=1.5)
plt.grid(True)
plt.ylim([-150, 900])
plt.legend(loc = 'best')
plt.show()
    