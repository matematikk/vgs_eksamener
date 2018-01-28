# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 13:16:53 2017 
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.2, 0.1, 0.3, 0.3, 0.1])
final_dist = np.copy(x)

terms_in_sum1 = 1
for i in range(terms_in_sum1 - 1):
    final_dist = np.convolve(final_dist, x)
    final_dist = final_dist / np.sum(final_dist)

plt.style.use('seaborn-ticks')
plt.rc('text', usetex = False)
plt.plot(final_dist, 
         label = r'Sum av {} fuglekasser.'.format(terms_in_sum1), 
         linewidth = 2.5)
plt.grid(True)
plt.tight_layout()

terms_in_sum2 = 4 
for i in range(terms_in_sum2 - 1):
    final_dist = np.convolve(final_dist, x)
    final_dist = final_dist / np.sum(final_dist)


plt.plot(final_dist, 
         label = r'Sum av {} fuglekasser.'.format(terms_in_sum1+terms_in_sum2), 
         linewidth = 2.5)

terms_in_sum3 = 20
for i in range(terms_in_sum3 - 1):
    final_dist = np.convolve(final_dist, x)
    final_dist = final_dist / np.sum(final_dist)

plt.plot(final_dist, 
         label = r'Sum av {} fuglekasser.'.format(terms_in_sum1+terms_in_sum2+terms_in_sum3), 
         linewidth = 2.5)

plt.legend(loc = 'best')
plt.savefig('fuglekasser.pdf', bbox_inches='tight')
plt.show()
    