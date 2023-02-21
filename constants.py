import numpy as np
import pybullet as p
iterations = 1000
blAmplitude = np.pi/4
blFrequency = 12
blPhaseOffset = 0
flAmplitude = np.pi/16
flFrequency = 6
flPhaseOffset = 0
zero = 0
gravity = -9.8
maxForce = 127
sleep = 1/60
# physicsClient = p.connect(p.GUI)
# robotId = p.loadURDF("body.urdf")
# planeId = p.loadURDF("plane.urdf")
# p.loadSDF("world.sdf")
# backLegSensorValues = np.zeros(iterations)
# frontLegSensorValues = np.zeros(iterations)
#maxVal = amplitude * np.sin(frequency*iterations + phaseOffset)
blTargetAngles = blAmplitude*(np.sin((np.linspace(zero, 2*np.pi, iterations)*blFrequency)+blPhaseOffset))
flTargetAngles = flAmplitude*(np.sin((np.linspace(zero, 2*np.pi, iterations)*flFrequency)+flPhaseOffset))