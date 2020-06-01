#!/usr/bin/env python
# coding: utf-8

# # import tool

# In[53]:


import numpy as np
import pandas as pd
import random
import itertools
import time
from tqdm import tqdm
import copy

from module.Parent_for_TJGA import Parent

class TJGA:
    def __init__(self, Question_, print_fit_ = True, Iteration_ = 50):
        self.Question = Question_
        self.Population_size = 90
        self.Parent_list = [Parent(Question_) for _ in range(self.Population_size)]
        self.Child_list = []
        
        # Control Signal
        self.if_findsol = False
        self.Iteration = Iteration_
        self.print_fit = print_fit_       
        
       # save buffer
        self.sol = None
        self.fitness_list = []
        self.final_iternation = 0
        self.costtime = None
        
    def crossover(self):
        random.shuffle(self.Parent_list)
        self.Child_list = []
        for i in range(self.Population_size//2):
            parent_0 = copy.deepcopy( self.Parent_list[2*i+0] )
            parent_1 = copy.deepcopy( self.Parent_list[2*i+1] ) 

            for j in random.choices([0, 1], k=9):
                if( j ):
                    buf_0, buf_1 = parent_0.now_block[j], parent_1.now_block[j]
                    parent_0.now_block[j], parent_1.now_block[j] = buf_1, buf_0                   

            self.Child_list = self.Child_list + [parent_0] + [parent_1]        
    
    def Elitism(self):
        all_instance = self.Parent_list + self.Child_list
        all_fit_value = [i.fitness() for i in all_instance]
        # sort 
        all_instance.sort(key=dict(zip(all_instance, all_fit_value)).get)
        # update
        self.Parent_list = all_instance[:self.Population_size]
    
    def mutation(self):
        _ =  [i.mutation() for i in self.Parent_list]
        
    def Solution_Found(self, print_ = True ): 
        min_value = min( [i.fitness() for i in self.Parent_list] )
        if( print_):
            print("best_fitness: %d" % min_value)
        if( min_value == 0):
            # Control Signal
            self.if_findsol = True

            # save solution
            Parent_fit_value = [i.fitness() for i in self.Parent_list]
            self.Parent_list.sort(key = dict(zip(self.Parent_list, Parent_fit_value)).get)
            self.sol = self.Parent_list[0].return_value()
        else:
            self.fitness_list = self.fitness_list + [min_value]
    
    def main(self):
        tStart = time.time()
        for i in tqdm(range(1, self.Iteration+1)):
            if( i % 2000 == 0):
                print("reset at iteration %d" % i)
                self.Parent_list = [Parent(self.Question) for _ in range(self.Population_size)]
                
            if( self.if_findsol):
                break
            
            # crossover
            self.crossover()
            self.Elitism()
            self.Solution_Found(self.print_fit)
            
            # mutation
            self.mutation()
            self.Solution_Found(self.print_fit)
            
        tEnd = time.time()
        self.costtime = tEnd - tStart
        self.final_iternation = i
        print("It cost %f sec" % (tEnd - tStart))
        if( i == self.Iteration):
            print("Solution Not Found")
        else:
            print("find solution")
            print("final iteration: %d" % i)
            print(self.sol)     
