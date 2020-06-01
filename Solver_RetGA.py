#!/usr/bin/env python
# coding: utf-8

# # import tool

# In[23]:


import pandas as pd
import numpy as np
import json
import sys


# # import self-define tool

# In[2]:


from module.RetGA import Ret_GA


# In[3]:


# QUESTION_NAME = "Perfect_1"
# PRINT_FIT = 0
# ITERATION = 5
# ID = str(0000)

if __name__ == '__main__':
    QUESTION_NAME = sys.argv[1]
    PRINT_FIT = int(sys.argv[2])
    ITERATION = int(sys.argv[3])
    ID = sys.argv[4]

    print("read data...")
    # Question = np.load("./data/Easy_1.npy")
    Question = np.load("./data/%s.npy"% QUESTION_NAME) 

    print("start to slove...")
    solver = Ret_GA(Question, print_fit_ = PRINT_FIT, Iteration_ = ITERATION)
    solver.main()

    print("save result...")
    dic = {"costtime":solver.costtime, 
           "final_iternation":solver.final_iternation}
    # for time and iteration
    savename = "./save_result/%s_%s_RetGA.json" % (QUESTION_NAME, ID)
    with open(savename, 'w') as outfile:
        json.dump(dic, outfile)

    # for solution
    np.save("./save_result/%s_.npy" % (QUESTION_NAME), solver.sol)

