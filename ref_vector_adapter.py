import numpy as np





def ref_vector_adapter(V_0,V_t,FunValue,t,T_min=100):
    if(t%T_min!=0):
        return V_t
    #### change
    Z_min=np.min(FunValue,axis=0)
    Z_max=np.max(FunValue,axis=0)
    Z=Z_max-Z_min
    V_t=V_0*Z
    ### normlize
    V_t=V_t/np.sqrt(np.sum(V_t**2,axis=1)).reshape(-1,1)
    return V_t




if __name__ == '__main__':
    from scipy.io import loadmat
    dat = loadmat('ref_adp_result.mat')
    V_0 = dat['Vs']
    V_t  = np.copy(V_0)
    FunValue= dat['FunctionValue']
    V = dat['V']
    t = 10
    T_min = 1
   
    V_t=ref_vector_adapter(V_0,V_t,FunValue,t,T_min)
    # print(V_t-V)
    print(np.sum(V_t-V,axis=1))


