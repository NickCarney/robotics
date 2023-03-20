import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
from sensor import SENSOR
from motor import MOTOR
import os
class ROBOT:

    def __init__(self, solutionID):
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        fileToLoad = "brain"+str(solutionID)+".nndf"
        self.nn = NEURAL_NETWORK(fileToLoad)
        os.system("rm "+fileToLoad)
        #os.system("rm brain"+str(solutionID)+".nndf")
    
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
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                #print(neuronName,jointName,desiredAngle)
                for i in self.motors:
                    self.motors[i].Set_Value(self.robotId, desiredAngle)
            
    def Think(self):
        self.nn.Update()
        self.nn.Print()

    def Get_Fitness(self,solutionID):
        stateOfLink0 = p.getLinkState(self.robotId,0)
        positionOfLinkZero = stateOfLink0[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        f = open('tmp'+str(solutionID)+'.txt','w')
        os.system('mv tmp'+str(solutionID)+'.txt fitness'+str(solutionID)+'.txt')
        f.write(str(xCoordinateOfLinkZero))
        f.close()
        