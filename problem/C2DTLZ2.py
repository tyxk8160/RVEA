#  min(
#      min(
#          (PopObj-1).^2+repmat(sum(PopObj.^2,2),1,M)-PopObj.^2-r^2,
#               [],
#                                   2),
        #  sum((PopObj-1/sqrt(M)).^2,2)-r^2)

# 

#/usr/bin/python

import numpy as np



from .ProblemBase import ProblemBase


class C2DTLZ2Problem(ProblemBase):
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
        return [2.0]*self.M
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
        if M == 3:
            r = 0.4
        else:
            r = 0.5
        x=np.array(ind['genes']) 
        D = x.size
        g = np.sum(np.square(x[M-1:]-0.5))
        F = []
        for i in range(M):
            f = (1+g)*np.prod(np.cos(x[:M-1-i]*np.pi/2))
            if i >0:
                f = f*np.sin(x[M-i-1]*np.pi/2)
            F.append(f)

        ind['objects'] = F
        popobj = np.array(F)
        c1 = np.square(popobj-1) + np.sum(np.square(popobj)) -np.square(popobj)- np.square(r)
        c2 = np.sum(np.square(popobj -1.0/np.sqrt(M))) - np.square(r)
        # print(c1)
        # print(c2)
        c = min(np.min(c1),c2)
        if c<0:
            c =0.0
        C = [c]
        ind['constrait'] = C

        return ind









