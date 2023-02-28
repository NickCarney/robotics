import pyrosim.pyrosim as pyrosim
import numpy as np
import pybullet as p
import constants as c
class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.motorValues = np.zeros(c.iterations)

    
    def Set_Value(self,robotId, desiredAngle):        
        pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = self.jointName,
        controlMode = p.POSITION_CONTROL,
        targetPosition = desiredAngle,
        maxForce = c.maxForce)
        
