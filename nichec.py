#/usr/bin/python

import numpy as np

'''

'''

z = 1.0e-8
Nearzero = 1.0e-15
delta = 1e-8


def caculate_nichecount(inds,sigma):
    '''
    describe：
        caculate_nichecount.
        nc(x|U)
    Args:
        inds: np.array, Nxgens
        sigma:float, radius
    return:
        None
    '''
    N,_ = inds.shape

    for i in range(N):
        # caculate distance
        # if dst >\sigma,then sh(x_1,x_2) = 0; => \frac {d(\vec x_1,\vec x_2)} {\sigma} \geq 1 =>sh<0
        # we can assume:sh(x_1,x_1) = 0 
        dst = np.sqrt(
            np.sum(
               np.square (inds[i] - inds),
               axis = 1
            )
        )

        sh = 1 - 1.0*dst/sigma
        sh[sh <0] = 0
        inds['i']['nichec'] = np.sum(sh)-1
     


def get_niche_params(MaxK,lower,N,upper,pointAmount):
    '''
    describe:
        get initial sigma and param C,D
    Args:
        MaxK:int, the max iter
        lower:np.array
        upper:np.array
        N:int,the dimension ,the gens count
        PointAmount:int
    return:
        R0:float ,initial sigma
        C:float,param C
        D:float,param D
    '''
    cp = 2 # constant
    difference = upper - lower
    production = np.prod(difference)
    R0 = 0.5*((2*N*production)/(pointAmount*np.pi))**(1.0/N) #
    C = R0+delta                                            # $C=\sigma^{(0)}+\delta
    #caculate D
    q = np.log((R0+delta)/delta)
    D = MaxK/q**(1.0/cp)
    return R0,C,D


def reduce_radius(k,C,D):
    '''
    descibe:
        reduce the sigma echo iter
        $$\sigma = Ce^-(s/D)^cp -\delta$$
    Args:
        k:int the state
        C:float,a param
        D:float,a param
    return:
        R:float,the next sigma
    '''
    cp=2
    R =C*np.exp(-(k/D)**cp)-delta

    return R


