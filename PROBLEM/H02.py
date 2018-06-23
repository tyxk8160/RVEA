'''
Created on 2013-1-20

@author: Administrator
'''
import math
import H02_conf
#import protools


moudle=H02_conf
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
    
    f=max(x)

    p=0.0001
    gsum=0.0
    h1sum=0.0
    for i in xrange(D):
        gsum=gsum+(pow(x[i],2)-10*math.cos(2*math.pi*x[i])+10)
        y=x[i]-0.5
        h1sum=h1sum+(pow(y,2)-10*math.cos(2*math.pi*y)+10)
    g1=10-gsum/D
    g2=gsum/D-15.0       
    h1=abs(h1sum/D-20)-p

    r={}
    r['objectives'] = [f]
    v = []
    v.append(g1 )
    v.append(g2 )
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
    x['pheno'] = [10,10,10,10,10,10,10,10,10,10]
    print evaluate(x)
    
    
