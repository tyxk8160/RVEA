
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


      

def generate_combnum(m,d):         ###generate m-dimension combined number which sum is d ,
                                   ###all numbers form a list,this function results the list
    nums=[]

    if m == 2:
        nums=[]
        for i in range(d+1):
            nums.append( i )
            nums.append( d-i )
    else:
        nums=[]
        for i in range(d+1):
            v_s = generate_combnum(m-1,d-i)
            #ipdb.set_trace()

            
            for j in range( int(len(v_s)/(m -1 )) ):
              
                nums.append(i)
                
                for k in range(m-1):
                    
                    nums.append(v_s[ j * (m - 1) + k])
                               
    return nums

def get_vectorlist(m,d):         ####from the above list to m-dimension vector,
    nums = generate_combnum(m,d)                                    ####these vectors form a vector-list 
    v = []
    for i in range(int(len(nums)/m)):
        ve=[]
        for j in range(m):
            ve.append(round(nums[i * m +j]*1.0/d,4))
        v.append(ve)
    return v
def get_inside_vectorlist(m,insi_d):
    boundary_vectors = get_vectorlist(m,insi_d)
    center_vector = []
    for i in range(m):
        center_vector.append(1.0/float(m))
    inside_vectors = []
    for vec in boundary_vectors:
        insi_vec = []
        for i in range(m):
            insi_vec.append((vec[i] - center_vector[i]) / 2.0 + center_vector[i])
        inside_vectors.append(insi_vec)
    return inside_vectors
def test(m,d,insi_d):
 
    if insi_d == 0:
    #vectors = get_vectorlist(m,d)
    #print vectors
    
    #vectors_new = matrix_transform(m,d)
    #print vectors_new

    #vectors_new2 = get_inside_vectorlist(m,insi_d)
    #print vectors_new2

        return get_vectorlist(m,d)
    else:
        L=get_vectorlist(m,d)+get_inside_vectorlist(m,insi_d)
        # print (get_vectorlist(m,d)+get_inside_vectorlist(m,insi_d))
        return L


    
if __name__ == '__main__':

    m = 3
    d = 3
    insi_d = 1
    if insi_d == 0:
    #vectors = get_vectorlist(m,d)
    #print vectors
    
    #vectors_new = matrix_transform(m,d)
    #print vectors_new

    #vectors_new2 = get_inside_vectorlist(m,insi_d)
    #print vectors_new2

        print (get_vectorlist(m,d))
    else:
        print (get_vectorlist(m,d)+get_inside_vectorlist(m,insi_d))
         
         
        

    
