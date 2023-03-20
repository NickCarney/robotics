
import constants as c
import copy
from solution import SOLUTION
class PARALLEL_HILL_CLIMBER:
    
    def __init__(self):
        self.parents = dict()
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION()
        print(self.parents)

    def Evolve(self):
        for i in range(c.populationSize):
            self.parents[i].Evaluate('GUI')
        # for currentGeneration in range(c.numberOfGenerations):
        #     self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        print('\n',"parent fitness:",self.parent.fitness,"child fitness:",self.child.fitness)
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()
        

    def Select(self):      
        if(self.parent.fitness>self.child.fitness):
            self.parent = self.child

    def Show_Best(self):
        pass