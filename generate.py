import pyrosim.pyrosim as pyrosim
length=1
width=1
height=1
x=-.5
y=0
z=-.5
pyrosim.Start_SDF("boxes.sdf")
#pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
#pyrosim.Send_Cube(name="Box2", pos=[x+1,y,z+1] , size=[length,width,height])
adder=0
for xc in range(10):
    for yc in range(10):
        for i in range(10):
            adder+=height
            print(height)
            print((z+adder))
            pyrosim.Send_Cube(name="Box", pos=[x+xc,y+yc,z+adder] , size=[length,width,height])
            length*=.9
            width*=.9
            height*=.9
        adder=0
        length=1
        width=1
        height=1

pyrosim.End()