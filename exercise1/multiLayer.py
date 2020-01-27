#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 10:16:14 2020

@author: gutama
"""



#%%
#used librariies and packages
import numpy as np
import matplotlib.pyplot as plt
from activations import Activations

from sklearn.datasets import make_moons

#%%





#%%
#Global variables
X,y = make_moons()
activation=Activations()

#%%



#%%
def scatter(X,y):
    
    fig,ax=plt.subplots()

    for i,j in enumerate(np.unique(y)):
        ax.scatter(X[y==j,0], X[y==j,1])
        

#%%




        
 #%%   
    
class Node():
    """
   
            
            
    
    """
    def __init__(self, input_data):
        """
        
        Node class is an blue print of a calculate the weighted sum for single 
        node:
        
        
        Parameters:
        ----------
                    - input_data:(array-like, shape) multidimensional array
                    
                            if the node is in first layer this is the training data points
                            if the node is in hidden layer the input data is the output of 
                            prevous layer
                
        Returns
        -------
        None.

        """
        self.X=input_data
        self.N=input_data.shape[0]
        self.d=input_data.shape[1]
        self.weights=np.random.random((self.d)) 
        
        
        
    def calculateWeightedSum(self):
        """
        Returns
        -------
        (array-like shape)
            Returns the weighted sum of a node for all data points in the input data.

        """
        return self.weights.T@self.X.T
        
        
  #%%      


#%%    
class Layer(Node):
 
   
    
   
    
    def __init__(self,layerInput,activation_function):
        """
        The layer class takes an input from prevous layer and calculate calcuate weighted 
    sum for all
    

        Parameters
        ----------
        layerInput : array-like, shape (Nxd)
            DESCRIPTION.
        activation_function : activation function
            DESCRIPTION.

        Returns
        -------
        None.

        """
        super().__init__(layerInput)
        self.f=activation_function
        self.layerInput=layerInput
        self.N =self.layerInput.shape[0]
        self.weighted_sum=np.ones((self.N,1))
        
        
       
        
        
    def addNodes(self):
        """
        

        Returns
        -------
        array-like:
            
            this functions returns a weigthsum of single 
            node for all input datas
        """
       
     
        ws=self.calculateWeightedSum().reshape(self.N,1)
        self.weighted_sum=np.concatenate((self.weighted_sum,ws),axis=1)
        return self
       
       #self.nodes.append(node.calculateWeightedSum())
  
    def calculateOutput(self):
        return self.f(self.weighted_sum[:,1:])
        
#%%
        
    
    
    
    
   #%% 

class ANN(Layer):
    
  
    
    
    #init
    def __init__(self,train_data,label,lrate):
        """
        

        Parameters
        ----------
        train_data : TYPE
            DESCRIPTION.
        label : TYPE
            DESCRIPTION.
        lrate : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        super().__init__(train_data,activation.softmax)
        self.train_data=train_data
        self.label=label
        self.lrate=lrate
        
        
        
        for i in range(train_data.shape[1]):
            self.addNodes()
       
        
        
        
        
        
        
    def addLayer(self):
        pass
    def train(self):
        pass
    def test(self):
        pass
    def backprogagate(self):
        pass
        
    
#%%    
    
    
   

        

    
  #%%  
    
if __name__=="__main__":
    ann=ANN(X,y,10)
    
#%%
