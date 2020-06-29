from Oslo_model import RelaxModel
import pickle


with open("Q2-a.txt", "rb") as fp:
    cross_over_time = pickle.load(fp)

for i in range(len(cross_over_time)):
    cross_over_time[i] = int(round(cross_over_time[i],0))
print(cross_over_time)


length = [4,8,16,32,64,128,256]
times = 100000
ave_height = []
def ave_height_f():
    for i in range(len(length)):
        model = RelaxModel(0.5,length[i],times)
        model.start()
        useful_height = model.heights[cross_over_time[i]+1:]
        ave = sum(useful_height)/len(useful_height)
        ave_height.append(ave)
    print('done 1')
    return ave_height
a = ave_height_f()

with open('ave_h_of_recurrent.txt','wb') as fp:
    pickle.dump(a, fp)


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
    print('done 2')
    return sigma_h
b = sigma_f()
with open('sigma.txt','wb') as fp:
    pickle.dump(b, fp)

Prob = []
maxmin = []
def height_prob_f():
    for i in range(len(length)):
        media = []
        model = RelaxModel(0.5, length[i], times)
        model.start()
        useful_height = model.heights[cross_over_time[i]+1:]
        maximum = max(useful_height)+1
        minimum = min(useful_height)
        for j in range(minimum,maximum):
            P = useful_height.count(j)/len(useful_height)
            media.append(P)
        Prob.append(media.copy())
        maxmin.append(range(minimum, maximum))
    print('done all')
    return Prob,maxmin
c = height_prob_f()
print(c)
with open('height_probability.txt','wb') as fp:
    pickle.dump(c, fp)



