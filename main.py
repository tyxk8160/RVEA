#/usr/bin/python
import numpy as np 
from util.output import output

from problem.DTLZ5 import DTLZ5Problem
from problem.DTLZ4 import DTLZ4Problem
from problem.DTLZ2 import DTLZ2Problem
from problem.DTLZ3 import DTLZ3Problem
from problem.DTLZ1 import DTLZ1Problem

from util.UniformPoint import uniform_point,generate_point

from op.EAreal import EAreal
from output.mlog import Foo
from algorithm.rvea.RVEA import RVEA
from output.FigureOut import FigureOut
from metrics.hyperholume import HyperVolume




problem = DTLZ1Problem(7) # var count is 12

op = EAreal() # EAreal operator
# TrueValue, _= uniform_point(1000,3)
TrueValue,_ = generate_point(1000,3)
TrueValue =0.5*TrueValue

# fig = FigureOut(TrueValue)

alg = RVEA(problem,op,105,generations = 500)
# alg.subscribe(fig)
pop,Vt = alg()




front = [pop_tmp['objects'] for pop_tmp in pop]
print(pop)

FunValue = np.asarray(front,dtype=float)
hv  =HyperVolume([1.5,1.5,1.5])
# # print(front)
# # print(type(front[0]))

print('HV=',hv.compute(front)/(1.5**3))


output(TrueValue,FunValue)
