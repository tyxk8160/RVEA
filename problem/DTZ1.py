

#/usr/bin/python
'''
'''
import numpy as np



M = 3 # default number of objects 

def evaluate(ind):
    '''
    describe:
        $g(X_M) = 100[M+\sum [(x_i-0.5)^2-\cos^2 (20*pi*(x_i-0.5))]$

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
    print(D-M+1)
    g = 100*(D-M+1+np.sum(
        np.square((x[M-1:]-0.5))-np.cos(20*np.pi*(x[M-1:]-0.5)))
        )
    print(g)

    F = [] # objects
    for i in range(M):
        f = 0.5*np.prod(x[:M-i-1])*(1+g)
        if i >0:
            f = f*(1-x[M-i])
        F.append(f)
    ind['objects'] = F
    


def main():
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
    
        if np.abs(diff) >1e-15:
            print("Failed:case")
            print(genes)
            print('diff=',diff)
            print('='*15)



if __name__ == '__main__':
    main()