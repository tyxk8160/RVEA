#/usr/bin/python

import numpy as np


from .ProblemBase import ProblemBase


class DTLZ5Problem(ProblemBase):
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
        DTLZ2

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
        g = np.sum(np.square(x[M-1:]-0.5))
        F = []
        ## theta
        x[1:] = np.pi/(4*(1+g))*(1+g*x[1:])
        
        for i in range(M):
            f = (1+g)*np.prod(np.cos(x[:M-1-i]*np.pi/2))
            if i >0:
                f = f*np.sin(x[M-i-1]*np.pi/2)
            F.append(f)

        ind['objects'] = F
        return ind









