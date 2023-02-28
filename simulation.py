import pybullet as p
import constants as c
import pybullet_data
import pyrosim.pyrosim as pyrosim
from world import WORLD
from robot import ROBOT
from sensor import SENSOR
from motor import MOTOR
import numpy as np
import time
class SIMULATION:
    def __init__(self):
        
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(c.zero,c.zero,c.gravity)
        self.world = WORLD()
        self.robot = ROBOT()
        #self.sensor = SENSOR()
        
    def Run(self):
        for i in range(c.iterations):
            print(i)
            time.sleep(c.sleep)
            #print(i)
            p.stepSimulation()
            #self.robot.Prepare_To_Sense()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            #targetAngles[i] = amplitude * np.sin(frequency*i + phaseOffset)
            
            
            #print(frontLegSensorValues)
    def __del__(self):     
        p.disconnect()
            
