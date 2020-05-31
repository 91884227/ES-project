#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import random
import itertools


# In[2]:


class Parent:
    def __init__(self, Question_):
        self.Blueprint = (Question_ > 0).astype(int)
        self.Blueprint_2 = (Question_ == 0).astype(int) # 質和Blueprint 相反
        self.Question = Question_
        
        buf = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        buf_2 = np.random.choice(buf, size = (9, 9), replace=True)
        self.nowvalue = self.Question*self.Blueprint + buf_2*self.Blueprint_2
    
    def mutation(self):
        buf = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        m_value = np.random.choice(buf, size = (9, 9), replace=True)
        buf = np.random.choice([0, 1], size = (9, 9), replace=True, p = [0.8, 0.2])
        index_yes = buf*self.Blueprint_2
        index_no = (index_yes == 0).astype(int)  
        replace_buf = m_value*index_yes + self.nowvalue*index_no
        self.nowvalue = replace_buf
    
    def __call__(self):
        print("now-value:")
        print(self.nowvalue)
        print("fitness: %d\n" % self.fitness()  )
    
    def remove_repetition_array(self, array_): # need to modify
        Gi_set = list(set([1, 2, 3, 4, 5, 6, 7, 8, 9]) - set(array_) )
        if(len(Gi_set) == 0):
            return(array_)
        else:
            change_value = np.random.choice(Gi_set, size = 9, replace = True)
            buf = []
            save = []
            for index, i in enumerate(array_):
                if(i in buf):
                    save = save + [change_value[index]]
                else:
                    buf = buf + [i]
                    save = save + [i]  
            return(save)
    
    def remove_repetition(self):
        after_row = np.array([self.remove_repetition_array(i) for i in self.nowvalue])
        after_replace_blue = after_row * self.Blueprint_2 + self.Question*self.Blueprint
        after_column = np.array([self.remove_repetition_array(i) for i in np.array(after_replace_blue).T]).T
        after_replace_blue2 = after_column * self.Blueprint_2 + self.Question*self.Blueprint
        self.nowvalue = after_replace_blue2
    
    def fitness_array(self, array_):
        buf = [array_[int(i[0])]!=array_[int(i[1])] for i in itertools.combinations('012345678', 2)]
        return( sum(buf) )
    
    def fitness(self):
        row_fitness = [self.fitness_array(i) for i in self.nowvalue]
        col_fitness = [self.fitness_array(i) for i in self.nowvalue.T]

        subsqure_to_array = [ list(self.nowvalue[3*int(iset[0]) : 3*(int(iset[0])+1), 3*int(iset[1]) : 3*(int(iset[1])+1)].reshape(-1)) 
                             for iset in itertools.product('012',  repeat=2)]
        subsqure_fitness = [self.fitness_array(i) for i in subsqure_to_array] 
        buf = sum(row_fitness) + sum(col_fitness) + sum(subsqure_fitness)
        return(buf)

