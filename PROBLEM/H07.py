'''
Created on 2013-1-20

@author: Administrator
'''
import math
import H07_conf
#import protools


moudle=H07_conf
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
    x=[0]
    x.extend(ind['pheno'])
    
    f=0.0
    for i in xrange(1,(D+1)):
        f=f+((-x[i])*math.sin(pow(abs(x[i]),0.5)))
    f=f/D
    g1=0.0
    for i in xrange(1,D):
        g1=g1+(pow((pow(x[i],2)-x[i+1]),2)+pow((x[i]-1),2))
    g2_1=1
    g2_2=1
    for i in xrange(1,(D+1)):
        g2_1=g2_1*pow(x[i],2)/4000
        g2_2=g2_2*math.cos(x[i]/(pow(i,0.5)))
    g1=-100+g1
    g2=-20+g2_1-g2_2+1
    h1=0.0
    for i in xrange(1,D):
        h1=h1+pow((pow(x[i],2)-x[i+1]),2)
    p=0.0001
    h1=abs(h1)-p
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
    
    
