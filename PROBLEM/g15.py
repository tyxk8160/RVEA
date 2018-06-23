import math
import g15_conf
#import protools


moudle=g15_conf
upper=moudle.upper
lower=moudle.lower
prec=moudle.prec
keys=moudle.keys
constraints_num=2
objective_num=1

division = 12

n = 3

def problem_initialize():
    
    return n,upper,lower,prec,constraints_num,objective_num

def evaluate(ind):
    x = ind['pheno']
    
    g1 = x[0]*x[0]+x[1]*x[1]+x[2]*x[2]-25
    g1=abs(g1)-0.0001
    g2 = 8*x[0]+14*x[1]+7*x[2]-56
    g2=abs(g2)-0.0001
    
    f = 1000-x[0]*x[0]-2*x[1]*x[1]-x[2]*x[2]-x[0]*x[1]-x[0]*x[2]
    r={}
    r['objectives'] = [f]
    v = []
    v.append(g1)
    v.append(g2)
    r['constraints'] = v
    if ind.get("id") != None:
        r['id'] = ind['id']
    r['valid'] = True
    r['extrainfo'] = {}
    r['extrainfo']['filename'] = None
    r['modifypheno']=0

    
    return r

if __name__ == '__main__':
    x = {}
    x['pheno'] = [3.51212812611795133,0.216987510429556135,3.55217854929179921]
   # x = [i/10 for i in x]
    print evaluate(x)
