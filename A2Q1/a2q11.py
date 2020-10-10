#!/usr/bin/env python
# coding: utf-8

# In[2]:


import import_ipynb
import math
import model 
from model import *

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
        current_Hypothesis,cost = model.fit(alpha,numOfSteps)
        print ("Current hypothesis: ",current_Hypothesis ,",  cost = ","{0:.4f}".format(cost))
    
setLine()


# In[ ]:





# In[ ]:




