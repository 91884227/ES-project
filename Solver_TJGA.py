#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import json
import sys


# In[2]:


from module.TJGA import TJGA


# In[ ]:


if __name__ == '__main__':
    QUESTION_NAME = sys.argv[1]
    PRINT_FIT = int(sys.argv[2])
    ITERATION = int(sys.argv[3])
    ID = sys.argv[4]

    print("read data...")
    # Question = np.load("./data/Easy_1.npy")
    Question = np.load("./data/%s.npy"% QUESTION_NAME) 

    print("start to slove...")
    solver = TJGA(Question, print_fit_ = PRINT_FIT, Iteration_ = ITERATION)
    solver.main()

    print("save result...")
    dic = {"costtime":solver.costtime, 
           "final_iternation":solver.final_iternation}
    # for time and iteration
    savename = "./save_result/%s_%s_TJGA.json" % (QUESTION_NAME, ID)
    with open(savename, 'w') as outfile:
        json.dump(dic, outfile)

    # for solution
    np.save("./save_result/%s_.npy" % (QUESTION_NAME), solver.sol)

