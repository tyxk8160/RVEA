#/usr/bin/python
'''
Get Result of HV
'''
#/usr/bin/python
import numpy as np 
from util.output import output
from util.UniformPoint import uniform_point,generate_point

# from algorithm.nrvea.RVEA import nRVEA
# from algorithm.rvea.RVEA import RVEA
# from metrics.hyperholume import HyperVolume,hv_compute
from op.EAreal import EAreal



from problem import *
from algorithm import *
from metrics import HV




objs = [10,8,6,3]
problem1 = [(5,DTLZ1Problem),(10,DTLZ2Problem),(10,DTLZ3Problem),(10,DTLZ4Problem)]
# without constarit
fp = open('result/hv.txt','a+')

op = EAreal()


for K,Problem in problem1:
    fp.write('-'*80+'\r\n')
    for M in objs:
        problem = Problem(M+K-1,M = M)
        alg = RVEA(problem,op,popsize = 105,generations =500)
        pop,Vt = alg()
        front = [pop_tmp['objects'] for pop_tmp in pop]
        hv = HV(front,problem.R)
        print(hv)
        fp.write(Problem.__name__+'\t'+'%d\t%f\r\n' %(M,hv))
        


