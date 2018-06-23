'''
Created on 2013-1-20

@author: Administrator
'''
import math
import H06_conf
#import protools


moudle=H06_conf
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
    
    f=0.0
    for i in xrange(D):
        f=f+((-x[i])*math.sin(pow(abs(x[i]),0.5)))
    f=f/D
    g1=0.0
    for i in xrange(D-1):
        g1=g1+(pow((pow(x[i],2)-x[i+1]),2)+pow((x[i]-1),2))
        
   
    g1=-100+g1
    r={}
    r['objectives'] = [f]
    v = []
    v.append(g1)
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
    
    
