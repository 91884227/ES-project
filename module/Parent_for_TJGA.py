#!/usr/bin/env python
# coding: utf-8

# # import tool

# In[8]:


import numpy as np
import pandas as pd
import random
import itertools


# In[266]:


# Question_ = np.load("./data/Easy_1.npy")
# Question_ = np.load("./data/Perfect_1.npy")
# Question_ 


# In[267]:


class block:
    def __init__(self, array_):
        self.init = np.resize(array_, 9)
        self.ifgiven = (self.init > 1).astype(int)
        self.ifnotgiven = (self.init == 0).astype(int)
        
        buf = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        put_in = list(np.random.permutation(list(set(buf) - set(self.init))))
        self.nowvalue = [i if i > 0 else put_in.pop(0) for i in self.init]
    
    def __call__(self):
        print("block:")
        print(np.resize(self.nowvalue, (3, 3)))
        print("nowvalue:")
        print(self.nowvalue)
    
    def mutation(self):
        if( random.choice([0, 0, 0, 0, 1, 1, 1, 1, 1, 1]) ):
            buf = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            index_1, index_2 = random.choice(buf), random.choice(buf)
            if_choose_given = ( self.ifgiven[index_1] + self.ifgiven[index_2] ) > 0
            if( not if_choose_given):
                # print("mutation_yes")
                buf_1, buf_2 = self.nowvalue[index_1], self.nowvalue[index_2]
                self.nowvalue[index_1], self.nowvalue[index_2] = buf_2, buf_1
    def return_value(self):
        return(np.resize(self.nowvalue, (3, 3)) )


# In[268]:


# test = block(np.array([[ 0, 0, 0], [9, 0, 4], [ 0, 5, 6]]))

# test()


# In[269]:


class Parent:
    def __init__(self, Question_):
        self.Question = Question_
        block_1 = block(self.Question[0:3, 0:3])
        block_2 = block(self.Question[0:3, 3:6])
        block_3 = block(self.Question[0:3, 6:9])
        block_4 = block(self.Question[3:6, 0:3])
        block_5 = block(self.Question[3:6, 3:6])
        block_6 = block(self.Question[3:6, 6:9])
        block_7 = block(self.Question[6:9, 0:3])
        block_8 = block(self.Question[6:9, 3:6])
        block_9 = block(self.Question[6:9, 6:9])
        self.now_block = [block_1, block_2, block_3, 
                          block_4, block_5, block_6, 
                          block_7, block_8, block_9]
    def __call__(self):
        print("now_block value:")
        print(self.return_value())
        print("fitness:")
        print(self.fitness())
        
    def mutation(self):
        _ = [i.mutation() for i in self.now_block]
    
    def return_value(self):
        buf = np.zeros((9, 9)).astype(int)
        buf[0:3, 0:3] = self.now_block[0].return_value()
        buf[0:3, 3:6] = self.now_block[1].return_value()
        buf[0:3, 6:9] = self.now_block[2].return_value()
        buf[3:6, 0:3] = self.now_block[3].return_value()
        buf[3:6, 3:6] = self.now_block[4].return_value()
        buf[3:6, 6:9] = self.now_block[5].return_value()
        buf[6:9, 0:3] = self.now_block[6].return_value() 
        buf[6:9, 3:6] = self.now_block[7].return_value()
        buf[6:9, 6:9] = self.now_block[8].return_value()   
        return(buf)
    
    def fitness(self):
        buf = self.return_value()
        all_number = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

        row_fit = [ len(all_number - set(i)) for i in buf]
        col_fit = [ len(all_number - set(i)) for i in buf.T]

        fitness = sum(row_fit) + sum(col_fit)

        return(fitness)        


# In[270]:


# test = Parent(Question_)
# test.mutation()
# test.fitness()

