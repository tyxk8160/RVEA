# /usr/bin/python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
plt.style.use('ggplot')



class DrawFigure(object):
    

    def __init__(self,fig = None,dimension = 3,ion = True):
        '''
        plot 2D or 3D 
        '''
        self.fig = fig
        self.plt = plt
        if self.fig is  None:
            self.fig= plt.figure()
        if dimension == 3:
            self.ax = Axes3D(self.fig)
            self.ax.view_init(50 ,50 )
        else:
            self.ax = plt
        if ion is True:
            plt.ion()
        
     

