import numpy as np

import sys
sys.path.append('..')
from generate_reference_point import uniform_point
from util import ref_vector_T
from tmp import *
from _select import  _select
from output import output
from problem.DTZ2 import evaluate
from mtest.EAreal import _offspring_pop


def reference_vectort_adapt(V_0,FunValue):
     #### change
    Z_min=np.min(FunValue,axis=0)
    Z_max=np.max(FunValue,axis=0)
    Z=Z_max-Z_min
    V_t=V_0*Z
    ### normlize
    V_t=V_t/np.sqrt(np.sum(V_t**2,axis=1)).reshape(-1,1)
    return V_t
def evaluate_pop(pop):
    '''
    may have some error
    '''
    for ind in pop:
        evaluate(ind)
def output_wrap():
    TrueValue, _= uniform_point(1000,3)
    def wrap(FunValue):
        output(TrueValue,FunValue)
    return wrap

def test():
    '''
    '''
    from scipy.io import loadmat
    dat = loadmat('RVEA.mat')
    population = dat['A']
    g = dat['Gene']
    FunctionValue = dat['FunctionValue']
    Vt = dat['V']
    theta0 =dat['theta0']
    refV = dat['refV']
    new_pop = dat['Population']
    Selection = dat['Selection']


    Generation = 500
    alpha=2.0
    N,M =population.shape
    pop = []
    for i in range(N):
        inds ={'genes':population[i]}
        pop.append(inds)
    evaluate_pop(pop)
    FunValue = np.asarray([pop_tmp['objects'] for pop_tmp in pop],dtype=float)
    N,M=FunValue.shape
    theta0=M*np.math.pow((g/Generation),alpha)

     
    select_index=_select(FunValue,Vt,refV,theta0)

    pop=[pop[i] for i in select_index]
    Funvalue=FunValue[select_index,:]

    select_index = np.array(select_index).reshape(-1,1) +1
    T_pop =np.asarray([pop_tmp['genes'] for pop_tmp in pop],dtype=float)
    
    F_diff = np.sum(np.abs(Funvalue-FunctionValue))
    P_diff = np.sum(np.abs(T_pop-new_pop))
    S_diff = Selection-select_index

    print(F_diff)
    print("*"*50)
    print(P_diff)
    print("*"*50)
    print(S_diff)
    print("*"*50)

    


out = output_wrap()

def loop(pop,V0,Generation):
    '''
    desribe:
        @todo
    Args:
        @todo
    return:
        @todo
    '''
    alpha = 2
    fr = 0.02
    Vt = V0
    refV = ref_vector_T(Vt)
  
    for g in range(Generation):
        
        popsize=len(pop)
        genecount=len(pop[0]['genes'])
        _pop=_offspring_pop(pop,popsize,genecount)
        
        # if g%40 == 0:
        #     output(np.asarray([pop_tmp['objects'] for pop_tmp in _pop],dtype=float),
        #     np.asarray([pop_tmp['objects'] for pop_tmp in pop],dtype=float))
        pop = _pop+pop

        evaluate_pop(pop)
        FunValue = np.asarray([pop_tmp['objects'] for pop_tmp in pop],dtype=float)
        N,M=FunValue.shape
        theta0=M*np.math.pow((g/Generation),alpha)

     
        select_index=_select(FunValue,Vt,refV,theta0)
        #pop=pop[select_index,:]
        pop=[pop[i] for i in select_index]
        Funvalue=FunValue[select_index,:]
    

        if g%int(Generation*fr) == 0:
            Vt = reference_vectort_adapt(V0,FunValue)
            refV = ref_vector_T(Vt)


    return pop,Vt




def main():
    from scipy.io import savemat


    popsize=105
    t_max=500
    genecount = 7
    V_0,popsize=uniform_point(popsize,3)
    V_0=np.array(V_0)
    V_t=np.copy(V_0)
    pop=init(popsize,t_max,genecount)
    pop ,Vt= loop(pop,V_0,1000)
    TrueValue, _= uniform_point(1000,3)
    FunValue = np.asarray([pop_tmp['objects'] for pop_tmp in pop],dtype=float)
    savemat('result.mat',{"FunValue":FunValue,"V0":V_0})
    output(TrueValue,FunValue)

    




if __name__ == '__main__':
    # test() 
    main()

    




    
