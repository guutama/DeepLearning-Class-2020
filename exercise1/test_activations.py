# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 09:42:07 2020

@author: gmo028
"""




#%%
import unittest 
import activations
from activations import Activations as A

import numpy as np 

#%%




#Global variables

#%%
data=np.array([[10,10],[8,8],[6,6],[4,4],[2,2]])

true_result=np.array([[0.5,0.5],[0.5,0.5],[0.5,0.5],[0.5,0.5],[0.5,0.5]])
#%%



#%%
class TestActivations(unittest.TestCase):
    
    
    def test_softmax(self):
        """
        

        Returns
        -------
        None.

        """
        a=A()
        result=a.softmax(data)
        #self.assertequal(result,)
        np.allclose(result,true_result)
        
        
        
        
#%%
    
    
    
    

#%%

if __name__=="__main__":
    
    unittest.main()
    
  #%% 
    
    
    
    
    