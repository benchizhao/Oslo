from Oslo_model import RelaxModel
'''
# Question 1
-------------------------------------------------------------------------
'''
model_16 = RelaxModel(0.5,16,100000)
model_16.start()
print(sum(model_16.heights)/len(model_16.heights))

model_32 = RelaxModel(0.5,32,100000)
model_32.start()
print(sum(model_32.heights)/len(model_32.heights))
