# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 13:16:53 2017
"""

import numpy as np
import matplotlib.pyplot as plt


def regr(i):
    return 5.37*i +525.2

x = list(range(50,301, 50))
K = [792,1065,1329,1601,1867,2136]

plt.style.use('seaborn-ticks')
plt.rc('text', usetex = True)
plt.scatter(x, K, label = 'Data', s = 40)
i = np.linspace(min(x), max(x), num = 500)
plt.plot(i, regr(i), label = 'Regresjon', linewidth=1.5)
plt.grid(True)
plt.legend(loc = 'best')
plt.show()
    