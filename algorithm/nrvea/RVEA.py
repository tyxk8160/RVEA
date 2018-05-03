#/usr/bin/python
import numpy as np

from ..AlgorithmBase import AlgorithmBase
from util.PopulationUtil import initpopulation,evaluate_pop
from .dynamic import DynamicEevaluation
# from util.uniform_point import uniform_point


from util.UniformPoint import uniform_point
from .APDSelect import APDSelect



class nRVEA(AlgorithmBase):
    def __init__(self,problem,op,popsize,generations,
        alpha =2.0 ,fr = 0.1):
        self.alpha = alpha
        self.fr = fr
        self.ev = DynamicEevaluation(popsize,problem,generations)
        super(nRVEA,self).__init__(problem,op,popsize,generations)
    
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

            # pop = evaluate_pop(pop, self.problem)
            pop = self.ev(pop)
           
           
            pop ,Vt = select(pop)
            self.notify(pop)
        


            

        return pop,Vt





        
        



