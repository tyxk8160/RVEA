#/usr/bin/python
'''
generate uniform reference vector 
'''
from itertools import combinations
import numpy as np
from scipy.special import comb # for compute combination

def uniform_point(N,M):
    '''
    describe:
        Generate a set of uniformly distributed points on the unit hyperplane
    Args:
        N:int, the population
        M:int,the count of genes
    return:
        V:np.array,uniform point
        N1:int,the number of uniform point
    '''
    # maybe not elegance ~_~
    H1 = 1
    while comb(H1+M,M-1)<=N:
        H1+=1
    comb_vec = np.array(list(combinations(range(H1+M-1),M-1))) # 
    ## need add the last collumn and zeros collumn
    
    one_array = np.ones((comb_vec.shape[0],1))
    comb_vec = np.column_stack((one_array*-1,
                               comb_vec,
                               one_array*(H1+M-1)))
    
    V = np.diff(comb_vec,axis = 1)-1    # tricks
    
    

    # 
    if H1 < M:
        H2 = 0
        while comb(H2+M,M-1)+comb(H1+M-1,M-1) <=N:
            H2+=1
        if H2 > 0:
            comb_vec = np.array(list(combinations(range(H2+M-1),M-1))) # 
            one_array = np.ones((comb_vec.shape[0],1))
            comb_vec = np.column_stack((one_array*-1,
                               comb_vec,
                               one_array*(H2+M-1)))
            V2 = np.diff(comb_vec,axis = 1)-1 #tricks
            
            V = np.row_stack((V,V2))
    # norm
    V = V/np.sqrt(np.sum(np.square(V),axis=1)).reshape(-1,1)  # $v_i = \frac {v_i} {\sqrt{\sum_i^M v_i ^2}}$
    return V,V.shape[0]






if __name__ == '__main__':
    V0,_=uniform_point(105,3)
    print(V0)