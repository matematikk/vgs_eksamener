# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 13:16:53 2017
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.stats import norm, binom
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.unicode'] = True

x = np.linspace(200, 400, num = 2000)

mu = 308
sigma = 14.6

plt.figure(figsize=(8, 4))
plt.style.use('seaborn-ticks')
plt.rc('text', usetex = True)
plt.plot(x, norm.pdf(x, mu, sigma), label = 'normal(x, 308, 14.6)', linewidth=1.5)
x_2 = list(range(0,1000,3))
plt.plot(x_2, binom.pmf(x_2, 1000, 0.308), 'o', label = 'binom(x, 1000, 0.308)', linewidth=1.5, markersize = 6)
#plt.plot(x, Pd(x), label = r"P'(x)", linewidth=1)
plt.grid(True)
plt.xlim([mu-50,mu+50])
plt.legend(loc = 'best')
plt.savefig('{}.pdf'.format('oppgave3_plot'), bbox_inches='tight')
plt.show()


    