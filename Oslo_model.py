# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 15:57:19 2020

@author: Benchi Zhao
"""
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from random import choices

class RelaxModel:
    def __init__(self, p, length, times):
        self.p = p
        self.L = length
        self.times = times
        self.population = [1, 2]
        self.weights = [p, 1 - p]
        self.l = [0] * length
        self.slop = [0] * length
        self.z = choices(self.population, self.weights, k=length)

        self.heights = []
        self.all_slop = []
        self.ave_slop = []
        self.totall_grains = []
        self.configuration = []
        self.ava_size_list = []

        self.critical_number_grians = 0
        self.n_th_out = 0
        self.t_c = 0
        self.ave_t_c = 0

        self.last = self.L - 1
        self.second_last = self.L - 2

        self.check_again = False

    def start(self):
        for i in range(self.times):
            self.ava_size = 0
            self.run_once()

            self.ave_slop.append(sum(self.slop)/len(self.slop))
            self.ava_size_list.append(self.ava_size)
            self.configuration.append(self.l.copy())
            self.all_slop.append(self.slop.copy())

    def run_once(self):
        l = self.l
        slop = self.slop

        l[0] += 1
        slop[0] += 1

        self.check_again = True
        while self.check_again:
            self.check_again = False
            self.check_slop_once()
        assert 3 not in slop
        self.heights.append(l[0])
        self.totall_grains.append(sum(self.l))

    def check_slop_once(self):
        slop = self.slop
        z = self.z

        for i in range(self.L):
            while slop[i] > z[i]:
                self.ava_size += 1
                self.check_again = True
                self.iter_i(i)

    def iter_i(self, i):
        if i == 0:
            self.slide_first(i)
        elif i == self.last:
            self.slide_last(i)
        else:
            self.slide_middle(i)

    def slide_first(self, i):
        slop = self.slop
        l = self.l

        slop[0] -= 2
        slop[1] += 1
        l[1] += 1
        l[0] -= 1
        self.z[i] = self.next_weight()

    def slide_middle(self, i):
        slop = self.slop
        l = self.l

        slop[i] -= 2
        slop[i + 1] += 1
        slop[i - 1] += 1
        l[i + 1] += 1
        l[i] -= 1
        self.z[i] = self.next_weight()

    def slide_last(self, i):
        slop = self.slop
        l = self.l

        slop[self.last] -= 1
        slop[self.second_last] += 1
        l[self.last] -= 1
        self.z[i] = self.next_weight()

    def next_weight(self):
        return choices(self.population, self.weights)[0]

    def plot_height(self,colour):
        x=range(len(self.heights))
        plt.plot(x,self.heights,c=colour,marker='.')
        plt.show()

    def which_grain_out(self):
        auxiliary_list = range(1,self.times+1)
        for i in range(self.times):
            if auxiliary_list[i] - self.totall_grains[i] != 0:
                self.n_th_out = i - 1
                break
        return self.n_th_out


    def cross_over_time(self):
        self.t_c = 0
        for i in range(self.L):
            self.t_c += self.all_slop[self.which_grain_out()][i] * (i+1)
            
    def ave_cross_over_time(self):
        for i in range(self.L):
            self.ave_t_c += self.ave_slop[i] * (i+1)


    def critical_z(self):
        return sum(self.all_slop[self.which_grain_out()])/len(self.all_slop[self.which_grain_out()])

l =10
model = RelaxModel(0.5,l,300)
model.start()
model.which_grain_out()
print(model.n_th_out)

