#/usr/bin/python
import unittest
from unittest import TestCase


import sys
sys.path.append('..')
from util.PopulationUtil import CreatePopulation,initpopulation,evaluate_pop
from problem.DTLZ2 import DTLZ2Problem
import numpy as np


class Utiltest(TestCase):
    def setup(self):
        print('PoulationUtil')
    def tearDown(self):
        print('testdown')
    
    def test_createpopulation(self):
        print('CreatePopulation')
        PopDesc = np.arange(12).reshape(4,3)
        pop = CreatePopulation(PopDesc)
        for i in range(4):
            x = list(pop[i]['genes'])
            y = list(PopDesc[i,:])
            self.assertEqual(x,y,msg = pop[i])
    def test_initialpopulation(self):
        pop = initpopulation(4,3,0.0,1.0)
        self.assertEqual(len(pop),4,msg = 'length is error')
      

    def test_evaluatepop(self):
        problem = DTLZ2Problem(7)
        pop = initpopulation(6,7,np.array(problem.lower),np.array(problem.upper))
        pop = evaluate_pop(pop,problem)
    
        self.assertEqual(len(pop),6)
        print(pop[0])
        

            

        



if __name__ == '__main__':
    unittest.main()