
#/usr/bin/python

from abc import ABC,abstractmethod
import numpy as np




class OpBase(ABC):
    @abstractmethod
    def __call__(self,pop,popsize,genescount):
        '''
        describe:
            offspring population
        args:
            pop: parent population
            popsize: parent population size
            genescount: the number of genes
        '''
        pass




def polynomial_mutation(offspringDec,N,D,lower,upper,
    proM,disM):
    '''
    describe:
        polynodial mutation
    Args:
        offerspringDec:  np.array,offspring gennes
        N, offerspringDec size
        D: int ,number of genes
        lower: array or a float
        upper:array or a float
    return:
        offspringDec:np.array

    '''
    shape = np.ones((N,D))
    Site  =np.random.rand(N,D) < proM/D
    mu    = np.random.rand(N,D)
    MaxValue = upper * shape
    MinValue = lower * shape
    MaxMin = MaxValue - MinValue

    
    temp  = Site & (mu<=0.5)
    a1 = (offspringDec[temp] - MinValue[temp])/(MaxValue[temp] - MinValue[temp])
    q = 2*mu[temp]+(1-2*mu[temp])*np.power(1-a1,disM+1)
    q = np.power(q,1.0/(disM+1)) -1
    offspringDec[temp] = offspringDec[temp] +MaxMin[temp]*q
    
    temp = Site & (mu >0.5)
    a1 = ( MaxValue[temp]-offspringDec[temp] )/(MaxValue[temp] - MinValue[temp])
    q = 2*(1-mu[temp])+2*(mu[temp]-0.5)*np.power(1-a1,disM+1)
    q = 1 - np.power(q,1.0/(disM+1))
    offspringDec[temp] = offspringDec[temp] +MaxMin[temp]*q
    
    offspringDec[offspringDec>MaxValue] = MaxValue[offspringDec>MaxValue]
    
    offspringDec[offspringDec<MinValue] = MinValue[offspringDec<MinValue]

    return offspringDec