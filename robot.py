import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
from sensor import SENSOR
from motor import MOTOR
import constants as c
import os

class ROBOT:

    def __init__(self,solutionID):
        self.robotId = p.loadURDF("body.urdf",basePosition=[0,0,c.verticalHeight])
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain" + str(solutionID) + ".nndf")
        os.system("rm brain" + str(solutionID) + ".nndf")
    
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    
    def Sense(self, t):
        for i in self.sensors:
            self.sensors[i].Get_Value(t)
            
    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
            
    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                #print(neuronName,jointName,desiredAngle)
                for i in self.motors:
                    self.motors[i].Set_Value(self.robotId, desiredAngle)
            
    def Think(self):
        self.nn.Update()
        self.nn.Print()
        
    def Get_Fitness(self, solutionID):
        stateOfLinkZero = p.getLinkState(self.robotId,0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        yCoordinateOfLinkZero = positionOfLinkZero[2]
        f = open("tmp" + str(solutionID) + ".txt", "w")
        f2 = open("tmp2" + str(solutionID) + ".txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        f2.write(str(yCoordinateOfLinkZero))
        f.close()
        f2.close()
        os.system("mv tmp" + str(solutionID) + ".txt " "fitness" + str(solutionID) + ".txt")
        os.system("mv tmp2" + str(solutionID) + ".txt " "fitnessy" + str(solutionID) + ".txt")