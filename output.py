#/usr/bin/python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
plt.style.use('ggplot')

def plot3(x,y,z,*args,**kargs):
    fig = plt.figure()
    ax = Axes3D(fig)
    elev = 10 if 'elev' not in kargs.keys() else kargs['elev']
    azim =  11 if 'azim' not in kargs.keys() else kargs['azim']
    ax.view_init(elev = kargs['elev'],azim = kargs['azim'])
    ax.plot(x,y,z,*args)
    plt.show()


def output(TrueValue,FunValue):
    fig = plt.figure()
    ax = Axes3D(fig)
    
    ax.view_init(50 ,50 )
    # truevalue
    ax.scatter(TrueValue[:,0],TrueValue[:,1],TrueValue[:,2],'b')
    ax.scatter(FunValue[:,0],FunValue[:,1],FunValue[:,2],'r')
    ax.set_xlim(0.0,1.0)
    ax.set_ylim(0.0,1.0)
    ax.set_zlim(0.0,1.0)
    
    plt.show()

def main():
    from scipy.io import loadmat
    dat = loadmat('draw.mat')
    TrueValue = dat['TrueValue']
    FunValue = dat['FunctionValue']
    print(TrueValue)
   
    output(TrueValue,FunValue)


    


if __name__ == '__main__':
    main()