#/usr/bin/python
import numpy as np


delta = 1.0e-08
Nearzero = 1.0e-15


def reduce_boundary(k,A,B): 
    '''
    descibe:
        reduce the epsilon echo iter
        $$\epsilon = Ae^-(s/B)^cp -\delta$$
    Args:
        k:int the state
        A:np.arrray,a param
        B:np.array,a param
    return:
        e:np.array,the next epsilon
    '''
    cp=2
    R =C*np.exp(-(k/D)**cp)-delta
    return e

def caculate_violation_objective(pop):
    '''
    describe:
        caculate the cv。$cv(\vec x) = \frac {1}{m}\sum \frac {G_i(\vec x)}{max G_i(\vec x)}
    Args:
        pop:dict 
            pop['violations'] violation value, maybe a list?
            pop['violation_objectives'] ,cv violation_objective,a float

    return:
        None
    '''
    # transform list as array
    # Dimension: N x constraint_cnt
    violations_vec  = np.array([ind['violations'] for ind in pop])
    N,constraint_cnt = violations_vec.shape
    maxG = np.max(violations_vec,axis = 0).reshape(1,-1) # for some fuck case
    cv= violations_vec/maxG  # numpy feature
    cv = np.sum(cv,axis =1)/constraint_cnt

    # transform numpy array to list
    for i in range(N):
        pop[i]['violation_objects'] = cv[i]

def get_vilation_param(pop,MaxK):
    '''
    describe:
        caculte the max vilotion of each constrait and initial param A  and B
    Args:
        pop:dict 
            pop['violations'] violation value, maybe a list?
        MaxK:the max iter times
    return:
        epsilon : np.array,initial epsilon
        A : np.array,param
        B : np.array,param
    '''
    cp = 2
    # transform list as array
    # Dimension: N x constraint_cnt
    violations_vec  = np.array([ind['violations'] for ind in pop])
    N,constraint_cnt = violations_vec.shape
    epsilon = np.max(violations_vec,axis = 0).reshape(1,-1) # for some fuck case
    A = epsilon + delta
    q = np.log((epsilon+delta)/delta)
    B = MaxK/q**(1.0/cp)
    return epsilon,A,B



