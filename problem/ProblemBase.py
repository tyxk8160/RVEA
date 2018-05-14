#/usr/bin/python
from abc import ABC,abstractmethod,abstractproperty
import numpy as np




class ProblemBase(ABC):
    D = 12
    M = 3

    @abstractmethod
    def evaluate(self,ind):
        '''
        describe:
            all probelm must implement this method
        Args:
            ind, dict
        return:
            r,dict
        '''
        print('this function is need！')
        pass
    # @abstractproperty
    # def constraints_num(self):
    #     '''
    #     describe:
    #         this property is needed
    #     '''
    #     pass
    # @abstractproperty
    # def objects_num(self):
    #     '''
    #     desribe:
    #         need
    #     '''
    #     pass
    # @abstractproperty
    # def D(self):
    #     '''
    #     descibe:
    #         genes number
        
     # '''
    

    @property
    def lower(self):
        '''
        describe:
            lower
            default 0.0
        Args:
            None
        return:
            lower: a list
        '''
     
        return np.array([0.0]*self.D)

        
    @property
    def upper(self):
        '''
        describe:
            upper 
        Args:
            None
        return:
            upper: a list
        '''
        return np.array([1.0]*self.D)



    
    