from Oslo_model import RelaxModel
import pickle
import numpy as np
import matplotlib.pyplot as plt


with open("Q2-a.txt", "rb") as fp:
    cross_over_time = pickle.load(fp)

for i in range(len(cross_over_time)):
    cross_over_time[i] = int(round(cross_over_time[i],0))
print(cross_over_time)

f_file = open('a0,a1,w1.txt', 'rb')
constants = pickle.load(f_file)
f_file.close()

print(constants)
a0 = constants[0]
a1 = constants[1]
w1 = constants[2]


length = [4,8,16,32,64,128,256]
times = 100000
ave_height = []
def ave_height_f():
    for i in range(len(length)):
        ave = a0*np.array(length)[i]*(1-a1*np.array(length)[i]**-w1)
        ave_height.append(ave)
    print('done 1')
    return ave_height
a = ave_height_f()


sigma_h = []
def sigma_f():
    for i in range(len(length)):
        model = RelaxModel(0.5, length[i], times)
        model.start()
        useful_height = model.heights[cross_over_time[i]+1:]
        ave = sum(useful_height) / len(useful_height)
        hh = [x*x for x in useful_height]
        sigma = (sum(hh)/len(useful_height)-ave**2)**(0.5)
        sigma_h.append((sigma))
    print(sigma_h)
    return sigma_h
# b = sigma_f()

with open('sigma.txt','wb') as fp:
    pickle.dump(b, fp)

sigma_h = [0.8024041474783541, 0.9574525014044384, 1.1325304315206037, 1.3523052008719416, 1.5575624127831909, 1.8559043344721602, 2.1273409438265767]

para, var = np.polyfit(np.log(np.array(length)) / np.log(10), np.log(sigma_h) / np.log(10), 1, cov=True)
error = np.sqrt(np.diag(var))
print(para,error[0])

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

x = range(2,300)
y = 10 ** (para[0] * (np.log(x) / np.log(10)) + para[1])
ax.loglog(x, y,color = 'r', label=r'Curve fit of sigma with slop %.3f $\pm$ %.3f' %(para[0],error[0]))
ax.loglog(length, sigma_h, 'bo')
plt.legend()
plt.grid()
plt.xlabel('System size L')
plt.ylabel(r'$\sigma_h$')
plt.show()



