import pybullet as p
import pybullet_data
import constants as c
class WORLD :
    def __init__(self):
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        camTargetPos = [0, 0, 100]
        p.resetDebugVisualizerCamera( cameraDistance=5, cameraYaw=10, cameraPitch=330, cameraTargetPosition=camTargetPos)
        for i in range(10):
            self.planeId = p.loadURDF("plane.urdf", basePosition = [0,3*i,c.verticalHeight],globalScaling=.017)
            print(4*i)

        
        
        

        p.loadSDF("world.sdf")