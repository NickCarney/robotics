import numpy as np
import matplotlib
import matplotlib.pyplot as plt

backLegSensorValues = np.load('data/backLegSensorData.npy')
frontLegSensorValues = np.load('data/frontLegSensorData.npy')
print(backLegSensorValues)
print(frontLegSensorValues)
frontLeg = plt.plot(backLegSensorValues, label='Back Leg', linewidth = 7)
backLeg = plt.plot(frontLegSensorValues, label='Front Leg')
plt.legend(loc = 'best')
plt.show()