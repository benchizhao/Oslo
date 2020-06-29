# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 10:54:46 2020

@author: Benchi Zhao
"""

from Oslo_model import RelaxModel
import pickle
'''
Question 2 b
Creat 100 piles and find the number of grains at cross over time by length of 4,8,16,32,64,128,256
calculate the average
----------------------------------------------------------
'''
def ave_tc(number_of_piles):
    lengths_of_system = [4,8,16,32,64,128,256]
    all_tc_list = []
    times = 100000
    for i in range(len(lengths_of_system)):
        ave_tc_list = []
        for j in range(number_of_piles):
            model = RelaxModel(0.5,lengths_of_system[i],times)
            model.start()
            model.cross_over_time()
            ave_tc_list.append(model.t_c)
        all_tc_list.append(sum(ave_tc_list)/len(ave_tc_list))
    return all_tc_list
a = ave_tc(15)
print(a)

with open('Q2-a.txt','wb') as fp:
    pickle.dump(a, fp)
