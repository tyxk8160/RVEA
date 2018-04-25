#/usr/bin/python

import numpy as np



from .ProblemBase import ProblemBase


class DTLZ7Problem(ProblemBase):
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
        
        g = 1.0+9.0/(D-M+1)*np.sum(x[M-1:])
        h = M - np.sum( x[:M-1]/(1+g)*(1+np.sin(3*np.pi*x[:M-1]))
            
        )


        F = []
        for i in range(M):
            f = x[i]
            if i == M-1:
                f = (1+g)*h
            F.append(f)

        ind['objects'] = F
        return ind









