# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 13:16:53 2017

@author: Tommy O, for ENT3R 
"""

import numpy as np
import matplotlib.pyplot as plt
import random
import itertools

r = 1.1
S = 50
u = 8
cash = [50]
while cash[-1] > 0:
    ny = cash[-1]*r - u
    cash.append(ny)
    



plt.figure(figsize=(5.75, 2.25))
plt.style.use('seaborn-ticks')
plt.rc('text', usetex = True)

plt.subplot(1,1,1)
x = np.linspace(-5,3, num = 500)
plt.plot(cash, '-o', label = r'Beholdning i fond', markersize = 3)
plt.grid(True)
plt.legend(loc = 'best')


plt.tight_layout()
#plt.savefig('del2_3_plot.pdf')
plt.show()
        