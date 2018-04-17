#/usr/bin/python
import numpy as np
from random import shuffle
import copy



def _offspring_pop(pop,popsize,genecount):
    '''
    '''
    proC,disC,proM,disM = 1,20,1,20

    lower = 0.0
    upper = 1.0

    D  = genecount
    N = popsize
    Parent = copy.deepcopy(pop)
    if popsize % 2 != 0:
        Parent = [Parent[0]]+Parent
        N +=1
    index = list(range(N))

    shuffle(index)
    index1 = index[:N//2]
    index2 = index[N//2:]
    # print(index1)
    # print(index2)
    # print(index)
    
    Parent1 = np.array([Parent[i]['genes'] for i in index1])
    Parent2 = np.array([Parent[i]['genes'] for i in index2])
    '''
    beta = zeros(N/2,D);
    mu   = rand(N/2,D);
    beta(mu<=0.5) = (2*mu(mu<=0.5)).^(1/(disC+1));
    beta(mu>0.5)  = (2-2*mu(mu>0.5)).^(-1/(disC+1));
    beta = beta.*(-1).^randi([0,1],N/2,D);
    beta(rand(N/2,D)<0.5) = 1;
    beta(repmat(rand(N/2,1)>proC,1,D)) = 1;
    OffspringDec = [(Parent1Dec+Parent2Dec)/2+beta.*(Parent1Dec-Parent2Dec)/2
                    (Parent1Dec+Parent2Dec)/2-beta.*(Parent1Dec-Parent2Dec)/2];
    '''
    shape = np.ones((N//2,D))
    beta = np.zeros((N//2,D))
    mu = np.random.rand(N//2,D)
    beta[mu<=0.5] = np.power(2*mu[mu<0.5],1.0/(disC+1))
    beta[mu>0.5]  = np.power(2-2*mu[mu>0.5],1.0/(disC+1))
    beta = beta * np.power(-1, np.random.randint(0,2,size=(N//2,D)))
    beta[np.random.rand(N//2,D) < 0.5] = 1
    beta[np.random.rand(N//2,1)*shape > proC] = 1
    offspringDec = np.row_stack(( (Parent1+Parent2)/2+beta*(Parent1-Parent2)/2,
                                        (Parent1+Parent2)/2-beta*(Parent1-Parent2)/2

    ))
    
    # @todo:
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
    return CreatePopulation(offspringDec[:popsize])








def CreatePopulation(PopDescibe):
    pop = []
    N,_ =PopDescibe.shape
    for i in range(N):
        ind = {"genes":list(PopDescibe[i,:])}
        pop.append(ind)
    return pop