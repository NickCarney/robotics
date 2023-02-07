import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
iterations = 100
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = np.zeros(iterations)
frontLegSensorValues = np.zeros(iterations)
for i in range(iterations):
    time.sleep(1/60)
    #print(i)
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,
    jointName = b'Torso_BackLeg',
    controlMode = p.POSITION_CONTROL,
    targetPosition = 0.0,
    maxForce = 500)
    #print(frontLegSensorValues)
np.save('backLegSensorData.npy',backLegSensorValues)
np.save('frontLegSensorData.npy',frontLegSensorValues)
p.disconnect() 
