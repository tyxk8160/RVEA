#/usr/bin/python

from util.draw import DrawFigure
import numpy as np

class FigureOut():
    def __init__(self,TrueValue):
        '''
        pass
        '''
        self.TrueValue = TrueValue
        self.fig = DrawFigure()

    
    def display(self,pop,*args,**kargs):
        '''
        '''
        TrueValue = self.TrueValue
        ax = self.fig.ax
        ax.cla()
        FunValue = np.asarray([pop_tmp['objects'] for pop_tmp in pop],dtype=float)
         # truevalue
        ax.scatter(TrueValue[:,0],TrueValue[:,1],TrueValue[:,2],'b')
        ax.scatter(FunValue[:,0],FunValue[:,1],FunValue[:,2],'r')
        self.fig.plt.pause(0.1)
    def close(self,*args,**kargs):
        '''
        '''
        pass

    