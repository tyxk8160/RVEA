#/usr/bin/python
import numpy as np
from util.output import output
from metrics.hyperholume import HyperVolume
import pylab as plt


class DynamicOut(object):
    '''
    output for each generation
    '''
    def __init__(self, PF=None,frame = None):
        '''
        '''
        self.frame = frame
        self.PF = PF
        if self.frame is None:
            self.frame = [0,10,20,60,100,150,200,300,499]
        self.g = 0

    def display(self,pop,*arg,**karg):
        '''
        '''
        if self.g in self.frame:
            front = [pop_tmp['objects'] for pop_tmp in pop]
            FunValue = np.asarray(front,dtype=float)
            output(self.PF, FunValue,isShow=False,index = self.g )
        self.g+=1
    def close(self):
        pass

class DynamicHV(object):
    '''
    '''
    def __init__(self,R):
        self.R = R
        self.K =np.prod(R)
        self.g = 0
        self.HVs=[]
    def display(self,pop,*arg,**karg):
        front = [pop_tmp['objects'] for pop_tmp in pop]

        
        hv  =HyperVolume(self.R)
        self.HVs.append(hv.compute(front)/self.K)
    def close(self):
        plt.plot(range(len(self.HVs)),self.HVs)
        print('close')
        plt.xlabel('genetations')
        plt.ylabel('HV')
        plt.title('HV in each generations')
        plt.show()


        


