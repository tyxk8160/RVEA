'''
Created on 2013-1-20

@author: Administrator
'''
import math
import H08_conf
#import protools


moudle=H08_conf
upper=moudle.upper
lower=moudle.lower
prec=moudle.prec
keys=moudle.keys
constraints_num=1
objective_num=1

n = 10

def problem_initialize():
    
    return n,upper,lower,prec,constraints_num,objective_num

def evaluate(ind):
    D=10
    x= ind['pheno']
    
    f=max(x)
    h1=0.0
    p=0.0001
    for i in xrange(D):
        h1=h1+((-x[i])*math.sin(pow(abs(x[i]),0.5)))
    h1=abs(h1/D)-p
    r={}
    r['objectives'] = [f]
    v = []
    v.append(h1 )
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
    x['pheno'] = [-483.61,-483.61,-483.61,-483.61,-483.61,-483.61,-483.61,-483.61,-483.61,-483.61]
    print evaluate(x)
    
    
