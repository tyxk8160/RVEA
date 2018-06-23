''' Created on 2013-1-20

@author: Administrator '''


import math
import g10_conf
#import protools


moudle=g10_conf
upper=moudle.upper
lower=moudle.lower
prec=moudle.prec
keys=moudle.keys
constraints_num=6
objective_num=1
n = 8
def problem_initialize():
    
    return n,upper,lower,prec,constraints_num,objective_num

def evaluate(ind):
    x= ind['pheno']
    g1=(-1)+0.0025*(x[3]+x[5])
    g2=(-1)+0.0025*(x[4]+x[6]-x[3])
    g3=(-1)+0.01*(x[7]-x[4])
    g4=(-1)*x[0]*x[5]+833.33252*x[3]+100*x[0]-83333.333
    g5=(-1)*x[1]*x[6]+1250*x[4]+x[1]*x[3]-1250*x[3]
    g6=(-1)*x[2]*x[7]+1250000+x[2]*x[4]-2500*x[4]
    f=x[0]+x[1]+x[2]
    r={}
    r['objectives'] = [f]
    v=[]
    v.append(g1 )
    v.append(g2 )
    v.append(g3 )
    v.append(g4 )
    v.append(g5 )
    v.append(g6 )
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
    x['pheno'] = [579.306685017979589, 1359.97067807935605, 5109.97065743133317, 182.01769963061534,295.601173702746792, 217.982300369384632, 286.41652592786852, 395.601173702746735]
    

    

    print evaluate(x)
