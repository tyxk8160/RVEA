'''
Created on 2013-1-20

@author: Administrator
'''
import math
import H09_conf
#import protools


moudle=H09_conf
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
    g2=0.0
    for i in xrange(1,(D+1)):
        g1=g1+pow(x[i],2)
        g2=g2+math.sin(math.pi*x[i]/50)
    g1=(-50)+g1/(100*D)
    g2=50*g2
    g3_1=0.0
    g3_2=1
    for i in xrange(1,(D+1)):
        g3_1=g3_1+pow(x[i],2)/4000
        g3_2=g3_2*math.cos(x[i]/(pow(i,0.5)))
    g3=75-50*(g3_1-g3_2+1)
    r={}
    r['objectives'] = [f]
    v = []
    v.append(g1 )
    v.append(g2 )
    v.append(g3 )
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
    
    
