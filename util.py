import numpy as np

from scipy.io import loadmat




def _get_pop(gens,objects,popsize):
    pop=[{'id':i,'gens':gens[i],'objectives':objects[i]} for i in range(popsize)]
    return pop

def get_funvalue(pop):
    '''
    

    '''
    FunValue = np.asarray([pop_tmp['objectives'] for pop_tmp in pop],dtype=float)
    #Translation
    #Z_min = np.min(FunValue,axis=0)
    
    #N,M=FunValue.shape
    #theta0=M*np.math.pow((t/tmax),alpha);
    
    return FunValue
   
def ref_vector_T(V_t):
    '''
    V_t is an matrix
    '''
    tmpV_t=np.matrix(V_t)
    minVt = tmpV_t*tmpV_t.T
    minVt.sort(axis=1)
    refV=minVt[:,-2]
    acos=np.frompyfunc(np.math.acos,1,1)
    ###########################################################################
    #             ufunc  
    #
    ############################################################################
    refV=acos(refV)
    return refV.reshape(-1,1)