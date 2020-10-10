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

def rabndomLine():
    seed(1)
    alpha = 0.003
    numOfSteps = 1000
    numOfLoops = 100
    noise = 20
    noOfFeatures = 2
    model = LinearRegression() 
    x = []
    #generationg the values for variables given in assignment
    x1 = np.random.uniform(low=0, high=1, size=(5000,))
    x2 = np.random.uniform(low=0, high=1, size=(5000,))
    #generationg the values for coeffients given in assignment
    a = float(np.random.uniform(low=-100, high=100, size=(1,)))
    b = float(np.random.uniform(low=-100, high=100, size=(1,)))
    c = float(np.random.uniform(low=-20, high=20, size=(1,)))
    #generationg the value for noise given in assignment
    delta = np.random.uniform(low=-100, high=100, size=(5000,))
    #calculating the label
    y = [(a*x1[i] + b*x2[i] + c+ delta[i])   for i in  range(len(x1))] 
    #array of features as (x1,x2)
    features = list(zip(x1, x2))
    

    for i in range(len(y)):
        model.addSample(features[i],y[i])
    Samples = model.getSamples(noOfFeatures)
    Labels = model.getValues()
    for i in range(numOfLoops+1):
        current_Hypothesis,cost = model.fit(alpha,numOfSteps)
        print ("Current hypothesis: ",current_Hypothesis ,",  cost = ","{0:.4f}".format(cost))
    
rabndomLine()
