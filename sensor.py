import numpy as np
import constants as c
import pyrosim.pyrosim as pyrosim
class SENSOR :
    def __init__(self, linkname):
        self.linkName = linkname
        self.values = np.zeros(c.iterations)
        
    def Get_Value(self, t):
        self.values[t]= pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        
    def __del__(self):
        print(self.values)