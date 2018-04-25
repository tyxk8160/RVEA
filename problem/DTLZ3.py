#/usr/bin/python

import numpy as np

from .ProblemBase import ProblemBase

class DTLZ3Problem(ProblemBase):
    def __init__(self,D ,M = 3):
        '''
        describe:
            set param
        Args:
            D,the number of genes
            M,the number of objects
        '''
        self.D = D
        self.M = M
    def evaluate(self,ind):
        '''
        describe:
        DTLZ3

        Args:
            ind:dict
                ind['gens'],list,solution space
                ind['objects'],list,obejcts
                ind['constrait'],list,[],the problem has no constrait
        return:
            ind: add objects and constraits
        '''
        M = self.M
        x=np.array(ind['genes']) 
        D = x.size
        # print('DTLZ3')
        if D != self.D:
            raise ValueError('Genes count must equal D')
        g =D - M +1 +np.sum(np.square(x[M-1:]-0.5)) - np.sum(np.cos(x[M-1:] - 0.5))
        F = []
        for i in range(M):
            f = (1+g)*np.prod(np.cos(x[:M-1-i]*np.pi/2))
            if i >0:
                f = f*np.sin(x[M-i-1]*np.pi/2)
            F.append(f)

        ind['objects'] = F
        return ind




