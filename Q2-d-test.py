from Oslo_model import RelaxModel
from operator import add
import matplotlib.pyplot as plt
import pickle
import numpy as np
import math

with open("Q2-d.txt", "rb") as fp:
    h_tilde = pickle.load(fp)
print(h_tilde[-1][:600])
with open("Q2-a.txt", "rb") as fp:
    stop_point = pickle.load(fp)
    stop_point = int(round(stop_point[-1],0))
print(stop_point)


def curve_fit():
    x = range(1,stop_point)
    x = [math.log10(m) for m in x]
    y = h_tilde[-1][1:stop_point]
    y = [math.log10(m) for m in y]
    s,cov = np.polyfit(x[:stop_point],y[:stop_point],1, cov=True)
    uncertainty = np.sqrt(np.diag(cov))
    return s[0],s[1],uncertainty[0]

coefficient = curve_fit()
print(coefficient)


def plot_collapsed_height():
    length = [4,8,16,32,64,128,256]
    t = range(1,100001)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    for i in range(len(length)):
        y = [var/length[i] for var in h_tilde[i]]
        x = [var/(length[i]*length[i]) for var in t]
        ax.plot(x, y, label='L=%a' % (length[i]), linewidth=0.5)
    x = range(1,stop_point+100000)
    x_curve = [var / (256*256) for var in x]
    y_curve = [t**coefficient[0] for t in x]
    y_curve = [10**coefficient[1] *t for t in y_curve]
    y_curve = [var/256 for var in y_curve]
    ax.plot(x_curve,y_curve,'--',label = 'Linear fit with slop \n 0.51021 +- 0.00002',color = 'k')
    ax.set_xscale('log')
    ax.set_yscale('log')
    plt.legend()
    plt.grid()
    plt.xlabel('Scaled time t/L\u00b2')
    plt.ylabel('Scaled average height of system h/L')
    plt.show()

# plot_collapsed_height()
