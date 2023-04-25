import numpy as np
import matplotlib.pyplot as plt
import constants as c
variantA = np.load('totalFitnessData.npy')
variantB = np.load('totalFitnessData2.npy')
averagesA = [0]*c.numberOfGenerations
averagesB = [0]*c.numberOfGenerations
for i in range(c.numberOfGenerations):
    #aRow = plt.plot(variantA[i,:], label = 'A'+str(i), linewidth = 2)
    averagesA[i] = np.mean(variantA[i,:])
    #bRow = plt.plot(variantB[i,:],label = 'B'+str(i), linewidth = 7)
    averagesB[i] = np.mean(variantB[i,:])
plt.plot(averagesA, label = 'A', linewidth = 2)
plt.plot(averagesB, label = 'B', linewidth = 7)
plt.legend(loc = 'best')
plt.show()
