#!/usr/bin/env python
# coding: utf-8

# # import tool

# In[1]:


import numpy as np
import pandas as pd
import random
import itertools
from tqdm import tqdm


# # import self-define module

# In[2]:


from module.Parent_for_RetGA import Parent


# # Read data in

# In[5]:


class Ret_GA:
    def __init__(self, Question_, print_fit_ = True, Iteration_ = 50):
        self.Question = Question_
        self.Parent_list = [Parent(Question_) for _ in range(10*9)]
        self.Child_list = []
        
        # Control Signal
        self.if_findsol = False
        self.Iteration = Iteration_
        self.print_fit = print_fit_
        
        given = sum(sum(self.Parent_list[0].Blueprint))
        if( given <=27):
            self.resetpoint = 2000
        elif(28<=given <=29):
            self.resetpoint = 350
        elif(30<=given <=31):
            self.resetpoint = 300
        elif(given >=32):
            self.resetpoint = 200
        else:
            print("error in self.resetpoint")
        print("resetpoint:%d" % self.resetpoint)
        
        # save buffer
        self.sol = None
        self.fitness_list = []
        self.final_iternation = 0
        
    def crossover(self):
        random.shuffle(self.Parent_list)
        self.Child_list = []
        for i in range(45):
            parent_1 = self.Parent_list[2*i+0]
            parent_2 = self.Parent_list[2*i+1]
            if( random.choice([1, 1, 1, 1, 1, 1, 1, 1, 0, 0]) ):
                change_row = random.choice([1, 2, 3, 4, 5, 6, 7])
                # child_1
                buf_Parent = Parent(self.Question)
                buf_1 = parent_1.nowvalue[0:change_row]
                buf_2 = parent_2.nowvalue[change_row:]
                buf_Parent.nowvalue = np.concatenate((buf_1, buf_2), axis=0)
                self.Child_list = self.Child_list + [buf_Parent]

                # child_2
                buf_Parent = Parent(self.Question)
                buf_1 = parent_2.nowvalue[0:change_row]
                buf_2 = parent_1.nowvalue[change_row:]
                buf_Parent.nowvalue = np.concatenate((buf_1, buf_2), axis=0)
                self.Child_list = self.Child_list + [buf_Parent] 
            else:
                self.Child_list = self.Child_list + [parent_1] + [parent_2]
        
    def Elitism(self):
        all_instance = self.Parent_list + self.Child_list
        all_fit_value = [i.fitness() for i in all_instance]
        # sort 
        all_instance.sort(key=dict(zip(all_instance, all_fit_value)).get, reverse = True)
        # update
        self.Parent_list = all_instance 
        
    def mutation(self):
        _ =  [i.mutation() for i in self.Parent_list]
    
    def Remove_Repetition(self):
        _ =  [i.remove_repetition() for i in self.Parent_list]
    
    def Solution_Found(self, print_ = True ): 
        max_value = max( [i.fitness() for i in self.Parent_list] )
        if( print_):
            print("best_fitness: %d" % max_value)
        if( max_value == 972):
            # Control Signal
            self.if_findsol = True

            # save solution
            Parent_fit_value = [i.fitness() for i in self.Parent_list]
            self.Parent_list.sort(key = dict(zip(self.Parent_list, Parent_fit_value)).get, 
                                  reverse = True)
            self.sol = self.Parent_list[0].nowvalue
        else:
            self.fitness_list = self.fitness_list + [max_value]
    
    def main(self):
        for i in tqdm(range(1, self.Iteration+1)):
            if( i%self.resetpoint == 0):
                print("reset at iteration %d" % i)
                self.Parent_list = [Parent(Question_) for _ in range(10*9)]
            if( self.if_findsol):
                break

            # first 
            self.crossover()
            self.Remove_Repetition()
            self.Solution_Found(self.print_fit)

            # secound
            self.mutation()
            self.Remove_Repetition()
            self.Solution_Found(self.print_fit)

            # third
            self.Elitism()

        self.final_iternation = i
        if( i == self.Iteration):
            print("Solution Not Found")
        else:
            print("find solution")
            print("final iteration: %d" % i)
            print(self.sol)        
    

