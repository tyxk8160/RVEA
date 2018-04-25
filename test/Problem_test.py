#/usr/bin/python


from unittest import TestCase
import unittest
from scipy.io import loadmat
import numpy as np 

import sys
sys.path.append('..')
import os

from problem.DTLZ2 import DTLZ2Problem
from problem.DTLZ1 import DTLZ1Problem
DATADIR = os.getcwd()+'/matdata/'
NoneZero = 1e-15

def diff_array(arr1 , arr2):
    
    diff = np.sum(arr1 -arr2)

    return np.abs(diff)

class ProblemTest(TestCase):
    def setUp(self):
        print('Problem Test')
    def test_DTLZ1(self):
        problem = DTLZ1Problem(12)
        genes =  [0.0, 1.0, 0.70607866667857344, 0.60055488824334413, 0.45883227652574399, 0.39924952430070748, 0.77289816053946903, 0.40100069978861119, 0.39752072306612385, 0.59991465354026574, 0.39613970880561844, 0.50060258299241878]
        inds = {'genes':genes}
        inds = problem.evaluate(inds)
        print(inds)

       
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