import numpy as np
import matplotlib
import matplotlib.pyplot as plt

backLegSensorValues = np.load('data/backLegSensorData.npy')
frontLegSensorValues = np.load('data/frontLegSensorData.npy')
print(backLegSensorValues)
print(frontLegSensorValues)
frontLeg = plt.plot(backLegSensorValues)
backLeg = plt.plot(frontLegSensorValues)
frontLeg.set_label('Front Leg')
backLeg.set_label('Back Leg')
plt.legend()
plt.show()