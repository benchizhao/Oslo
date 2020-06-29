import logbin230119 as lb
import numpy as np
import pickle
import matplotlib.pyplot as pl
from Oslo_model import RelaxModel
import operator

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


def tau_s():
    avasize = avalanche_size[-1]
    reqsize = avasize[t_c[-1]:]
    bincentre_bin, hist_bin = lb.logbin(reqsize, scale=1.5)
    x = bincentre_bin[:25]
    y = hist_bin[:25]
    para, var = np.polyfit(np.log(np.array(x)) / np.log(10), np.log(y) / np.log(10), 1, cov=True)
    error = np.sqrt(np.diag(var))
    return -para[0], error[0]
tau = tau_s()[0]
b = tau_s()[1]
print(tau)
print(b)

def d_value():
    s_max = []
    for i in range(len(length)):  # neglect largest L since it is used for comparison
        avasize = avalanche_size[i]
        reqsize = avasize[t_c[i]:]
        bincentre_bin, hist_bin = lb.logbin(reqsize, scale=1.5)
        #scaling y axis
        hist_bin = np.array(hist_bin) * np.array(bincentre_bin) ** tau - b

        index, value = max(enumerate(hist_bin), key=operator.itemgetter(1))
        s_max.append(bincentre_bin[index])
    para1, var1 = np.polyfit(np.log(np.array(length)) / np.log(10), np.log(s_max) / np.log(10), 1, cov=True)
    error = np.sqrt(np.diag(var1))
    return para1,error
D = d_value()[0][0]
print(D)
print(d_value()[1][0])
print(d_value()[0][1])

def Plot_collapse_data():
    fig = pl.figure()
    ax = fig.add_subplot(1, 1, 1)
    for item in range(len(length)):
        avasize = avalanche_size[item]
        reqsize = avasize[t_c[item]:]
        # Log-bin the data
        bincentre_bin, hist_bin = lb.logbin(reqsize, scale=1.5)
        hist_bin = np.array(hist_bin)*np.array(bincentre_bin)**tau
        bincentre_bin = bincentre_bin/(np.array(length)[item]**D)
        ax.loglog(bincentre_bin, hist_bin, '-', label=r"$L = %d$" % (length[item]))
    pl.grid(True)
    pl.legend()
    pl.xlabel(r"Avalanche size $s/L^D$")
    pl.ylabel(r"Probability $s^\tau P(s; L)$")
    pl.show()
Plot_collapse_data()
