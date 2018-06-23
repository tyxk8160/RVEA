#/usr/bin/python
import numpy as np
from generate_reference_point import uniform_point
from DCNSGA_II_DE_tools import  select_next_parent_population,fast_non_dominated_sort
import copy
from random import shuffle


def fast_select(pop,N):
    '''
    describe:
        a fast way to select the population
    Args:
        pop:list,population
        N:int, how many number you should select.must greate than zero
    return:
        subpop: subset of pop  and len(subpop) = N
    '''
    def compare(a, b):
        '''
        descibe:
            compare op
        '''
        if a["violation_objectives"][0] < b["violation_objectives"][0]:
            return -1
        elif a["violation_objectives"][0] > b["violation_objectives"][0]:
            return 1
        else:
            if a["objectives"] < b["objectives"]:
                return -1
            elif a["objectives"] > b["objectives"]:
                return 1
            else:
                return 0
        pop.sort(cmp = compare)
    return pop[:N]

        

def reference_vectort_density(FunValue,V_t):
    '''
    describe:
        compute the reference vector density
    Args:
        Funvalue:1-(l-1) layer
        Vt:
    return:
        r,np.array
    '''
    popsize,M=FunValue.shape
    N,M=V_t.shape
    Z_min = np.min(FunValue,axis=0)
    FunValue1 = FunValue-Z_min
    FunValueNorm=np.sqrt(np.sum(np.square(FunValue1),axis=1)).reshape(-1,1)
    uFunValue1 = FunValue1/FunValueNorm
    uFunValue1=np.asmatrix(uFunValue1)
    V_t=np.asmatrix(V_t)
    _cosine=uFunValue1*V_t.T
    _cosine=np.asanyarray(_cosine)

    uFunValue1=np.asmatrix(uFunValue1)
    V_t=np.asmatrix(V_t)
    _cosine=uFunValue1*V_t.T
    _cosine=np.asanyarray(_cosine)
    index=np.argmax(_cosine,axis=1)
    index=np.asarray(index).reshape(-1)

    r = np.zeros(N)
    for i in range(popsize):
        k = index[i]
        r[k] +=1
    return r











def reference_vectort_adapt(V_0,FunValue):
     
    Z_min=np.min(FunValue,axis=0)
    Z_max=np.max(FunValue,axis=0)
    Z=Z_max-Z_min
    V_t=V_0*Z
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
    refV=np.arccos(refV)
  
    return refV.reshape(-1,1)



class RVEA(object):
    def __init__(self,popsize,M,Generartion):
        '''
        desribe:
            nnn
        Args:
            popsize :int
            M : int
        '''
        self.V0 ,self.popsize= uniform_point(popsize,M)
        self.Generartion = Generartion
        self.g = 0
        self.M = M
        self.Vt = copy.deepcopy(self.V0)
        self.refV = ref_vector_T(self.Vt)



    def select(self,offspring_pop, parent_pop, parent_size):
        '''
        '''
        alpha = 2.0
        fr = 0.1
        Generation = self.Generartion
        pop = offspring_pop+parent_pop
        next_parent = []


        nondominated_rank = fast_non_dominated_sort(pop,len(pop))
        for i in xrange(len(nondominated_rank)):
            if len(next_parent)+len(nondominated_rank[i]) <= parent_size:
                next_parent.extend(nondominated_rank[i])
            else:
                break
        # compute r
        if next_parent==[]:
            r = np.zeros(self.Vt.shape[0])
        else:
            F1 = np.asarray([pop_tmp['objectives'] for pop_tmp in next_parent],dtype=float)  
            F2 = [pop_tmp['violation_objectives'][1] for pop_tmp in next_parent] # nichecount
            F3 = [pop_tmp['violation_objectives'][0] for pop_tmp in next_parent] # cv
            # FunValue[:,:-2] = F1
            FunValue = np.zeros((len(next_parent),self.M))
            FunValue[:,:-2] = F1
            FunValue[:,-2] = F2
            FunValue[:,-1] = F3
            r = reference_vectort_density(FunValue, self.Vt)



      
        
        if len(next_parent) < parent_size:
            num = parent_size - len(next_parent)
            SubPop1 = nondominated_rank[i] # the last layer
            F1 = np.asarray([pop_tmp['objectives'] for pop_tmp in SubPop1],dtype=float)
            
            F2 = [pop_tmp['violation_objectives'][1] for pop_tmp in SubPop1] # nichecount
            F3 = [pop_tmp['violation_objectives'][0] for pop_tmp in SubPop1] # cv
            # FunValue[:,:-2] = F1
            FunValue = np.zeros((len(SubPop1),self.M))
            FunValue[:,:-2] = F1
            FunValue[:,-2] = F2
            FunValue[:,-1] = F3
            N,M=FunValue.shape
            theta0=M*np.math.pow((self.g/Generation),alpha)

            select_index=_select(FunValue,self.Vt,self.refV,theta0,r)
            #
            if len(select_index) > num:
                #delete some pop
                select_index.sort(key=lambda x:x[0])
                index = select_index[:num]
                next_pop1 = [SubPop1[v] for k,v in index ] 
                next_parent += next_pop1
                
            else:
                # maybe select some from other
                select_index=[v for k,v in select_index]
                temp_parent = [SubPop1[i] for i in select_index]
                
                restPop = [SubPop1[i] for i in range(len(SubPop1)) if i not in select_index]
                next_pop1 = fast_select(restPop,  num - len(temp_parent))

                next_parent += temp_parent
                next_parent += next_pop1





        FunValue = np.zeros((len(next_parent),self.M))
        F1 = np.asarray([pop_tmp['objectives'] for pop_tmp in next_parent],dtype=float)
        
        F2 = [pop_tmp['violation_objectives'][1] for pop_tmp in next_parent] # nichecount
        F3 = [pop_tmp['violation_objectives'][0] for pop_tmp in next_parent] # cv
        # FunValue[:,:-2] = F1
        FunValue[:,:-2] = F1
        FunValue[:,-2] = F2
        FunValue[:,-1] = F3
        N,M=FunValue.shape
        self.g+=1
        if self.g%int(Generation*fr) == 0:
            self.Vt = reference_vectort_adapt(self.V0,FunValue)
            self.refV = ref_vector_T(self.Vt)
        return next_parent,len(next_parent)


def _select(FunValue,V_t,refV,theta0,r):
    '''
    describe:
        add r
    '''
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
        select_index.append((r[j],kind_x[id]))

    return select_index

        








    


    