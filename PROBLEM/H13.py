'''
Created on 2013-1-20

@author: Administrator
'''
import math
import H13_conf
#import protools


moudle=H13_conf
upper=moudle.upper
lower=moudle.lower
prec=moudle.prec
keys=moudle.keys
constraints_num=2
objective_num=1

n = 10

def problem_initialize():
    
    return n,upper,lower,prec,constraints_num,objective_num


def evaluate(ind):
    D=10
    x= ind['pheno']
    
    f=max(x)

    g1=0.0
    g2=0.0
    for i in xrange(D):
        g1=g1+(-x[i])*math.sin(pow(abs(x[i]),0.5))
        g2=g2+x[i]*math.cos(pow(abs(x[i]),0.5))

    g1=g1/D
    g2=g2/D
  
    r={}
    r['objectives'] = [f]
    v = []
    v.append(g1 )
    v.append(g2 )
    r['constraints'] = v
    if ind.get("id") != None:#####!!!!
        r['id'] = ind['id']
    r['valid'] = True
    r['extrainfo'] = {}
    r['extrainfo']['filename'] = None
    r['modifypheno']=0
    
    return r

if __name__ == '__main__':
    x={}
    x['pheno'] = [10,10,10,10,10,10,10,10,10,10]
    print evaluate(x)
    
    
