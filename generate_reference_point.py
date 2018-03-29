


#import ipdb
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

        print (get_vectorlist(m,d))
    else:
        L=get_vectorlist(m,d)+get_inside_vectorlist(m,insi_d)
        # print (get_vectorlist(m,d)+get_inside_vectorlist(m,insi_d))
        return L
    
        
         
         
        


test(3,3,1)



   
    
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
         
         
        

    
