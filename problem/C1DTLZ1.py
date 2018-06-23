#/usr/bin/python

import numpy as np



from .ProblemBase import ProblemBase


class C1DTLZ1Problem(ProblemBase):
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
    @property
    def R(self):
        '''
        refpoint
        '''
        return [1.5]*self.M
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
        g = 100*(D-M+1+np.sum(
        np.square((x[M-1:]-0.5))-np.cos(20*np.pi*(x[M-1:]-0.5)))
        )
        # print(g)
 
        F = [] # objects
        for i in range(M):
            # temp = x[:M-i-1]
            # print(temp)
            f = 0.5*np.prod(x[:M-i-1])*(1+g)
            if i >0:
                f = f*(1-x[M-i-1])
                # print(M-i,'=',x[M-i-1])
            F.append(f)
        ind['objects'] = F
        C = []
        c = 0.6*F[-1]+ np.sum(F[:-1]) -1
        if c< 0:
            c = 0.0
        C.append(c)
        ind['constrait'] = C
        return ind









