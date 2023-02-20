import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random as rand
import constants as c

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(c.zero,c.zero,c.gravity)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = np.zeros(c.iterations)
frontLegSensorValues = np.zeros(c.iterations)
#maxVal = amplitude * np.sin(frequency*iterations + phaseOffset)
blTargetAngles = c.blAmplitude*(np.sin((np.linspace(c.zero, 2*np.pi, c.iterations)*c.blFrequency)+c.blPhaseOffset))
flTargetAngles = c.flAmplitude*(np.sin((np.linspace(c.zero, 2*np.pi, c.iterations)*c.flFrequency)+c.flPhaseOffset))
np.save('data/blTargetAnglesData.npy',blTargetAngles)
np.save('data/flTargetAnglesData.npy',flTargetAngles)
#exit()
for i in range(c.iterations):
    time.sleep(c.sleep)
    #print(i)
    p.stepSimulation()
    #targetAngles[i] = amplitude * np.sin(frequency*i + phaseOffset)
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,
    jointName = b'Torso_BackLeg',
    controlMode = p.POSITION_CONTROL,
    targetPosition = np.sin(blTargetAngles[i]),
    maxForce = c.maxForce)
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,
    jointName = b'Torso_FrontLeg',
    controlMode = p.POSITION_CONTROL,
    targetPosition = np.sin(flTargetAngles[i]),
    maxForce = c.maxForce)
    #print(frontLegSensorValues)
np.save('backLegSensorData.npy',backLegSensorValues)
np.save('frontLegSensorData.npy',frontLegSensorValues)
p.disconnect() 
