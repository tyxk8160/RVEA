#/usr/bin/python
import numpy as np 
from util.output import output

from problem.DTLZ5 import DTLZ5Problem
from problem.DTLZ4 import DTLZ4Problem
from problem.DTLZ2 import DTLZ2Problem
from problem.DTLZ3 import DTLZ3Problem
from problem.DTLZ1 import DTLZ1Problem
from problem.C1DTLZ1 import C1DTLZ1Problem
from problem.C2DTLZ2 import C2DTLZ2Problem

from util.UniformPoint import uniform_point,generate_point

from op.EAreal import EAreal
from output.mlog import Foo
from algorithm.nrvea.RVEA import nRVEA
from output.FigureOut import FigureOut
from output.FileOut import FileOut
from metrics.hyperholume import HyperVolume




problem = C2DTLZ2Problem(7) # var count is 12

op = EAreal() # EAreal operator
TrueValue, _= uniform_point(1000,3)
# TrueValue,_ = generate_point(1000,3)
# TrueValue =0.5*TrueValue

# fig = FigureOut(TrueValue)
fo = FileOut('result/log.txt')

alg = nRVEA(problem,op,400,generations = 500)
# alg.subscribe(fig)
alg.subscribe(fo)
pop,Vt = alg()
pop = [pop_tmp for pop_tmp in pop if pop_tmp['cv0']<1e-15]




front = [pop_tmp['objects'] for pop_tmp in pop]
# print([pop_tmp['cv0'] for pop_tmp in pop])
# print(pop)

FunValue = np.asarray(front,dtype=float)
hv  =HyperVolume([2.0,2.0,2.0])
# # print(front)
# # print(type(front[0]))

print('HV=',hv.compute(front)/(2.0**3))


output(TrueValue,FunValue)
