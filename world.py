import pybullet as p
import pybullet_data
import constants as c
class WORLD :
    def __init__(self):
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        camTargetPos = [0, 0, c.verticalHeight]
        p.resetDebugVisualizerCamera( cameraDistance=5, cameraYaw=90, cameraPitch=320, cameraTargetPosition=camTargetPos)
        for i in range(20):
            self.planeId = p.loadURDF("plane.urdf", basePosition = [-3*(i-10),0,c.verticalHeight],globalScaling=.04)
            #print(4*i)

        
        
        

        p.loadSDF("world.sdf")