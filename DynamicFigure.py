#/usr/bin/python
import numpy as np 

from problem.DTLZ2 import DTLZ2Problem

from util.UniformPoint import uniform_point,generate_point

from op.EAreal import EAreal


from output.DynamicOut import DynamicOut,DynamicHV

from algorithm.nrvea.RVEA import nRVEA
from algorithm.rvea.RVEA import RVEA

from metrics.hyperholume import HyperVolume




# problem = C2DTLZ2Problem(7) # var count is 12
problem = DTLZ2Problem(12)

op = EAreal() # EAreal operator
TrueValue, _= uniform_point(1000,3)

sb = DynamicOut(PF = TrueValue)
sdhv =DynamicHV([2.0,2.0,2.0])
alg = RVEA(problem,op,105,generations = 1000)
# alg.subscribe(sb)
alg.subscribe(sdhv)
pop,Vt = alg()




front = [pop_tmp['objects'] for pop_tmp in pop]

# FunValue = np.asarray(front,dtype=float)

# output(TrueValue,FunValue)
