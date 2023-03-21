
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
        #print(self.parents)
        

    def Evolve(self):
        self.Evaluate(self.parents)
        for i in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()


    def Evolve_For_One_Generation(self):
        self.children = {}
        for key in self.parents.keys():
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID+=1
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        exit()
        # print('\n',"parent fitness:",self.parent.fitness,"child fitness:",self.child.fitness)
        # self.Select()

    def Spawn(self):
        #self.child = copy.deepcopy(self.parent)
        pass

    def Mutate(self):
        for key in self.children.keys():
            self.children[key].Mutate()
        
    def Evaluate(self, solutions):
        for i in range(c.populationSize):
            solutions[i].Start_Simulation('DIRECT')
        for i in range(c.populationSize):
            solutions[i].Wait_For_Simulation_To_End()
        pass

    def Select(self):      
        if(self.parent.fitness>self.child.fitness):
            self.parent = self.child

    def Show_Best(self):
        pass