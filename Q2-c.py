# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 10:57:19 2020

@author: Benchi Zhao
"""
from Oslo_model import RelaxModel
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from random import choices

'''
Question 2 c
----------------------------------------------------------
Consider the shape of the pile is triangle with length L, average slop <slop>, so the height is L*<slop>, which is 
proportional to size of pile L. The total number of grains is the obviously the area enclosed by the triangle, which is 
height times side: L*<slop>*L proportional to L**2
'''

def plot_ave_slop(length,times):
    data_base = []
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    for i in range(len(length)):
        model = RelaxModel(0.5, length[i], times)
        model.start()
        data_base.append(model.ave_slop)
    for i in range(len(data_base)):
        ax.plot(range(times), data_base[i], label='L=%a' % (length[i]), linewidth=0.5)
    ax.set_xscale('log')
    plt.legend()
    plt.xlabel('Grains driven into system')
    plt.ylabel('Height of system')
    plt.show()


plot_ave_slop([2,4,8,16,32],10000)