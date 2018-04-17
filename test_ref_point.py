#/usr/bin/env python
import numpy as np
from scipy.io import loadmat, savemat
import random
import copy
import math
from collections import defaultdict
from output import output


from mtest.EAreal import _offspring_pop
from mtest.rvea import evaluate_pop



# 加入约束优化
import nichec
import Constraint_Violation


from  _select import _select
from  util import _get_pop, ref_vector_T
from  ref_vector_adapter import ref_vector_adapter
from tmp import *

from generate_reference_point import test,uniform_point




def _loopone(alpha,pop,V_0,V_t,t,tmax=50):
#     fr=0.1
#    # tmax=300
    # T_min=5
    popsize=len(pop)
    genecount=len(pop[0]['genes'])
    _pop=_offspring_pop(pop,popsize,genecount)
    evaluate_pop(_pop)
    pop = _pop+pop

   
       
    FunValue = np.asarray([pop_tmp['objects'] for pop_tmp in pop],dtype=float)
    # no change if  constraint is None
    '''
    maybe need change the FunValue
    if constrait is not None,we should change it
    cv = [[pop_tmp['violation_objects'],pop_tmp['nichec']] 
        for pop_tmp in pop]
    Funvalue = np.collumn_stack((Funvalue,np.array(cv)))
    '''

    N,M=FunValue.shape
    theta0=M*np.math.pow((t/tmax),alpha)
    refV=ref_vector_T(V_t)
    select_index=_select(FunValue,V_t,refV,theta0)
    #pop=pop[select_index,:]
    pop=[pop[i] for i in select_index]
    Funvalue=FunValue[select_index,:]
    Vt_1=ref_vector_adapter(V_0,V_t,FunValue,t)

    return pop,Vt_1



     


   



        


if __name__ == '__main__':
    popsize=105
    t_max=1000
    genecount= 12
    V_0,popsize=uniform_point(popsize,3)
    V_0=np.array(V_0)
    V_t=np.copy(V_0)
    pop=init(popsize,t_max,genecount)
    for t in range(t_max):
        pop,V_t=_loopone(2.0,pop,V_0,V_t,t,t_max)
        print(t)
        # print(np.sum((V_0-V_t)**2,axis=1))
        
    TrueValue, _= uniform_point(1000,3)
    FunValue = np.asarray([pop_tmp['objects'] for pop_tmp in pop],dtype=float)
    output(TrueValue,FunValue)

    savemat('result.mat',{"FunValue":FunValue,"V0":V_0})
