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



def HV1(op):
    objs = [(275,10),(156,8),(132,6),(105,3)]
    
    problem1 = [(5,DTLZ1Problem),(10,DTLZ2Problem),(10,DTLZ3Problem),(10,DTLZ4Problem)]
  
    # without constarit
    fp = open('result/hv.txt','a+')




    for K,Problem in problem1:
        fp.write('-'*80+'\r\n')
        for popsize,M in objs:
            problem = Problem(M+K-1,M = M)
            alg = RVEA(problem,op,popsize = popsize ,generations =500)
            pop,Vt = alg()
            front = [pop_tmp['objects'] for pop_tmp in pop]
            hv = HV(front,problem.R)
            print(hv)
            fp.write(Problem.__name__+'\t'+'%d\t%f\r\n' %(M,hv))
            

    fp.close()

def HV2(op):
    problem2 =[(5,C1DTLZ1Problem),(10,C2DTLZ2Problem)]
    fp = open('result/chv.txt','w+')
    objs = [(275,10),(156,8),(132,6),(105,3)]
   
    for K,Problem in problem2:
        fp.write('-'*80+'\r\n')
        for popsize,M in objs:
            problem = Problem(M+K-1,M = M)
            alg = nRVEA(problem,op,popsize = popsize,generations =1000)
            pop,Vt = alg()
            pop = [pop_tmp for pop_tmp in pop if pop_tmp['cv1']<1e-15]
            front = [pop_tmp['objects'] for pop_tmp in pop]
            hv = HV(front,problem.R)
            print(hv)
            fp.write(Problem.__name__+'\t'+'%d\t%f\r\n' %(M,hv))
            


def main():
    op = EAreal()
    HV1(op)
    # HV2(op)

if __name__ == '__main__':
    main()