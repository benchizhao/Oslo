import pickle
from Oslo_model import RelaxModel


def scaling_above():
    critical = []
    for i in range(2, 260):
        model = RelaxModel(0.5, i, i * i + 4000)
        model.start()
        critical.append(model.critical_z())
        print(model.critical_z())


results = scaling_above()

with open('critial_z_for_L_2-260.txt', 'wb') as fp:
    pickle.dump(results, fp)