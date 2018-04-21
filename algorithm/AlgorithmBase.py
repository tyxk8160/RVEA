# /usr/bin/python
from abc import ABC,abstractmethod,abstractproperty

class AlgorithmBase(ABC):
    Observers = []
    def __init__(self,problem,op,
        popsize,generations):
        '''
        describe:
            all algorithm should know the problem and operator

        '''
        self.problem = problem
        self.op = op
        self.popsize = popsize
        self.generations = generations
       


    @abstractmethod
    def __call__(self):
        '''
        the main function
        '''

    def subscribe(self,O):
        '''
        describe:
            Observer pattern
        '''
        self.Observers.append(O)
    
    def notify(self,*arg,**kargs):
        '''

        '''
    
        for Observer in self.Observers:
           
            Observer.display(*arg,**kargs)
      



    def close(self,*arg ,**kargs):
        '''
        describe:
            special message
        '''
        for Observer in self.Observers:
            Observer.close()