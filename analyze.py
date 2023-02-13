import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#backLegSensorValues = np.load('data/backLegSensorData.npy')
#frontLegSensorValues = np.load('data/frontLegSensorData.npy')
targetAnglesValues = np.load('data/targetAnglesData.npy')
#print(backLegSensorValues)
#print(frontLegSensorValues)
print(targetAnglesValues)
#frontLeg = plt.plot(backLegSensorValues, label='Back Leg', linewidth = 7)
#backLeg = plt.plot(frontLegSensorValues, label='Front Leg')
angles = plt.plot(targetAnglesValues, np.sin(targetAnglesValues), label='Angles')
plt.legend(loc = 'best')
plt.show()