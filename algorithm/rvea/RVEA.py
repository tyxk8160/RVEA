#/usr/bin/python
import numpy as np

from ..AlgorithmBase import AlgorithmBase
from util.PopulationUtil import initpopulation,evaluate_pop
# from util.uniform_point import uniform_point


from util.UniformPoint import uniform_point
from .APDSelect import APDSelect

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

def reference_vectort_adapt(V_0,FunValue):
    #### change
    Z_min=np.min(FunValue,axis=0)
    Z_max=np.max(FunValue,axis=0)
    Z=Z_max-Z_min
    V_t=V_0*Z
    ### normlize
    V_t=V_t/np.sqrt(np.sum(V_t**2,axis=1)).reshape(-1,1)
    return V_t


#   popsize=105
#   t_max=500
#   genecount = 7
#   V_0,popsize=uniform_point(popsize,3)
#   V_0=np.array(V_0)
#   V_t=np.copy(V_0)
#   pop=init(popsize,t_max,genecount)
#   pop ,Vt= loop(pop,V_0,1000)
#   TrueValue, _= uniform_point(1000,3)
#   FunValue = np.asarray([pop_tmp['objects'] for pop_tmp in pop],dtype=float)
#   savemat('result.mat',{"FunValue":FunValue,"V0":V_0})
#   output(TrueValue,FunValue)


class RVEA(AlgorithmBase):
    def __init__(self,problem,op,popsize,generations,
        alpha =2.0 ,fr = 0.1):
        self.alpha = alpha
        self.fr = fr
        super(RVEA,self).__init__(problem,op,popsize,generations)
    
    def __call__(self):
        M = self.problem.M 
        D = self.problem.D
        print(self.generations)
        lower = self.problem.lower
        upper = self.problem.upper
        self.V_0,self.popsize = uniform_point(self.popsize,M)
        self.V_0 = np.array(self.V_0)
        self.V_t = np.copy(self.V_0)
        Pop = initpopulation(self.popsize,D,lower,upper)
        pop ,Vt = self.loop(Pop,self.V_0,self.generations)
        return pop,Vt
    



    


    def loop(self,pop,V0,Generation):
        '''
        desribe:
            @todo
        Args:
            @todo
        return:
            @todo
        '''
      
        # alpha = self.alpha
        # fr = self.fr

        #popsize,M,alpha=2.0,fr = 0.1, Generations = 500)
        select = APDSelect(self.popsize,
                self.problem.M,
                self.alpha,self.fr,self.generations)
        self.popsize = select.popsize
    
        for g in range(Generation):
           
            popsize=len(pop)
            genecount=len(pop[0]['genes'])
            # _pop=_offspring_pop(pop,popsize,genecount)
            _pop = self.op(pop,popsize,genecount)
            
            # if g%40 == 0:
            #     output(np.asarray([pop_tmp['objects'] for pop_tmp in _pop],dtype=float),
            #     np.asarray([pop_tmp['objects'] for pop_tmp in pop],dtype=float))
            pop = _pop+pop

            pop = evaluate_pop(pop, self.problem)
            self.notify(pop)


            pop ,Vt = select(pop)
        


            

        return pop,Vt





        
        



