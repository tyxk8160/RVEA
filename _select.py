import numpy as np


def log(fun):
    def wrap(FunValue,V_t,refV,theta0):
        ret = fun(FunValue,V_t,refV,theta0)
        # print(" "*20+"refV:",refV.shape[0])
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

        








    


    

if __name__ == '__main__':
    from scipy.io import loadmat
    dat=loadmat('data.mat')
    
    theta0=dat['theta0']
    refV=dat['refV']
    objects=dat['FunctionValue']
    V=dat['V']
    select_t=dat['Selection']
    select_t = select_t-1
    select_t= select_t.reshape(1,-1)
   

    select=np.array(_select(objects,V,refV,theta0)).reshape(1,-1)

    
    print(select-select_t)


    


