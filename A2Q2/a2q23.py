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

def randomDimension(noOfFeatures):
    
    seed(1)
    alpha = 0.00003
    numOfSteps = 1000
    numOfLoops = 100
    noise = 20
    model = LinearRegression() 
    examples = 5000
    #array of coefﬁcient
    t = []
    #array of all features of each 5000 examples
    x = []
    # array of r - label 
    r = []
    #array of product of coefﬁcient and x for each dimention
    tx = []
    #array of features as (x1,x2...xn)
    features = []
    #generating random variable for each coefﬁcient t0 in assignment
    t0 = float(np.random.uniform(low=-100, high=100, size=(1,)))
    for i in range(1,noOfFeatures+1):
        #generating random variable for each coefﬁcient t in assignment
        a = float(np.random.uniform(low=-100, high=100, size=(1,)))
        t.append(a)
        #generating random variable for each feature x in assignment
        x1 = np.random.uniform(low=0, high=1, size=(5000,))
        x.append(list(x1))
        #poduct of coefﬁcient and x 
        p = list(a*x1)
        tx.append(p)

    for j in range(examples):
        #summation of poduct of coefﬁcient and x for each sample
        z = sum(i[j] for i in tx)
        #adding noise and t0 to find r to the summation
        y = z + t0 + noise
        r.append(y)
        g =[i[j] for i in x]
        features.append(g)

    for i in range(len(r)):
        model.addSample(features[i],r[i])
    Samples = model.getSamples(noOfFeatures)
    Labels = model.getValues()
    for i in range(numOfLoops+1):
        current_Hypothesis,cost = model.fit(alpha,numOfSteps)
        print ("Current hypothesis: ",current_Hypothesis ,",  cost = ","{0:.4f}".format(cost))
    
randomDimension(5)

# In[ ]:




