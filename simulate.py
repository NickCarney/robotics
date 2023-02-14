import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random as rand
iterations = 1000
amplitude = np.pi/4   
frequency = 1
phaseOffset = 0
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = np.zeros(iterations)
frontLegSensorValues = np.zeros(iterations)
maxVal = amplitude * np.sin(frequency*iterations + phaseOffset)
targetAngles = np.sin(np.linspace(0, 2*np.pi, iterations)*frequency+phaseOffset)
np.save('data/targetAnglesData.npy',targetAngles)
exit()
for i in range(iterations):
    time.sleep(1/60)
    #print(i)
    p.stepSimulation()
    #targetAngles[i] = amplitude * np.sin(frequency*i + phaseOffset)
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,
    jointName = b'Torso_BackLeg',
    controlMode = p.POSITION_CONTROL,
    targetPosition = np.sin(targetAngles[i]),#rand.uniform(-np.pi/2,np.pi/2),
    maxForce = 127)
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,
    jointName = b'Torso_FrontLeg',
    controlMode = p.POSITION_CONTROL,
    targetPosition = np.sin(targetAngles[i]),#rand.uniform(-np.pi/2,np.pi/2),
    maxForce = 127)
    #print(frontLegSensorValues)
np.save('backLegSensorData.npy',backLegSensorValues)
np.save('frontLegSensorData.npy',frontLegSensorValues)
p.disconnect() 
