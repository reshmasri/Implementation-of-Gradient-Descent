#!/usr/bin/env python
# coding: utf-8

# In[8]:


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
    iterations = 0
    # array for all values of theta
    theta = []
    #number of features
    n =0
    def __init__(self):
        return
        
    def addSample(self,x,y):
        self.Samples.append(x)       
        self.labels.append(y)
        return 
    
    def fit(self,alpha,numOfSteps):
        
        current_Hypothesis = self.__str__(self.n)
        cost = self.getLoss()
        
        for i in range(numOfSteps):   
            for j in range((self.n +1)):
                #calculating value of each theta for each dimention
                self.theta[j] = self.getTheta(j) - ((alpha)*(2/len(self.Samples))*(self.summation(j)))
                
            self.iterations = self.iterations + 1
            
        self.getIteration()  
                 
        return current_Hypothesis,cost
    def summation(self,j):
        summation = int(0)
        for i in range(len(self.Samples)):
            x = self.Samples[i]
            y = self.labels[i]

            if(j == 0):
                summation = summation + (self.getHypothesis(x,self.n) - y)
            else:
                summation = summation + ((x[j-1])*(self.getHypothesis(x,self.n) - y))
        return summation
    
    def getHypothesis(self,x,j):
        Hypothesis = self.getTheta(0)
        if(j == 0):
            Hypothesis = Hypothesis
        else:
            for f in range(1,j+1):
                Hypothesis = Hypothesis  + (self.getTheta(f) * (x[f-1])) 
        return Hypothesis
    
    def __str__(self,j):

        value = str("{0:.2f}".format(self.getTheta(0)))
        if(j == 0):
            value = value
        else:
            for f in range(1,j+1):
                value = value +  " + " + str("{0:.2f}".format(self.getTheta(f)))+ " x_" + str(f)
        return value
    
    def getLoss(self):
        
        summation  = 0
        for i in range(len(self.Samples)):
            x = self.Samples[i]
            y = self.labels[i]
            summation = summation + (pow((self.getHypothesis(x,self.n) - y),2))
               
        mse = (1/len(self.Samples)) * summation

        return mse
    
    def getTheta(self,j):
        theta = self.theta[j]
        return theta

    def getIteration(self):

        return self.iterations
    
    def getSamples(self,n):
        self.n = n
        self.theta = [0] * (n+1)
        return self.Samples
    
    def getValues(self):
        
        return self.labels
    


# In[ ]:




