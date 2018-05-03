#/usr/bin/python

import unittest
from unittest import   TestCase
import numpy as np
import pylab as plt


import sys
sys.path.append('..')
from algorithm.rvea.dynamic import *
from problem.C1DTLZ1 import C1DTLZ1Problem
from util.PopulationUtil import CreatePopulation

class DynamicTest(TestCase):
    def setUp(self):
        print('Dynamic Test')
    def tearDown(self):
        print('down')
    def test_ev(self):
        popsize = 10
        problem = C1DTLZ1Problem(7)
        generation = 10
        ev = DynamicEevaluation(popsize,problem,generation)
        for i in range(10):
            popvalue = np.random.rand(popsize,7)
            pop = CreatePopulation(popvalue)
            ev(pop)
            # print(popvalue)
            # print('R = ',ev.Rn)
            # # # print('E =',ev.En)

            # print([pop_tmp['nichec'] for pop_tmp in pop])
    def test_maxR(self):
        # R = get_maxR(3,15,[1.0,1.0,1.0,1.0,1.0],[0,0,0,0,0])
        # print('R =',R)
        pass
    def test_reduceR(self):
        '''
        '''
        # R = get_maxR(3,15,[1.0,1.0,1.0,1.0,1.0],[0,0,0,0,0])
        # x = DynamicBoundary(R,100)
        # y = []
        # for i in range(99):
        #     y.append(x.reduce())
        pass
        
    def test_nichec(self):
        # pass
        problem = C1DTLZ1Problem(5)
        
        
        popsize=10
     
        popvalue = np.random.rand(popsize,5)
        pop = CreatePopulation(popvalue)
        R = get_maxR(pop)
        print('R=',R)
        x = DynamicBoundary(R,100)
        caculate_nichecount(pop,R)
        # print([pop_tmp['nichec'] for pop_tmp in pop])

        for i in range(99):
            R = x.reduce()
            caculate_nichecount(pop,R)
            print([pop_tmp['nichec'] for pop_tmp in pop])




        # plt.plot(y)
        # plt.show()
            # print('A=',x.A)
            # print('B=',x.B)
        


def main():
    unittest.main()

if __name__ == '__main__':
    main()
