#/usr/bin/python
import numpy as np 
from util.output import output

from problem.DTLZ2 import DTLZ2Problem

from util.UniformPoint import uniform_point

from op.EAreal import EAreal
from output.mlog import Foo
from algorithm.rvea.RVEA import RVEA
from output.FigureOut import FigureOut




problem = DTLZ2Problem(12) # var count is 12

op = EAreal() # EAreal operator
TrueValue, _= uniform_point(1000,3)
fig = FigureOut(TrueValue)

alg = RVEA(problem,op,105,generations = 500)
alg.subscribe(fig)
pop,Vt = alg()



fig.display(pop)


FunValue = np.asarray([pop_tmp['objects'] for pop_tmp in pop],dtype=float)
print(len(pop))


output(TrueValue,FunValue)
