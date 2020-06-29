import matplotlib.pyplot as pl
import pickle
import numpy as np

with open("Q2-a.txt", "rb") as fp:
    cross_over_time = pickle.load(fp)

with open("avalanche_size.txt", "rb") as fp:
    avalanche_size = pickle.load(fp)

for i in range(len(cross_over_time)):
    cross_over_time[i] = int(round(cross_over_time[i],0))


length = [4,8,16,32,64,128,256]
times = 100000

def ave_ava_f(k):
    ave_ava_size = []
    for i in range(len(avalanche_size)):
        useful_value = avalanche_size[i][cross_over_time[i]+1:]
        useful_value = [var**k for var in useful_value]
        ave = sum(useful_value)/len(useful_value)
        ave_ava_size.append(ave)
    return ave_ava_size



def plot_ave_k():
    fig = pl.figure()
    ax = fig.add_subplot(1, 1, 1)
    slops = []
    for l in [1,2,3,4,5]:
        ax.loglog(length,ave_ava_f(l) ,'o',label = 'k = %i' %(l))
        para, var = np.polyfit(np.log(np.array(length)) / np.log(10), np.log(ave_ava_f(l)) / np.log(10), 1, cov=True)
        x = range(1,260)
        y = 10 ** (para[0] * (np.log(x) / np.log(10)) + para[1])
        ax.loglog(x, y, label='Linear fit for k = %i' % (l))
        slops.append(para[0])
    pl.grid(True)
    pl.legend()
    pl.xlabel(r"Length L")
    pl.ylabel(r"k'th moment $<s^k>$")
    pl.show()
    return slops
slops = plot_ave_k()
print(slops)

def fit_slops():
    k = [1,2,3,4,5]
    para, var = np.polyfit(k,slops, 1, cov=True)
    error = np.sqrt(np.diag(var))

    fig = pl.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(k, slops,'o', label=r'Slops of $k^{th}$ moment ')
    x = np.linspace(1, 5.5,100)
    y =para[0] * np.array(x) + para[1]
    ax.plot(x, y, label=r'D = %.3f $\pm$ %.3f' %(para[0],error[0])+'\n'+r'$\tau$ =  %.3f $\pm$ %.3f'%((para[0]-para[1])/para[0],error[1]))
    pl.grid(True)
    pl.legend()
    pl.xlabel(r"k")
    pl.ylabel(r"D(1+k-$\tau_s$)")
    pl.show()
    print(para,error)

fit_slops()