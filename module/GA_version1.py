#!/usr/bin/env python
# coding: utf-8

# # import tool

# In[1]:


import pandas as pd
import numpy as np
import random
from tqdm import tqdm

# In[5]:


class sub_grid:
    def __init__(self, input_):
        self.value = np.resize(input_, 9)
        self.answer = self.value.copy()
        self.answer_index = np.where(self.value == 0)[0]
        buf = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        putin = np.random.permutation(list(set(buf) - set(self.value)))
        self.answer[self.answer_index] = putin
        
    def mutation(self):
        (index_1, index_2) = random.sample(set(self.answer_index), 2)
        buf = self.answer[index_1]
        self.answer[index_1] = self.answer[index_2]
        self.answer[index_2] = buf
    
    def to_2d(self):
        buf = np.resize(self.answer, (3, 3))
        return(buf)


# In[6]:


class GA:
    def __init__(self, Question):
        self.Question = Question
        self.Population_Size = 500
        self.Mutation_Rate = 0.1
        self.Crossover_Rate = 0.5
        self.Elitism = 0.8
        self.Max_Generation = 50000
        self.parent_list = [self.Create_Parent() for _ in range(self.Population_Size)]
        self.tournament_size = 3
        self.fit_history = []
    
    def Create_Parent(self):
        block_1 = sub_grid(np.resize(self.Question[0:3, 0:3], 9))
        block_2 = sub_grid(np.resize(self.Question[0:3, 3:6], 9))
        block_3 = sub_grid(np.resize(self.Question[0:3, 6:9], 9))
        block_4 = sub_grid(np.resize(self.Question[3:6, 0:3], 9))
        block_5 = sub_grid(np.resize(self.Question[3:6, 3:6], 9))
        block_6 = sub_grid(np.resize(self.Question[3:6, 6:9], 9))
        block_7 = sub_grid(np.resize(self.Question[6:9, 0:3], 9))
        block_8 = sub_grid(np.resize(self.Question[6:9, 3:6], 9))
        block_9 = sub_grid(np.resize(self.Question[6:9, 6:9], 9))
        return([block_1, block_2, block_3, block_4, block_5, block_6, block_7, block_8, block_9])
    
    def Parent_to_2d(self, parent_):
        buf = np.zeros((9, 9)).astype(int)
        buf[0:3, 0:3] = parent_[0].to_2d()
        buf[0:3, 3:6] = parent_[1].to_2d()
        buf[0:3, 6:9] = parent_[2].to_2d()
        buf[3:6, 0:3] = parent_[3].to_2d()
        buf[3:6, 3:6] = parent_[4].to_2d()
        buf[3:6, 6:9] = parent_[5].to_2d()
        buf[6:9, 0:3] = parent_[6].to_2d()
        buf[6:9, 3:6] = parent_[7].to_2d()
        buf[6:9, 6:9] = parent_[8].to_2d()
        return(buf)
    
    def crossover(self, parent_0_, parent_1_):
        # 0 2 4 6 8 -> parent0
        # 1 3 5 7 -> parent 1
        buf = [None]*9
        buf[::2] = parent_0_[::2]
        buf[1::2] = parent_1_[1::2]  
        return(buf)
    
    def mutation(self, parent_):
        for i in range(9):
            parent_[i].mutation()
        return(parent_)
    
    def fitness(self, parent_):
        parent_2d = self.Parent_to_2d(parent_)
        all_numbers =set([1, 2, 3, 4, 5, 6, 7, 8, 9])
        sum_buf1 = sum([len(all_numbers - set(i)) for i in parent_2d])
        sum_buf2 = sum([len(all_numbers - set(i)) for i in parent_2d.T])
        return( -(sum_buf1 + sum_buf2) ) 
    
    def tournament(self):
        sampling = random.choices(self.parent_list, k = self.tournament_size)
        index = np.argmax([self.fitness(i) for i in sampling])
        #print([self.fitness(i) for i in sampling])
        #print(index)
        parent_ = sampling[ index  ]
        return(parent_)
    
    def new_child(self):
        p1 = self.tournament()
        p2 = self.tournament()
        #print('p1 p2')
        #print(self.Parent_to_2d(p1))
        #print(self.Parent_to_2d(p2))
        child = self.crossover(p1, p2)
        #print('child')
        #print(self.Parent_to_2d(child))
        weight_ = [1 - self.Mutation_Rate, self.Mutation_Rate]
        mutation_yes = random.choices([0, 1], weights = weight_)[0]
        if( mutation_yes ):
            child = self.mutation(child)
        
        return(child)
    
    def cycle(self):
        buf = [self.new_child() for _ in range(self.Population_Size)]
        
        index = np.argmax([self.fitness(i) for i in self.parent_list])
        best_ = self.parent_list[index]
        
        self.fit_history = self.fit_history + [self.fitness(best_)]
        
        weight_ = [1 - self.Elitism, self.Elitism]
        elitism_yes = random.choices([0, 1], weights = weight_)[0]
        print()
        if( elitism_yes ):
            print("elitism_yes")
            print(self.Parent_to_2d(best_))
            buf[0] = best_
        
        self.parent_list = buf 
    
    def control(self):
        for i in range(self.Max_Generation):
            self.cycle()
            
            if( self.fit_history[-1] == 0):
                break
                
        return(i)

