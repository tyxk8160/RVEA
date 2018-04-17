

#/usr/bin/python
'''
'''
import numpy as np



M = 3 # default number of objects 

def evaluate(ind):
    '''
    describe:
      DTLZ2

    Args:
        ind:dict
            ind['gens'],list,solution space
            ind['objects'],list,obejcts
            ind['constrait'],list,[],the problem has no constrait
    return:
        None

    '''
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





if __name__ == '__main__':
   
    from scipy.io import loadmat
    dat = loadmat('test.mat')
    A = dat['A']
    B = dat['B']
    N,_ = A.shape
    print('*'*80)
    for i in range(N):
        genes = list(A[i,:])
        ind = {'genes':genes}
        evaluate(ind)
        objects = np.array(ind['objects'])
        FunctionValue = B[i,:]
        diff = np.sum(objects - FunctionValue)
        print(diff)
        if diff >1e-15:
            print("Failed:case")
            print(genes)
            print('diff=',diff)
            print('='*15)

