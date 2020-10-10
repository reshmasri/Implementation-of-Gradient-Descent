#!/usr/bin/env python
# coding: utf-8

# In[2]:


import import_ipynb
import math
import model 
from model import *
import matplotlib.pyplot as plt
import numpy as np

def setLine():
    
    alpha = 0.000000003
    numOfSteps = 100
    numOfLoops = 50
    model = LinearRegression()
    #feature
    x = list(range(0,1000))
    #label
    y = x
    for i in x:
        y = i      
        model.addSample(i,y)
    Samples = model.getSamples()
    Labels = model.getValues()
    for i in range(numOfLoops+1):
        model.fit(alpha,numOfSteps)
        plt.show()
   
      
setLine()


# In[ ]:




