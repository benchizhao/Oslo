from Oslo_model import RelaxModel
import matplotlib.pyplot as plt
import pylab
from random import choices
import pickle


class SovlingQuestionTwo:
    def __init__(self,p,lengths_of_system,times):
        self.p = p
        self.lengths_of_system = lengths_of_system
        self.times = times
        self.data_base_height = []
        self.list_tc = []
        self.ave_tc_list = []

    def plot_figure_data(self):
        for i in range(len(self.lengths_of_system)):
            model = RelaxModel(0.5,self.lengths_of_system[i],self.times)
            model.start()
            self.data_base_height.append(model.heights)

    def plot_figure_labels(self):
        for i in range(len(self.data_base_height)):
            plt.plot(range(self.times), self.data_base_height[i], label='L=%a' % (self.lengths_of_system[i]), linewidth = 0.5)
            #the plt.plot can be weitched to plt.loglog, so that we can get a log scale figure.
        plt.legend()
        plt.xlabel('Grains driven into system')
        plt.ylabel('Height of system')
        plt.show()

    def plot_figure(self):
        self.plot_figure_data()
        self.plot_figure_labels()

    def ave_tc(self):
        for i in range(len(self.lengths_of_system)):
            ave_tc = 0.0
            model = RelaxModel(0.5, self.lengths_of_system[i], self.times)
            model.start()
            model.cross_over_time()
            for j in range(len(model.ave_slop)):
                self.ave_tc = self.ave_tc + model.ave_slop[i]*(i+1)
            self.ave_tc_list.append(ave_tc)

    def save_data(self):
        with open('system_heights.txt', 'wb') as fp:
            pickle.dump(self.data_base_height, fp)


'''
Question 2a
---------------------------------------------------------
'''
Q2 = SovlingQuestionTwo(0.5,[4,8,16,32,64,128,256],100000)
Q2.plot_figure()
Q2.save_data()



