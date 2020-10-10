#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import urllib.request
import os
import gzip 
import shutil
import matplotlib.pyplot as plt
from itertools import product
import math


class LinearRegression:
    
    Samples = []
    labels = []
    theta0 = 0
    theta1 = 0  
    iterations = 0
    def __init__(self):
        return
        
    def addSample(self,x,y):

        self.Samples.append(x)
        self.labels.append(y)
        return 
    
    def fit(self,alpha,numOfSteps):
    
        current_Hypothesis = self.__str__()
        cost = self.getLoss()
        
        for i in range(numOfSteps):    
            
            summation0 = int(0)
            summation1 = int(0)
            for i in range(len(self.Samples)):
                x = self.Samples[i]
                y = self.labels[i]
                summation0 = summation0 + (self.getHypothesis(x) - y)
                summation1 = summation1 + (x*(self.getHypothesis(x) - y))

            self.theta0 = self.getTheta0() - ((alpha)*(2/len(self.Samples))*(summation0))
            self.theta1 = self.getTheta1() - ((alpha)*(2/len(self.Samples))*(summation1))  

            self.iterations = self.iterations + 1
            
        self.getIteration()  
                 
        return current_Hypothesis,cost
    
    def getHypothesis(self,x):

        Hypothesis =  self.getTheta0() + (self.getTheta1() * pow(x,1))   
        
        return Hypothesis
    
    def __str__(self):
        
        value = str("{0:.2f}".format(self.getTheta0()))+ " + " + str("{0:.2f}".format(self.getTheta1()))+ " x"
        return value
    
    def getLoss(self):
        
        summation  = 0
        for i in range(len(self.Samples)):
            x = self.Samples[i]
            y = self.labels[i]
            summation = summation + (pow((self.getHypothesis(x) - y),2))
               
        mse = (1/len(self.Samples)) * summation

        return mse
    
    def getTheta0(self):
      
        return self.theta0
    
    def getTheta1(self):
    
        return self.theta1
    
    def getIteration(self):

        return self.iterations
    
    def getSamples(self):
        
        return self.Samples
    
    def getValues(self):
        
        return self.labels
    


# In[ ]:




