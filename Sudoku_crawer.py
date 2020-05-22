#!/usr/bin/env python
# coding: utf-8

# # import tool

# In[1]:


from bs4 import BeautifulSoup
from tqdm import tqdm
import requests
import numpy as np
import pandas as pd
from tqdm import tqdm
import sys
import time


# In[59]:


class sudoku_crawer:
    def __init__(self, hardness, howmany):
        self.url = "http://nine.websudoku.com/?level=%d" % hardness
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"}
        self.howmuch_ = howmany # 到底要爬幾個
        self.name_front = [" ", "Easy", "Medium", "Hard", "Evil"][hardness]
        self.name_index = 1
    
    def craw_one(self):
        try:
            r = requests.get(self.url, headers = self.headers)
            soup =  BeautifulSoup(r.text)

            buf = soup.find(id="cheat").get("value") # string
            answer = np.array(list(buf)).astype(int) # string -> numpy int        

            buf = soup.find(id="editmask").get("value") # string
            mask = np.array(list(buf)).astype(int) # string -> numpy int

            question = np.resize(answer * mask, (9, 9))

            save_name = "./data/%s_%d.npy" % (self.name_front, self.name_index)
            np.save(save_name, question)
            self.name_index = self.name_index + 1
        except:
            print("error")
    
    def craw_all(self):
        for i in tqdm(range(self.howmuch_)):
            time.sleep(0.5)
            self.craw_one()


# In[ ]:


if __name__ == "__main__": 
    hardness, howmany = int(sys.argv[1]), int(sys.argv[2])
    crawer = sudoku_crawer(hardness, howmany)
    crawer.craw_all()
    

