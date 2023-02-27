import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
import numpy as np
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:
    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain.nndf")


    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    def Sense(self,t):
        for i in self.sensors:
            self.sensors[i].Get_Value(t)
    def Prepare_To_Act(self):
        self.motors = {}
        for joint in pyrosim.jointNamesToIndices:
            self.motors[joint] = MOTOR(joint)
    def Act(self, t):
        for i in self.motors:
            self.motors[i].Set_Value(self.robotId,t)
    def Save_Values(self):
        np.save('data/motorValues.npy',self.motors)
        # np.save('data/flTargetAnglesData.npy',flTargetAngles)
    def Think(self):
        self.nn.Print()

        
        