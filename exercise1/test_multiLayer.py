#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 10:17:27 2020

@author: gutama
"""


import problem2_2
import numpy as np
import unittest 





#%%

class testProblem2_2(unittest.TestCase):
    
    
    
    
    def testNode(self):
        """
        Test The Node Class

        Returns
        -------
        None.

        """
        n=problem2_2.Node(np.ones((3,3)))
        result=n.weights.shape
        
        self.assertEqual(result, (3,1))
        
        
        
        





#%%
        
   


     
        
 #%%       

tes=testProblem2_2()
tes.testNode()
 #%%       
