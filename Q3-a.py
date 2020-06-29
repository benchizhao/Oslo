import logbin230119 as lb
import numpy as np
import pickle
import matplotlib.pyplot as pl
from Oslo_model import RelaxModel

with open("avalanche_size.txt", "rb") as fp:
    avalanche_size = pickle.load(fp)
print(avalanche_size[6])

with open("Q2-a.txt", "rb") as fp:
    t_c = pickle.load(fp)
    for i in range(len(t_c)):
        t_c[i] = int(t_c[i])
print(t_c)

length = [4,8,16,32,64,128,256]
time = 100000

def write_in_ava_size():
    avalanche_size = []
    for i in range(len(length)):
        model = RelaxModel(0.5, length[i], time)
        model.start()
        avalanche_size.append(model.ava_size_list.copy())
    with open('avalanche_size.txt', 'wb') as fp:
        pickle.dump(avalanche_size, fp)



def Prob_vs_s():
    fig = pl.figure()
    ax = fig.add_subplot(1, 1, 1)
    for item in range(len(length)):
        avasize = avalanche_size[item]
        reqsize = avasize[t_c[item]:]
        # Log-bin the data
        bincentre_bin, hist_bin = lb.logbin(reqsize, scale=1.5)
        print(bincentre_bin)
        print(hist_bin)
        ax.loglog(bincentre_bin, hist_bin, '-', label=r"$L = %d$" % (length[item]))
    x = bincentre_bin[:25]
    y = hist_bin[:25]
    para, var = np.polyfit(np.log(np.array(x)) / np.log(10), np.log(y) / np.log(10), 1, cov=True)
    error = np.sqrt(np.diag(var))
    x1 = range(1, 200000, 100)
    y1 = 10 ** (para[0] * (np.log(x1) / np.log(10)))
    ax.loglog(x1, y1, 'k--', label=r'Slop = %.3f $\pm$ %.3f'%(para[0],error[0]))
    pl.grid(True)
    pl.legend()
    pl.xlabel(r"Avalanche size $s$")
    pl.ylabel(r"Probability of $s$ $P(s; L)$")
    pl.show()
Prob_vs_s()

avasize = avalanche_size[-1]

def single_plot():
    for i in [2,3, 4, 5, 6]:
        if i != 6:
            reqsize = avasize[t_c[-1]: t_c[-1] + 10 ** i]
        else:
            reqsize = avasize[t_c[-1]:]
        bins = np.arange(min(reqsize) , max(reqsize) , 1)
        bincentre = bins[:-1]

        hist, bin_edges = np.histogram(reqsize, bins=bins, density=True)  # density = True returns probability density
        # Log-bin the data
        bincentre_bin, hist_bin = lb.logbin(reqsize, scale=1.5)

        fig = pl.figure()
        ax = fig.add_subplot(1, 1, 1)
        if i != 6:
            ax.loglog(bincentre, hist, 'o', label=r"Unbinned, $N = 10^%d$" % (i))
            ax.loglog(bincentre_bin, hist_bin, 'r-', label=r"Binned, $N = 10^%d$" % (i))
        else:
            ax.loglog(bincentre, hist, 'o', label=r"Unbinned, $N = %.1g$" % (1e6 - t_c[-1]))
            ax.loglog(bincentre_bin, hist_bin, 'r-', label=r"Binned, $N = %.1g$" % (1e6 - t_c[-1]))
        pl.legend()
        pl.grid()
        pl.xlim(1, 10 ** 6)
        pl.ylim(10 ** -13, 1)
        pl.xlabel('System size L')
        pl.ylabel(r'$\sigma_h$')
        pl.show()
# single_plot()