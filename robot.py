import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
class ROBOT:
    def __init__(self):
        
        self.motors = {}
        self.robotId = p.loadURDF("body.urdf")
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    def Sense():
        backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
        