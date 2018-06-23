'''
Created on 2013-1-20

@author: Administrator
'''

import math
import g01_conf
#import protools

n = 13
upper=g01_conf.upper
lower=g01_conf.lower
prec=g01_conf.prec
keys=g01_conf.keys
constraints_num=9
objective_num=1

division = 3
insi_division = 2

def problem_initialize():
    
    return n,upper,lower,prec,constraints_num,objective_num

def evaluate(ind):
    x=ind['pheno']
    g1 =2*x[0]+2*x[1]+x[9]+x[10]-10
    g2 =2*x[0]+2*x[2]+x[9]+x[11]-10
    g3=2*x[1]+2*x[2]+x[10]+x[11]-10
    g4=-8*x[0]+x[9]
    g5=-8*x[1]+x[10]
    g6=-8*x[2]+x[11]
    g7=-2*x[3]-x[4]+x[9]
    g8=-2*x[5]-x[6]+x[10]
    g9=-2*x[7]-x[8]+x[11]
    f1=5*(x[0]+x[1]+x[2]+x[3])
    f2=5*(x[0]*x[0]+x[1]*x[1]+x[2]*x[2]+x[3]*x[3])
    f3=0.0
    for i in range(4,13):
        f3=f3+x[i]
    
    f = f1-f2-f3
    r={}
    r['objectives'] = [f]
    v = []
    v.append(g1 )
    v.append(g2 )
    v.append(g3 )
    v.append(g4 )
    v.append(g5 )
    v.append(g6 )
    v.append(g7 )
    v.append(g8 )
    v.append(g9 )
    r['constraints'] = v
    if ind.get("id") != None:
        r['id'] = ind['id']
    r['valid'] = True
    r['extrainfo'] = {}
    r['extrainfo']['filename'] = None
    r['modifypheno']=0
      

    return r

if __name__ == '__main__':
    x={}

    x['pheno'] = [1,1,1,1,1,1,1,1,1,3,3,3,1]


    for i in range(len(x['pheno'])):
        if 9<=i and i<12:
            x['pheno'][i]=x['pheno'][i]/100.0
    
    print evaluate(x)
