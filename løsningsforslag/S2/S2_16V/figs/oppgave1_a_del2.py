# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 13:16:53 2017

@author: Tommy O, for ENT3R 
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.unicode'] = True

years = [2, 4, 6, 8, 10, 12]
data = [197, 1888, 8950, 21530, 31440, 38350]
data = list(map(lambda a : a*100, data))

x = np.linspace(1, 15, num = 500)

def gp(x):
    return (576*np.exp(-0.68*x))/np.power(1 + 211*np.exp(-0.68*x), 2)



plt.figure(figsize=(8, 4))
plt.style.use('seaborn-ticks')
plt.rc('text', usetex = True)
#plt.xlabel(r'År etter 2000',fontsize=16)
#plt.ylabel(r'Antall artikler (millioner)',fontsize=16)
#plt.scatter(years, data, label='Datasett', s = 50)
plt.plot(x, gp(x), label = r"g'(x)", linewidth=1.5)
#plt.plot(x, Pd(x), label = r"P'(x)", linewidth=1)
plt.grid(True)
#plt.ylim([-150,900])
plt.legend(loc = 'best')
plt.savefig('{}.pdf'.format('oppgave1_b_del2'), bbox_inches='tight')
plt.show()


    