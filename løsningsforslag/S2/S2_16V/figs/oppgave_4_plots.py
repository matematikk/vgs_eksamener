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
    b = 4358.06
    r = 1.025
    if x < 18:
        return b * ((r**(x+1)-1)/(r-1))
    else:
        return func2(x-1)*r

def func3(x):
    b = 3725.01
    r = 1.025
    o = 1.02
    if x < 18:
        return b * sum(r**i * o**(x-i) for i in range(0, x+1))
    else:
        return func3(x-1)*r


start = 0
end = 18

plt.figure(figsize=(8/1.25, 4/1.25))
x = np.arange(start, end+1)

plt.style.use('seaborn-ticks')
plt.rc('text', usetex = False)
lw = 1.5
plt.plot(x, [func1(k) for k in x], '-o', label='4a)', linewidth = lw, markersize = 5, markeredgecolor='k')
plt.plot(x, [func2(k) for k in x], '-o', label='4b)', linewidth = lw, markersize = 5, markeredgecolor='k')
plt.plot(x, [func3(k) for k in x], '-o', label='4c)', linewidth = lw, markersize = 5, markeredgecolor='k')

plt.grid(True)
plt.ylim([0, 120000])
plt.legend(loc = 'best')
plt.xticks(x)
plt.savefig('{}.pdf'.format('oppgave4_plot2'), bbox_inches='tight')
plt.show()


    