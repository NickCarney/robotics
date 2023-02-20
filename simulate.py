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

# backLegSensorValues = np.zeros(c.iterations)
# frontLegSensorValues = np.zeros(c.iterations)
# #maxVal = amplitude * np.sin(frequency*iterations + phaseOffset)
# blTargetAngles = c.blAmplitude*(np.sin((np.linspace(c.zero, 2*np.pi, c.iterations)*c.blFrequency)+c.blPhaseOffset))
# flTargetAngles = c.flAmplitude*(np.sin((np.linspace(c.zero, 2*np.pi, c.iterations)*c.flFrequency)+c.flPhaseOffset))
# np.save('data/blTargetAnglesData.npy',blTargetAngles)
# np.save('data/flTargetAnglesData.npy',flTargetAngles)
# #exit()

# np.save('backLegSensorData.npy',backLegSensorValues)
# np.save('frontLegSensorData.npy',frontLegSensorValues)
# p.disconnect() 
