# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 13:16:53 2017
"""

import numpy as np
import matplotlib.pyplot as plt
import random
import itertools

def average(iterable):
    for i, e in enumerate(itertools.accumulate(iterable)):
        yield e / (i+1)

def play(a):
    """
    Returns profits for casino.
    """
    dice_sum = sum(random.randint(1,6) for i in range(2))
    if dice_sum == 10:
        return a - 200
    if dice_sum == 7:
        return a - 50
    return a


casino_profits = [play(30) for i in range(2000)]
casino_cumsum = list(itertools.accumulate(casino_profits))
casino_avg = list(average(casino_profits))

plt.figure(figsize=(5.75, 4.25))
plt.style.use('seaborn-ticks')
plt.rc('text', usetex = True)

plt.subplot(3,1,1)
x = np.linspace(-5,3, num = 500)
plt.plot(casino_profits, 'o', label = r'Profitt per spill', markersize = 0.5)
plt.grid(True)
plt.legend(loc = 'best')
print(set(casino_profits))

plt.subplot(3,1,2)
plt.plot(casino_cumsum, label = r"Total profitt", linewidth=1.5)
plt.grid(True)
plt.legend(loc = 'best')

plt.subplot(3,1,3)
plt.plot(casino_avg, '.', label = r"Gjennomsnittlig profitt", linewidth=1.5, markersize = 1)
plt.ylim([0,10])
plt.grid(True)
plt.legend(loc = 'best')

plt.tight_layout()
#plt.savefig('del1_8_plot.pdf')
plt.show()
        