'''
Created on 2013-1-20

@author: Administrator
'''
import math
import H01_conf
#import protools


moudle=H01_conf
upper=moudle.upper
lower=moudle.lower
prec=moudle.prec
keys=moudle.keys
constraints_num=3
objective_num=1

n = 10

def problem_initialize():
    
    return n,upper,lower,prec,constraints_num,objective_num




def evaluate(ind):
    D=10

    x= ind['pheno']
    
    f=0.0
    for i in xrange(D):
        f=f+pow(x[i],2)

    e=0.0001
    gsum=0.0
    h1=0.0
    h2=0.0
    for i in xrange(D):
        gsum=gsum+(-x[i])*math.cos (pow(abs(x[i]),0.5))
    g1=gsum/D
    for i in xrange(D/2):
        h1=h1+(-x[2*i])*math.cos(pow(abs(x[2*i]),0.5))
        h2=h2+(-x[2*i+1])*math.cos(pow(abs(x[2*i+1]),0.5))

    
    h1=abs(h1)-0.0001
    h2=abs(h2)-0.0001
    r={}
    r['objectives'] = [f]
    v = []
    v.append(g1 )
    v.append(h1 )
    v.append(h2 )
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
    
    
