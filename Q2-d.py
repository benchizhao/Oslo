from Oslo_model import RelaxModel
from operator import add
import pickle

def h_tilde(M):
    length = [4,8]
    times = 100000
    h_tilde = []
    for i in range(len(length)):
        h_data_base = [0]*times
        for j in range(M):
            model = RelaxModel(0.5, length[i], times)
            model.start()
            h_data_base = list(map(add, h_data_base, model.heights))
        h_data_base = [x/M for x in h_data_base]
        h_data_base = [round(i, 3) for i in h_data_base]
        h_tilde.append(h_data_base)
    return h_tilde

h_ave = h_tilde(15)
print(h_ave)

with open('Q2-d.txt','wb') as fp:
    pickle.dump(h_ave, fp)