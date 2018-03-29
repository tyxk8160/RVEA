#/usr/bin/env python
import numpy as np
from scipy.io import loadmat, savemat
import random
import copy
import math
from collections import defaultdict
from matplotlib import pyplot as plt


from  _select import _select
from  util import _get_pop, ref_vector_T
from  ref_vector_adapter import ref_vector_adapter
from tmp import *

from generate_reference_point import test









def _loopone(alpha,pop,V_0,V_t,t,tmax=100):
#     fr=0.1
#    # tmax=300
    # T_min=5
    popsize=len(pop)
    genecount=len(pop[0]['genes'])
    _pop=offspring_pop(pop,popsize,genecount)
    pop = _pop+pop

    FunValue = np.asarray([pop_tmp['objectives'] for pop_tmp in pop],dtype=float)
    N,M=FunValue.shape
    theta0=M*np.math.pow((t/tmax),alpha)
    refV=ref_vector_T(V_t)
    select_index=_select(FunValue,V_t,refV,theta0)
    #pop=pop[select_index,:]
    pop=[pop[i] for i in select_index]
    Funvalue=FunValue[select_index,:]
    Vt_1=ref_vector_adapter(V_0,V_t,FunValue,t)

    print pop,Vt_1



     


   









        


if __name__ == '__main__':
    popsize=13
    t_max=2000
    genecount=7
    V_0=test(3,3,1)
    V_0=np.array(V_0)
    V_t=np.copy(V_0)
    pop=init(popsize,t_max,genecount)
    for t in range(t_max):
        pop,V_t=_loopone(0.1,pop,V_0,V_t,t,t_max)
        # print(t)
        # print(np.sum((V_0-V_t)**2,axis=1))
        

    FunValue = np.asarray([pop_tmp['objectives'] for pop_tmp in pop],dtype=float)
    savemat('result.mat',{"FunValue":FunValue})

    #_pop=offspring_pop(pop,popsize,genecount)
    #print(_pop)
   # inds_obj=objectives_value_translation(_pop)
   # main()
