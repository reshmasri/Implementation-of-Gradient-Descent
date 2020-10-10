#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import import_ipynb
import math
import model 
from model import *
from random import seed
from random import randint
from random import random
import numpy as np

def randomLine():
    seed(1)
    alpha = 0.000003
    numOfSteps = 1000
    numOfLoops = 250
    model = LinearRegression() 
    #generating feature x
    x = np.random.uniform(low=-4, high=6, size=(500,))
    #generating coeffient and constant
    a = float(np.random.uniform(low=-5, high=10, size=(1,)))
    b = float(np.random.uniform(low=-5, high=5, size=(1,)))
    #adding gaussian noise
    noise = np.random.normal(0,1,500)
#   labels
    y=[]
    for i in range(len(x)):
        t = a*x[i] + b + noise[i]
        y.append(t)
        
    for i in range(len(x)):
        model.addSample(x[i],y[i])    
    Samples = model.getSamples()
    Labels = model.getValues()
    for i in range(numOfLoops+1):
        current_Hypothesis,cost = model.fit(alpha,numOfSteps)
        print ("Current hypothesis: ",current_Hypothesis ,",  cost = ","{0:.4f}".format(cost))
    
randomLine()


# In[ ]:





# In[ ]:




