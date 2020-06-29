import matplotlib.pyplot as plt
from Oslo_model import RelaxModel
import pickle
import numpy as np
import math

with open("critial_z_for_L_2-260.txt", "rb") as fp:
    cri_z = pickle.load(fp)
    ave_z = sum(cri_z)/len(cri_z)
print(ave_z/2)


with open(('Q2-a.txt'), "rb") as fp:
    x_list = pickle.load(fp)
print(x_list)

def curve_fit_tc_L():
    x = [math.log10(m) for m in x_list]
    y_list = [4,8,16,32,64,128,256]
    y = [math.log10(m) for m in y_list]
    s, cov = np.polyfit(y,x, 1, cov=True)
    print(s)
    print(math.sqrt(cov[1][1]))
    xx = range(2,260)
    yy = [(var **1.98)*10**(-0.036) for var in xx]
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(y_list, x_list, 'bo', label = 'Cross-over time <t_c>')
    ax.plot(xx , yy,'r',label = 'Linear fit with slop \n 1.981 +- 0.024')
    plt.xlabel('System size L')
    plt.ylabel('Average cross-over time <t_c>')
    plt.legend()
    ax.set_xscale('log')
    ax.set_yscale('log')
    plt.show()
curve_fit_tc_L()



def scaling_above():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    #plot points
    x1 = [4,8,16,32,64,128,256]
    y1 = x_list
    for i in range(len(x1)):
        y1[i] = y1[i]/x1[i]**2
    ax.plot(x1, y1, 'bo', label = 'Scaled cross_over time <t_c/L^2>')

    #without approximation
    x2 = range(2,260)
    y2 = [ave_z*0.5*(1+1/var) for var in x2]
    ax.plot(x2, y2,  'r', label='Relatin of <z>*1/2*(1+1/L)')

    #with approximation
    x3 = range(2,260)
    y3 = [(ave_z/2)]*len(x3)
    ax.plot(x3, y3, 'k--', label = '<z>/2 = 0.8449')

    plt.xlabel('System size L')
    plt.ylabel('Scaled average cross-over time <t_c>/L^2')
    plt.legend()
    plt.show()

scaling_above()