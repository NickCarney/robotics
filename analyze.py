import numpy as np
import matplotlib
import matplotlib.pyplot as plt


blTargetAnglesValues = np.load('data/blTargetAnglesData.npy')
flTargetAnglesValues = np.load('data/flTargetAnglesData.npy')
#print(backLegSensorValues)
#print(frontLegSensorValues)
#print(blTargetAnglesValues)
#frontLeg = plt.plot(backLegSensorValues, label='Back Leg', linewidth = 7)
#backLeg = plt.plot(frontLegSensorValues, label='Front Leg')
bAngles = plt.plot(np.sin(blTargetAnglesValues), label='Angles')
fAngles = plt.plot(np.sin(flTargetAnglesValues), label='Angles2')
plt.legend(loc = 'best')
plt.show()