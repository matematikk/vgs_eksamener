# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 13:16:53 2017
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.unicode'] = True

def func1(x):
    return 64116.591*(1.025)**x

def func2(x):
    b = 4176
    r = 1.025
    return b * ((r**(x+1)-1)/(r-1))

def func3(x):
    b = 3525
    r = 1.025
    o = 1.02
    return b * sum(r**i * o**(x-i) for i in range(0, x+1))


start = 0
end = 25
func3 = np.vectorize(func3)

plt.figure(figsize=(8, 4))
x = np.arange(start, end+1)

plt.style.use('seaborn-ticks')
plt.rc('text', usetex = False)
lw = 1.5
plt.plot(x, func1(x), '-o', label='4a)', linewidth = lw, markersize = 4)
plt.plot(x, func2(x), '-o', label='4b)', linewidth = lw, markersize = 4)
plt.plot(x, func3(x), '-o', label='4c)', linewidth = lw, markersize = 4)

plt.grid(True)
plt.ylim([0,150000])
plt.legend(loc = 'best')
plt.savefig('{}.pdf'.format('oppgave4_plot2'), bbox_inches='tight')
plt.show()


    