# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import numpy as np

#spftmax activation function 





class Activations():
    def softmax(self,x):
        A=np.exp(x)
        print(A)
        sum_=A.sum(1).reshape(A.shape[0],1)
        print(sum_)
        return A/sum_
        
        
    
