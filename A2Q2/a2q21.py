#!/usr/bin/env python
# coding: utf-8

# In[1]:


import import_ipynb
import math
import model 
from model import *
import math

def setPlane():
    
    alpha =  0.000000003
    numOfSteps = 1000
    numOfLoops = 10
    model = LinearRegression()     
    noOfFeatures = 2
    x = list(range(0,1000))
    #calculating points for points((x,2x),5x)and ((2x,x),4x) 
    x1,y1 = x,[i*2 for i in x]   
    x2,y2 = [i*2 for i in x],x
    x  = x1 + x2
    y = y1 + y2
    #calculating z = x + 2y
    z = [(x[i] + 2*y[i])   for i in  range(len(x))] 
    #array of features as (x1,x2)
    features = list(zip(x, y))
  
    for i in range(len(z)):
        model.addSample(features[i],z[i])
    Samples = model.getSamples(noOfFeatures)
    Labels = model.getValues()
    for i in range(numOfLoops+1):
        current_Hypothesis,cost = model.fit(alpha,numOfSteps)
        print ("Current hypothesis: ",current_Hypothesis ,",  cost = ","{0:.4f}".format(cost))
    
setPlane()


# In[ ]:




