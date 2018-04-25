#/usr/bin/python

import numpy as np



from .ProblemBase import ProblemBase


class DTLZ9Problem(ProblemBase):
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
        DTLZ8

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
        F = []
        x =np.power(x,0.1)
        for i in range(M):
            f = (D//M)*np.sum(x[(i-1)*D//M:x[i*D//M]])
            F.append(f)
        C = []
        for i in range(M-1):
            c = F[-1]**2+F[i]- 1
            c =0-c
            C.append(c)
        ind['objects'] = F
        ind['constaits'] = C
        


       
        return ind









