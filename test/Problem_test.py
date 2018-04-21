#/usr/bin/python


from unittest import TestCase
import unittest
from scipy.io import loadmat
import numpy as np 

import sys
sys.path.append('..')
import os

from problem.DTLZ2 import DTLZ2Problem
DATADIR = os.getcwd()+'/matdata/'
NoneZero = 1e-15



#  from scipy.io import loadmat
#     dat = loadmat('test.mat')
#     A = dat['A']
#     B = dat['B']
#     N,_ = A.shape
#     print('*'*80)
#     for i in range(N):
#         genes = list(A[i,:])
#         ind = {'genes':genes}
#         evaluate(ind)
#         objects = np.array(ind['objects'])
#         FunctionValue = B[i,:]
#         diff = np.sum(objects - FunctionValue)
#         print(diff)
#         if diff >1e-15:
#             print("Failed:case")
#             print(genes)
#             print('diff=',diff)
#             print('='*15)

def diff_array(arr1 , arr2):
    
    diff = np.sum(arr1 -arr2)

    return np.abs(diff)

class ProblemTest(TestCase):
    def setUp(self):
        print('Problem Test')
       
    def test_DTZL2(self):
        data = loadmat(DATADIR+'DTLZ2_test.mat')
        A = data['A']
        B = data['B']
        N,D = A.shape
        N,M = B.shape
        problem = DTLZ2Problem(D,M)
        for i in range(N):
            genes = A[i,:]
            inds = {'genes':genes}
            inds = problem.evaluate(inds)
            objects = np.array(inds['objects'])
            FunctionValue = B[i,:]
            diff = diff_array(FunctionValue,objects)
            # if diff > NoneZero:
            #     print(diff)
            #     print(inds)
    
            self.assertTrue(diff/M < NoneZero,msg = inds)



    def tearDown(self):
        print('Problem test down')











if __name__ == '__main__':
    unittest.main()