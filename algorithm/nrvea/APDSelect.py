#/usr/bin/python
'''
APD base select
'''
import numpy as np
from util.UniformPoint import uniform_point
import copy

fp = open('result/result.txt','w')



def ReferenceVectorRegeneration(Va,FunValue):
    '''
    desibe:
        Refernce Vector Regeration
    Args:
        Va: append refernce vector
        Funvalue: population objects
    return:
        Va: new vector
    '''
    popsize,M=FunValue.shape
    N,M=V_t.shape
    Z_min = np.min(FunValue,axis=0)
    Z_max = np.max(FunValue,axis =0 )
    FunValue1 = FunValue-Z_min
    FunValueNorm=np.sqrt(np.sum(np.square(FunValue1),axis=1)).reshape(-1,1)
    # index = np.abs(FunValue)<1e-15
    # FunValue[index] = 1.0
    
    try:
        
     
        uFunValue1 = FunValue1/FunValueNorm

        
    except RuntimeWarning as e:
      
      
        print(e)

    
    
    uFunValue1=np.asmatrix(uFunValue1)
    Va=np.asmatrix(Va)
    _cosine= uFunValue1*Va.T
    _cosine= np.asanyarray(_cosine)
    
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
    index = (P_kind == None)


    # random
    Va = np.array(va)
    Va[index,:] = np.random.rand(sum(index),M)*Z_max

    return Va





def reference_vectort_adapt(V_0,FunValue):
    #### change
    Z_min=np.min(FunValue,axis=0)
    Z_max=np.max(FunValue,axis=0)
    Z=Z_max-Z_min
    V_t=V_0*Z
    ### normlize
    V_t=V_t/np.sqrt(np.sum(V_t**2,axis=1)).reshape(-1,1)
    return V_t



def ref_vector_T(V_t):
    '''
    V_t is an matrix
    '''
    tmpV_t=np.matrix(V_t)
    minVt = tmpV_t*tmpV_t.T
    minVt[minVt>=1.0] = -1.0
    minVt.sort(axis=1)
    
    refV=minVt[:,-1]
    # acos=np.frompyfunc(np.math.acos,1,1)
    ###########################################################################
    #             ufunc  
    #
    ############################################################################
    refV=np.arccos(refV)
  
    return refV.reshape(-1,1)




def _cselect(FunValue,V_t,refV,theta0,efeasible):
    '''
    describe:
        select with efeasible
    Aegs:
        FunValue: population objects maybe also include nichec and cv0 cv1
        V_t: reference vector
        refV: ???
        theta:APD params
        efeasible: flag
    return:
        select_index: next generation population
    '''
    cv1 = FunValue[:,-1] # handle constrait
    


    popsize,M=FunValue.shape
    N,M=V_t.shape
    Z_min = np.min(FunValue,axis=0)
    FunValue1 = FunValue-Z_min
    FunValueNorm=np.sqrt(np.sum(np.square(FunValue1),axis=1)).reshape(-1,1)


    
   
    try:
        
     
        uFunValue1 = FunValue1/FunValueNorm

        
    except RuntimeWarning as e:
      
      
        print(e)

    
    
    uFunValue1=np.asmatrix(uFunValue1)
    V_t=np.asmatrix(V_t)
    _cosine= uFunValue1*V_t.T
    _cosine= np.asanyarray(_cosine)
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

        # @todo
        # add constarit select
        kind_x = np.array(kind_x)
        subefeasible = efeasible[kind_x]
        _subefeasible = (subefeasible<=0)
       
        if sum(_subefeasible) == 0:
            ## select with cv1
            # add
            cv1 = efeasible
            # @end todo
            subcv1 = cv1[kind_x]
           
            id = subcv1.argmin()
           
            select_index.append(kind_x[id])
        else:

            kind_x = kind_x[_subefeasible]
            
            
            subacosine=_acosine[kind_x,j]

            subFunvalueNorm=FunValueNorm[kind_x]
            
            ###(1+D)*F'
            D=float(theta0)*subacosine/float(refV[j])
            
            APD=np.array(1+D)*subFunvalueNorm
            id=APD.argmin()
           
            select_index.append(kind_x[id])


    return select_index



class APDSelect():
    '''
    APDBase select...
    '''
    def __init__(self,popsize,M,alpha=2.0,fr = 0.1, Generations = 500):
        
        self.V0 ,self.popsize= uniform_point(popsize,M)
        self.Generartions = Generations 
        self.g = 0
        self.M = M
        self.alpha = alpha
        self.Vt = copy.deepcopy(self.V0)
        self.refV = ref_vector_T(self.Vt)
        self.fr = fr

    def __call__(self,pop):
        '''
        select populations
        '''
        efeasible = np.array([pop_tmp['efeasible'] for pop_tmp in pop])
        cv1 = np.array([pop_tmp['cv1'] for pop_tmp in pop])
        cv0 = np.array([pop_tmp['cv0'] for pop_tmp in pop])
        nichec = np.array([pop_tmp['nichec'] for pop_tmp in pop])


    


        
        # @todo add constrait
        FunValue = np.asarray([pop_tmp['objects'] for pop_tmp in pop],dtype=float)
        # FunValue = np.column_stack((FunValue,nichec,cv0,cv1))

        #@end todo
        N,M=FunValue.shape
        theta0=M*np.math.pow((self.g/self.Generartions),self.alpha)




        select_index=_cselect(FunValue,self.Vt,self.refV,theta0,cv1)
        fp.write(str(select_index))
        fp.write('\r\n')
        fp.write('='*100)
        fp.write('\r\n')
            #pop=pop[select_index,:]
        pop=[pop[i] for i in select_index]
        Funvalue = FunValue[select_index,:]




        N,M=FunValue.shape
        self.g+=1
        if self.g%int(self.Generartions*self.fr) == 0:
            self.Vt = reference_vectort_adapt(self.V0,FunValue)
            self.refV = ref_vector_T(self.Vt)

        return pop,self.Vt

        
