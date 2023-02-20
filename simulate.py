import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random as rand
import constants as c
from simulation import SIMULATION
simulation = SIMULATION()
simulation.Run()


# np.save('data/blTargetAnglesData.npy',blTargetAngles)
# np.save('data/flTargetAnglesData.npy',flTargetAngles)
# #exit()

# np.save('backLegSensorData.npy',backLegSensorValues)
# np.save('frontLegSensorData.npy',frontLegSensorValues)
# p.disconnect() 
