import numpy as np
import pickle
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

length = [4, 8, 16, 32, 64, 128, 256]

f_file = open('sigma.txt', 'rb')
sigma = pickle.load(f_file)
f_file.close()
print(sigma)

f_file = open('a0,a1,w1.txt', 'rb')
constants = pickle.load(f_file)
f_file.close()

print(constants)
a0 = constants[0]
a1 = constants[1]
w1 = constants[2]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(length, sigma, 'bo')
plt.xlabel('System size L')
plt.ylabel(r'$a_0 - <h>)/ L$')
plt.grid()
plt.show()

# Optimise a scaling funvtion for it
# def scaling(L, a0, w0, a1, w1):
#     return a0*(L**w0)*(1 - a1*L**-w1)
#
#
# def plot_sigma_h():
#     a0_err = 0.01
#     fig = plt.figure()
#     ax = fig.add_subplot(1, 1, 1)
#     ax.plot(length, sigma, 'bo', label="Best-fit line with a_0 = %.3f +- %.3f" % (a0, a0_err))
#     plt.xlabel('System size L')
#     plt.ylabel(r'$a_0 - <h>)/ L$')
#     plt.grid()
#
#     para, var = curve_fit(scaling, np.log(length) / np.log(10), np.log(sigma) / np.log(10), p0 = [0.1,1,1,2])
#     print(para,var)
#     xpts = np.logspace(0.2, 3.1, 5000)
#     ypts = 10 ** (para[0] * (np.log(xpts) / np.log(10)) ** para[1] * (
#                 1 - para[2] * (np.log(xpts) / np.log(10)) ** (-para[3])))
#
#     plt.loglog(xpts, ypts, 'r-', label=r"Scaling function $a_0 L^{\omega_0} (1 - a_1 L^{-\omega_1})$ fit with"
#                                        + "\n" + r"$a_0 = %.3f \pm %.3f$" % (
#                                        para[0], np.sqrt(np.diag(var)[0])) + "\n" + r"$\omega_0 = %.3f \pm %.3f$" % (
#                                        para[1], np.sqrt(np.diag(var)[1]))
#                                        + "\n" + r"$a_1 = %.3f \pm %.3f$" % (
#                                        para[2], np.sqrt(np.diag(var)[2])) + "\n" + r"$\omega_1 = %.3f \pm %.3f$" % (
#                                        para[3], np.sqrt(np.diag(var)[3])))
#     plt.legend()
#
#     # Divide by a0*L**w0 to obtain trend for large L - expect SD to tend towards a0*L**w0
#     yptsdiv = ypts / 10 ** (para[0] * (np.log(xpts) / np.log(10)) ** para[1])
#     sddiv = sigma / 10 ** (para[0] * (np.log(length) / np.log(10)) ** para[1])
#
#     plt.figure()
#     plt.loglog(length, sddiv, 'bo', label=r"Scaled standard deviation $\sigma_h / a_0 L^{\omega_0}$")
#     plt.xlabel(r"System size $L$")
#     plt.ylabel(r"Scaled standard deviation $\sigma_h / a_0 L^{\omega_0}$")
#     plt.grid()
#     plt.loglog(xpts, yptsdiv, 'r-', label=r"Scaling function $(1 - a_1 L^{-\omega_1})$ fit")
#     plt.legend()
#     plt.ylim(0.1, 10)
#     plt.show()
#     return para
#
# result = plot_sigma_h()
#
# with open('a0,w0,a1,w1_for_sigma.txt','wb') as fp:
#     pickle.dump(result, fp)