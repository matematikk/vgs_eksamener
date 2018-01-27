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

x = np.linspace(5, 250, num = 2000)

def K(x):
    a =  3/20
    b = 11
    c = 2300
    return a*x*x + b*x + c

def I(x):
    return 3200 * np.log(2.5*x + 1)

def O(x):
    return I(x) - K(x)



plt.figure(figsize=(8, 4))
plt.style.use('seaborn-ticks')
plt.rc('text', usetex = True)
plt.xlabel(r'Enheter produsert',fontsize=16)
plt.ylabel(r'Kroner',fontsize=16)
#plt.scatter(years, data, label='Datasett', s = 50)
plt.plot(x, O(x), label = r"Overskudd(x)", linewidth=1.5)
#plt.plot(x, Pd(x), label = r"P'(x)", linewidth=1)
plt.grid(True)
#plt.ylim([-150,900])
plt.legend(loc = 'best')
plt.savefig('{}.pdf'.format('oppgave2_c'), bbox_inches='tight')
plt.show()


    