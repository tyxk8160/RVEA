#/usr/bin/python
import numpy as np

'''
compute niche count and efeisible
'''

from util.PopulationUtil import evaluate_pop
z = 1.0e-8
Nearzero = 1.0e-15
delta = 1e-8



def caculate_nichecount(pop,sigma):
    '''
    describe：
        caculate_nichecount.
        nc(x|U)
    Args:
        pop:populations
        sigma:float, radius
    return:
        None
    '''
    if sigma < Nearzero:
        for pop_tmp in pop:
            pop_tmp['nichec'] = 0.0

    popobj = np.array([pop_tmp['genes'] for pop_tmp in pop])
    N = len(pop)


    for i in range(N):
        # caculate distance
        # if dst >\sigma,then sh(x_1,x_2) = 0; => \frac {d(\vec x_1,\vec x_2)} {\sigma} \geq 1 =>sh<0
        # we can assume:sh(x_1,x_1) = 0 
        dst = np.sqrt(
            np.sum(
               np.square (popobj[i] - popobj),
               axis = 1
            )
        )
        # print(dst)

        sh = 1 - 1.0*dst/sigma
        sh[sh <0] = 0
        pop[i]['nichec'] = np.sum(sh)-1




def caculate_initial_max_violation(pop):
    '''
    describe:
        caculate the initial max violation
    Args:
        pop:population
    return:
        MaxG:np.array
    '''
    cv = np.array([pop_tmp['constrait'] for pop_tmp in pop])
    return np.max(cv,axis = 0)

def  caculate_violation_objective(pop,MaxG):
    '''
    descibe:
        caculate the violation_objective
    Args:
        pop:population
        MaxG:the initial max violation
    '''
    popobj = np.array([pop_tmp['constrait'] for pop_tmp in pop])
    N ,m = popobj.shape
    for i in range(N):
        cv1 = 1.0/m*np.sum(popobj[i,:]/MaxG)
        cv0 = np.max(popobj[i,:]/MaxG)
        pop[i]['cv0'] = cv0
        pop[i]['cv1'] = cv1



def mark_individual_efeasible(pop,e):
    '''
    describe:
        test is efeaible
    Args:
        pop:population
        e:np.array
    return:
        None
    '''
    for ind in pop:
        x = np.array(ind['constrait'])
        ind['efeasible'] = np.all(x<=e)



# def get_maxR(D,popsize,upper,lower):
#     '''
#     describe:
#         caculate maxR
#     '''
#     diff = np.array(upper) -np.array(lower)
#     R = 0.5*np.power(np.prod(diff)/(popsize*np.pi),1/D)
#     return R
def get_maxR(pop):
    '''
    describe:
        the fuck
    
    '''
    N = len(pop)
    popobj = np.array([pop_tmp['genes'] for pop_tmp in pop])
    
    sum = 0.0
    for i in range(N):
        # caculate distance
        # if dst >\sigma,then sh(x_1,x_2) = 0; => \frac {d(\vec x_1,\vec x_2)} {\sigma} \geq 1 =>sh<0
        # we can assume:sh(x_1,x_1) = 0 
        dst = np.sqrt(
            np.sum(
               np.square (popobj[i] - popobj),
               axis = 1
            )
        )
        subsum = np.sum(dst)
        sum+= subsum

    return sum/(N*N-N)


class DynamicBoundary(object):
    '''
    compute dynamic boundary
    '''
    def __init__(self,start,S,cp =2):
        '''
        describe:
            caculate A ,B 
        Args:
            start:np.array
        
            S = max state
        return:
            None
        '''
        self.s = 0
        self.cp = cp
        self.A = start + delta
        self.B = S/np.power(np.log(start/delta+1),1.0/cp)
       

    
    def reduce(self):
        '''
        descibe:
            update param
        '''
        A = self.A
        B = self.B
        cp = self.cp
        self.s= self.s+1
        e = A*np.exp(-np.power(self.s/B,cp)) - delta
        return e





class DynamicEevaluation(object):
    '''
    descibe:
        main interface of evelation
    '''
    def __init__(self,popsize,problem,generations):
        '''
        '''
        self.problem = problem
        self.g = 0
        self.generations = generations
        

        pass
    


    def init(self,pop):
        '''
        '''
        evaluate_pop(pop,self.problem)
        self.MaxG = caculate_initial_max_violation(pop)
        self.E = DynamicBoundary(self.MaxG,self.generations)
        self.En =self.MaxG

        MaxR = get_maxR(pop)
        self.R = DynamicBoundary(MaxR,self.generations)
        self.Rn = MaxR
    



    


    def __call__(self,pop):
        '''
        descibe:
            caculate the cv and other
        '''
        if self.g == 0:
            self.init(pop)
        
        for ind in pop:
            ind = self.problem.evaluate(ind)

        # nichc and cv0 cv1
        caculate_nichecount(pop,self.Rn)
        caculate_violation_objective(pop,self.MaxG)
        mark_individual_efeasible(pop,self.En)



        # reduce bounoundary
        x= np.array([pop_tmp['efeasible'] for pop_tmp in pop])
        if np.all(x):
            self.g+=1
            self.En = self.E.reduce()
            self.Rn = self.R.reduce()
        
        return pop







