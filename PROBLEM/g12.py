import math
import g12_conf
#import protools


moudle=g12_conf
upper=moudle.upper
lower=moudle.lower
prec=moudle.prec
keys=moudle.keys
constraints_num=1
objective_num=1
division = 90
n = 3

def problem_initialize():
    
    return n,upper,lower,prec,constraints_num,objective_num

def evaluate(ind):
    x= ind['pheno']
    
    f = -(100-pow(x[0]-5,2)-pow(x[1]-5,2)-pow(x[2]-5,2))/100
    r={}
    r['objectives'] =[f]
    v = []

    g = []
    for i in range(9):
        gi = pow(x[0]- i + 1,2)+pow(x[1]- i + 1,2)+pow(x[2]- i + 1,2)-0.0625
        g.append(gi)
    g0 = g[0]
    for i in range(len(g)):
        if g[i] < g0:
            g0 = g[i]
            
    v.append(g0 )
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
    x['pheno']= [5,5,5]
   
    print evaluate(x)
