
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
            print("\nGeneration",i+1)
            self.Evolve_For_One_Generation()


    def Evolve_For_One_Generation(self):
        self.children = {}
        self.Spawn()
        self.Mutate()
        #self.Evaluate(self.children)
        self.Print()
        # print('\n',"parent fitness:",self.parent.fitness,"child fitness:",self.child.fitness)
        self.Select()

    def Spawn(self):
        for i in self.parents:
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for i in self.children:
            self.children[i].Mutate()
        
    def Evaluate(self, solutions):
        for x in solutions:
            solutions[x].Start_Simulation("DIRECT")
        for x in solutions:
            solutions[x].Wait_For_Simulation_To_End()

    def Select(self):      
        for i in self.parents:
            #if abs(self.parents[i].fitness) < abs(self.children[i].fitness) and (abs(self.children[i].fitnessy) < 2):
            if(self.parents[i].fitness > self.children[i].fitness and self.children[i].fitnessy >=c.verticalHeight):
                self.parents[i] = self.children[i]

    def Show_Best(self):
        best = 10
        for i in self.parents:
            #if abs(self.parents[i].fitness) > abs(best) and (abs(self.children[i].fitnessy) < 2):
            if(self.parents[i].fitness < best and self.parents[i].fitnessy > 100):
                best = self.parents[i].fitness
                best_key = i
        print('Best fitness obtained:',self.parents[best_key].fitness)
        self.parents[best_key].Start_Simulation("GUI")

    def Print(self):
        for i in self.parents.keys():
            print("\n")
            print(self.parents[i].fitness,self.children[i].fitness,"\n")