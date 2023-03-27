import numpy as np
import pybullet as p
amplitude = np.pi/4
frequency = 12
offset = 0
zero = 0
gravity = -9.8
maxForce = 127
sleep = 1/240
array = np.linspace(0, 360, 1000)

length = 1
width = 1
height = 1
x = 0.0
y= 0.0
z = 1

populationSize = 1
numberOfGenerations = 1

backLegAmplitude = np.pi/4
backLegFrequency = 4
backLegPhaseOffset = 0
frontLegAmplitude = np.pi/2
frontLegFrequency = 12
frontLegPhaseOffset = np.pi/4
maxForce = 50

numMotorNeurons = 2
numSensorNeurons = 3