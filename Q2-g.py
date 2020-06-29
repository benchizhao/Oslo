import matplotlib.pyplot as plt
import pickle
import numpy as np
import math
from scipy.optimize import curve_fit


length = [4, 8, 16, 32, 64, 128, 256]

with open("a0,a1,w1.txt", "rb") as fp:
    factors_for_h = pickle.load(fp)
print(factors_for_h)
a0h = factors_for_h[0]
a1h = factors_for_h[1]
w1h = factors_for_h[2]

with open("ave_h_of_recurrent.txt", "rb") as fp:
    h_ave = pickle.load(fp)
print(h_ave)

with open("sigma.txt", "rb") as fp:
    sigma = pickle.load(fp)
print(sigma)

with open("height_probability.txt", "rb") as fp:
    h_prob = pickle.load(fp)
print(h_prob[0][6])
print(h_prob[1][6])



def plot_prob_vs_h():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    for i in range(len(length)):
        ax.plot(h_prob[1][i], h_prob[0][i], label="L = %i" % (length[i]))
    plt.xlabel('Height h')
    plt.ylabel('Probability of height P(h;L)')
    plt.grid()
    plt.legend()
    plt.ylim(0,)
    plt.show()
# plot_prob_vs_h()


def plot_gaussian():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    for i in range(len(length)):
        x = (np.array(h_prob[1][i])-h_ave[i])/sigma[i]
        y = np.array(h_prob[0][i])*sigma[i]
        ax.plot(x,y,label = 'L = %i' %(length[i]))
    plt.xlabel(r'(h-<h>)/$\sigma$')
    plt.ylabel(r'$\sigma$P(h;L)')
    plt.legend()
    plt.show()
plot_gaussian()



