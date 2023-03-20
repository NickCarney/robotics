
import constants as c
import copy
from solution import SOLUTION
import os
class PARALLEL_HILL_CLIMBER:
    
    def __init__(self):
        os.system('rm brain*.nnd')
        os.system('rm body*.nnd')
        self.nextAvailableID = 0
        self.parents = dict()
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID+=1
        print(self.parents)
        

    def Evolve(self):
        for i in range(c.populationSize):
            self.parents[i].Start_Simulation('GUI')
        for i in range(c.populationSize):
            self.parents[i].Wait_For_Simulation_To_End()
        for i in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()


    def Evolve_For_One_Generation(self):
        # self.Spawn()
        # self.Mutate()
        # self.child.Evaluate("DIRECT")
        # print('\n',"parent fitness:",self.parent.fitness,"child fitness:",self.child.fitness)
        # self.Select()
        pass

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()
        

    def Select(self):      
        if(self.parent.fitness>self.child.fitness):
            self.parent = self.child

    def Show_Best(self):
        pass