import matplotlib.pyplot as plt
import pickle
import numpy as np
from scipy import stats


with open("ave_h_of_recurrent.txt", "rb") as fp:
    h_ave = pickle.load(fp)
print(h_ave)

length = [4,8,16,32,64,128,256]
def ave_h_slop(x,y):
    s,cov = np.polyfit(x,y,1, cov=True)
    uncertainty = np.sqrt(np.diag(cov))
    return round(s[0],4),round(s[1],4),round(uncertainty[0],4),round(uncertainty[1],4)

coefficient = ave_h_slop(length,h_ave)
print(coefficient)


def plot_fit_height():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(length, h_ave, 'bo',label = 'Average height <h>')
    x = range(length[-1] + 100)
    y = [coefficient[0]*var + coefficient[2] for var in x]
    ax.plot(x,y,label = 'Linear fit with slop \n 1.722 +- 0.002 \n and intercept \n -0.966 +- 0.171',color = 'r')
    plt.legend()
    plt.grid()
    plt.xlabel('System size L')
    plt.ylabel('Average height <h>')
    plt.show()
plot_fit_height()

def curvefit_a0():
    testa0 = np.linspace(1.72, 1.74, 150)

    slop_var = []
    for i in range(len(testa0)):
        y = []
        for j in range(len(length)):
            y.append(abs(testa0[i] - h_ave[j] / length[j]))
        slope, intercept, r_value, p_value, std_err = stats.linregress(np.log(np.array(length)), np.log(y))
        # testpara, testvar = np.polyfit(np.log(np.array(length)) / np.log(10), np.log(y) / np.log(10), 1, cov=True)
        slope_r2 = r_value**2
        slop_var.append(slope_r2)
    a0index = slop_var.index(max(slop_var))
    mina0 = testa0[a0index]



    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(testa0, slop_var, 'o')
    ax.plot(mina0, slop_var[a0index],'ro',label = r'Best fitted point a0 = %.3f' %(mina0))

    plt.xlabel(r"$a_0$")
    plt.ylabel(r"Adjusted R$^2$")
    plt.legend()
    plt.show()
    return mina0

a0 = curvefit_a0()

def curvefit_a1_w1():
    a0_err = 0.001
    yfinal = a0 - np.array(h_ave) / (np.array(length))
    parafinal, varfinal = np.polyfit(np.log(np.array(length)) / np.log(10), np.log(yfinal) / np.log(10), 1, cov=True)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(length, yfinal, 'o', label=r"Best-fit line with $a_0 = %.3f \pm %.3f$" % (a0, a0_err))
    plt.xlabel('System size L')
    plt.ylabel(r'$a_0$ - $<h>)/L$')

    xpts= np.logspace(0.1, 3, 5000)
    yptsfinal = 10 ** (parafinal[0] * (np.log(xpts) / np.log(10)) + parafinal[1])
   # ytest = 10 ** (parafinal1 * (np.log(xpts) / np.log(10)) + parafinal1[1])
    ax.plot(xpts, yptsfinal, 'k--', label="Linear fit with slope = $%.3f \pm %.3f$" % (
    parafinal[0], np.sqrt(np.diag(varfinal))[0]) + "\n" + "and intercept = $%.3f \pm %.3f$" % (parafinal[1], np.sqrt(np.diag(varfinal))[1]))
   # ax.plot(xpts, ytest, 'r--')
    ax.set_xscale('log')
    ax.set_yscale('log')
    plt.legend()
    plt.show()
    # Calculate a_1 and w_1 from the intercept and slope respectively
    a1 = 10 ** (parafinal[1] - np.log(a0) / np.log(10))
    w1 = -parafinal[0]
    data = [a0, a1, w1]  # a_0, a_1, w_1
    return data

result = curvefit_a1_w1()
print(result)

# with open('a0,a1,w1.txt','wb') as fp:
#     pickle.dump(result, fp)