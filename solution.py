import numpy as np
import pyrosim.pyrosim as pyrosim
import constants as c
import os
import random
import time
class SOLUTION:

    
    def __init__(self,nextAvailableID):
        self.weights = np.array([[np.random.rand(),np.random.rand()],[np.random.rand(),np.random.rand()],[np.random.rand(),np.random.rand()]])
        self.weights = self.weights * 2 - 1
        self.myId = nextAvailableID
        
    #def Evaluate(self,directOrGUI):
        
        

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()   
        os.system("python3 simulate.py " + directOrGUI + " "+str(self.myId)+" &")

    def Wait_For_Simulation_To_End(self):
        # fitnessFileName = 'fitness'+str(self.myId)+'.txt'
        # while not os.path.exists(fitnessFileName):
        #     time.sleep(0.01) 
        # f = open(fitnessFileName,'r')
        # print(fitnessFileName)
        # self.fitness = float(f.read())
        # #print(self.fitness)
        # f.close()
        # os.system('rm '+fitnessFileName)

        while not os.path.exists("fitness" + str(self.myId) + ".txt"):
            time.sleep(0.01)       
        f = open("fitness" + str(self.myId) + ".txt", "r")
        self.fitness = float(f.read())
        f.close()
        os.system("rm fitness" + str(self.myId) + ".txt")

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[3,3,c.z] , size=[c.length,c.width,c.height])    
        pyrosim.End()
    
    ##def Create_Robot():
        
        
    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[c.x,c.y,c.z] , size=[c.length,c.width,c.height])
        pyrosim.Send_Joint( name = "Torso_Backleg" , parent= "Torso" , child = "Backleg" , type = "revolute", position = [-0.5,0.0,1])
        pyrosim.Send_Cube(name="Backleg", pos=[-0.5,0,-0.5] , size=[c.length,c.width,c.height])
        pyrosim.Send_Joint( name = "Torso_Frontleg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = [0.5,0,1.0])
        pyrosim.Send_Cube(name="Frontleg", pos=[0.5,0,-0.5] , size=[c.length,c.width,c.height])
        pyrosim.End()
        
    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain"+str(self.myId)+".nndf")
        
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "Backleg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "Frontleg")
        
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_Backleg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_frontleg")
        for currentRow in range(self.weights.shape[0]):
            for currentColumn in range(self.weights.shape[1]):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+3 , weight = self.weights[currentRow][currentColumn] )
        
        
        pyrosim.End()

    def Mutate(self):
        randomRow = random.randint(0,2)
        randomColumn = random.randint(0,1)
        self.weights[randomRow][randomColumn] = random.random()*2-1

    def Set_ID(self,nextAvailableID):
        self.myId = nextAvailableID
        nextAvailableID+=1

    