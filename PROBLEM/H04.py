'''
Created on 2013-1-20

@author: Administrator
'''
import math
import H04_conf
#import protools


moudle=H04_conf
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
    x= ind['pheno']

    D=10
    
    f=0.0
    for i in xrange(D):
        f=f+pow(x[i],2)

    p=0.0001
    h1=0.0
    h2=0.0
    for i in xrange(D/2):        
        h2=h2+(x[2*i+1])*math.sin(pow(abs(x[2*i+1]),0.5))
        h1=h1+(-x[2*i])*math.sin(pow(abs(x[2*i]),0.5))
   
    h1=abs(h1)-p
    h2=abs(h2)-p
    r={}
    r['objectives'] =[f]
    v = []
    v.append(h1)
    v.append(h2)
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
    
    
