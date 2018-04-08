import numpy as np


def log(fun):
    def wrap(FunValue,V_t,refV,theta0):
        ret = fun(FunValue,V_t,refV,theta0)
        print(ret)
        return ret
    return wrap


@log
def _select(FunValue,V_t,refV,theta0):
    popsize,M=FunValue.shape
    N,M=V_t.shape
    Z_min = np.min(FunValue,axis=0)
    FunValue1 = FunValue-Z_min
    FunValueNorm=np.sqrt(np.sum(np.square(FunValue1),axis=1)).reshape(-1,1)
    uFunValue1 = FunValue1/FunValueNorm
    ###  _cosvalue
    #
    #
    uFunValue1=np.asmatrix(uFunValue1)
    V_t=np.asmatrix(V_t)
    _cosine=uFunValue1*V_t.T
    _cosine=np.asanyarray(_cosine)
    # tmp_x=_cosine[_cosine>1.0]
    # tmp_y=_cosine[_cosine<-1.0]
    # if tmp_x.any():
    #     print(tmp_x)
    # if tmp_y.any():
    #     print(tmp_y)
    

    _acosine=np.arccos(_cosine)
   
  
    index=np.argmax(_cosine,axis=1)
    index=np.asarray(index).reshape(-1)
    P_kind=[None]*N
    for i in range(popsize):
        k=index[i]
        k=int(k)
        if P_kind[k] is None:
            P_kind[k]=[]
        P_kind[k].append(i)
    ### todo:
    #
    select_index=[]
    for j in range(N):
        kind_x=P_kind[j]
        if kind_x is None:
            continue
        subacosine=_acosine[kind_x,j]

        subFunvalueNorm=FunValueNorm[kind_x]
        ###(1+D)*F'
        D=float(theta0)*subacosine/float(refV[j])
        
        APD=np.array(1+D)*subFunvalueNorm
        id=APD.argmin()
        select_index.append(kind_x[id])

    return select_index

        



# def reference_vector_guided_selection(pop,t,V_t,tmax):
#     '''
#         pop --->population
#         t   --->generatio
#         V_t --->unit refernce vector set
#     '''
#     FunValue = np.asarray([pop_tmp['objectives'] for pop_tmp in pop],dtype=float)
#     N,M=FunValue.shape

    
#     Z_min = np.min(FunValue,axis=0)
#     #Translation
#     FunValue1 = FunValue-Z_min
#     # shape error,fuck numpy
#     #WTF shape=(M,)
#     uFunValue1 = FunValue/np.sqrt(np.sum(np.square(FunValue1),axis=1)).reshape(N,1)
#     _cosine = np.sum (np.multiply(uFunValue1,V_t),axis=1).reshape(N,1)
#     _acosine = np.arccos(_cosine)
#     tmpV_t=np.matrix(V_t)
#     minVt = tmpV_t*tmpV_t.T
#     INF=1<<27
#     for i in range(N):
#         minVt[i,i]=INF
    
#     minVt=np.min(np.array(minVt),axis=1)
#     # WTF bad for loop
#     index=np.argmax(_cosine,axis=1)
#     for i in range(N):
#         k=index[i]
#         PP[k].append(pop[i])

#     # genes
#     new_pop=[]
#     for i in range(M):
#         uVti=minVt[i]
#         individual_index = PP[i]
#         subuFunvalue = uFunValue[individual_index,:] # OK or not
#         subacos = _acosine[individual_index]
#         # APD
#         PD1 = 1+ M*np.math.pow((t/tmax),alpha)*subacos/uVti
#         APD = np.multiply(PD1,subuFunvalue)
#         select_index=np.amin(APD)
#         new_pop.append(copy.deepcopy(pop[individual_index[select_index]]))
#     return new_pop
    
   



        
# def main():
#     dat=loadmat('select_test2.mat')
    
#     theta0=dat['theta0']
#     refV=dat['refV']
#     objects=dat['FunctionValue']
#     V=dat['V']
#     select_t=dat['Selection']
   

#     select=_select(objects,V,refV,theta0)
#     print(select)




    
#     pass

    

if __name__ == '__main__':
    from scipy.io import loadmat
    dat=loadmat('data.mat')
    
    theta0=dat['theta0']
    refV=dat['refV']
    objects=dat['FunctionValue']
    V=dat['V']
    select_t=dat['Selection']
   

    select=_select(objects,V,refV,theta0)
    print(select)


    


