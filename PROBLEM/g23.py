'''
Created on 2013-6-24

@author: Administrator
'''
import math
import g23_conf
#import protools


moudle=g23_conf
upper=moudle.upper
lower=moudle.lower
prec=moudle.prec
keys=moudle.keys
constraints_num=6
objective_num=1

n = 9

def problem_initialize():
    
    return n,upper,lower,prec,constraints_num,objective_num

def evaluate(ind):
    x= ind['pheno']
    
    f=-9*x[4]-15*x[7]+6*x[0]+16*x[1]+10*(x[5]+x[6])
    
    g1=x[8]*x[2]+0.02*x[5]-0.025*x[4]
    g2=x[8]*x[3]+0.02*x[6]-0.015*x[7]
    g3=x[0]+x[1]-x[2]-x[3]
    g3=abs(g3)-0.0001
    g4=0.03*x[0]+0.01*x[1]-x[8]*(x[2]+x[3])
    g4=abs(g4)-0.0001
    g5=x[2]+x[5]-x[4]
    g5=abs(g5)-0.0001
    g6=x[3]+x[6]-x[7]
    g6=abs(g6)-0.0001    
    r={}
    r['objectives'] = [f]
    v = []
    v.append(g1)
    v.append(g2)
    v.append(g3)
    v.append(g4)
    v.append(g5)
    v.append(g6)
   
    r['constraints'] = v
    if ind.get("id") != None:#####!!!!
        r['id'] = ind['id']
    r['valid'] = True
    r['extrainfo'] = {}
    r['extrainfo']['filename'] = None
    r['modifypheno']=0
    
    return r

if __name__ == '__main__':

    x = {}
    x['pheno']=[0.00510000000000259465, 99.9947000000000514,
9.01920162996045897e-18, 99.9999000000000535, 0.000100000000027086086, 2.75700683389584542e-14, 99.9999999999999574, 200,0.0100000100000100008]
    print evaluate(x)
