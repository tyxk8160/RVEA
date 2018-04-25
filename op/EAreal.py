from .OpBase import OpBase,polynomial_mutation
from util.PopulationUtil import CreatePopulation
import copy
from random import shuffle
import numpy as np





class EAreal(OpBase):
    '''
    GA real coding
    '''
    def __init__(self, lower =0.0,
                    upper = 1.0 ,
                    proC = 1,
                    disC = 20,
                    proM = 1,
                    disM = 20):
        '''
        '''
        self.lower = lower
        self.upper = upper
        self.proC = proC
        self.disC = disC
        self.disM = disM
    def __call__(self,pop,popsize,genescount):
        '''
    
        '''

        proC,disC,proM,disM = self.proC,self.disC,self.proC,self.disM
        lower = self.lower
        upper = self.upper

       

        D  = genescount
        N = popsize
        Parent = copy.deepcopy(pop)
        if popsize % 2 != 0:
            Parent = [Parent[0]]+Parent
            N +=1
        index = list(range(N))

        shuffle(index)
        index1 = index[:N//2]
        index2 = index[N//2:]


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




        offspringDec = polynomial_mutation(offspringDec, N, 
                    D, lower, upper, proM, disM)

        return CreatePopulation(offspringDec[:popsize])

        
