import pyrosim.pyrosim as pyrosim
import numpy as np
import pybullet as p
import constants as c
class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.motorValues = np.zeros(c.iterations)
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self. offset = c.offset
        print(self.jointName)
        if self.jointName == b'Torso_BackLeg':
            self.motorValues = self.amplitude*(np.sin((np.linspace(c.zero, 2*np.pi, c.iterations)*self.frequency)+self.offset))
        elif self.jointName == b'Torso_FrontLeg':
            self.motorValues = self.amplitude*(np.sin((np.linspace(c.zero, 2*np.pi, c.iterations)*self.frequency*.5)+self.offset))
        
    def Set_Value(self,robotId, desiredAngle):        
        pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = self.jointName,
        controlMode = p.POSITION_CONTROL,
        targetPosition = self.motorValues[desiredAngle],
        maxForce = c.maxForce)
        
