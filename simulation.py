import pybullet as p
import constants as c
import pybullet_data
import pyrosim.pyrosim as pyrosim
from world import WORLD
from robot import ROBOT
class SIMULATION:
    def __init__(self):
        
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(c.zero,c.zero,c.gravity)
        self.world = WORLD()
        self.robot = ROBOT()
        pyrosim.Prepare_To_Simulate(self.robot.robotId)
    def Run():
        for i in range(c.iterations):
            print(i)
            # time.sleep(c.sleep)
            # #print(i)
            # p.stepSimulation()
            # #targetAngles[i] = amplitude * np.sin(frequency*i + phaseOffset)
            # backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            # frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
            # pyrosim.Set_Motor_For_Joint(
            # bodyIndex = self.robot.robotId,
            # jointName = b'Torso_BackLeg',
            # controlMode = p.POSITION_CONTROL,
            # targetPosition = np.sin(blTargetAngles[i]),
            # maxForce = c.maxForce)
            # pyrosim.Set_Motor_For_Joint(
            # bodyIndex = robotId,
            # jointName = b'Torso_FrontLeg',
            # controlMode = p.POSITION_CONTROL,
            # targetPosition = np.sin(flTargetAngles[i]),
            # maxForce = c.maxForce)
            # #print(frontLegSensorValues)

            
