import numpy as np
import pybullet as p
iterations = 1000
amplitude = np.pi/4
frequency = 12
offset = 0
zero = 0
gravity = -9.8
maxForce = 127
sleep = 1/240
array = np.linspace(0, 360, 1000)

backLegAmplitude = np.pi/4
backLegFrequency = 4
backLegPhaseOffset = 0
frontLegAmplitude = np.pi/2
frontLegFrequency = 12
frontLegPhaseOffset = np.pi/4
maxForce = 50
# backLegSensorValues = np.zeros(iterations)
# frontLegSensorValues = np.zeros(iterations)
#maxVal = amplitude * np.sin(frequency*iterations + phaseOffset)
#blTargetAngles = blAmplitude*(np.sin((np.linspace(zero, 2*np.pi, iterations)*blFrequency)+blPhaseOffset))
#flTargetAngles = flAmplitude*(np.sin((np.linspace(zero, 2*np.pi, iterations)*flFrequency)+flPhaseOffset))