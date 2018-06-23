'''
Created on 2013-1-20

@author: Administrator
'''
import math
import g04_conf
#import protools

n = 5
upper=g04_conf.upper
lower=g04_conf.lower
prec=g04_conf.prec
keys=g04_conf.keys
constraints_num=6
objective_num=1
def problem_initialize():
    
    return n,upper,lower,prec,constraints_num,objective_num

def evaluate(ind):
    x= ind['pheno']
   
    f=5.3578547*pow(x[2],2)+0.8356891*x[0]*x[4]+37.293239*x[0]-40792.141
    g1=85.334407+0.0056858*x[1]*x[4]+0.0006262*x[0]*x[3]-0.0022053*x[2]*x[4]-92
    g2=-85.334407-0.0056858*x[1]*x[4]-0.0006262*x[0]*x[3]+0.0022053*x[2]*x[4]
    g3=80.51249+0.0071317*x[1]*x[4]+0.0029955*x[0]*x[2]+0.0021813*x[2]*x[2]-110
    g4=-80.51249-0.0071317*x[1]*x[4]-0.0029955*x[0]*x[2]-0.0021813*x[2]*x[2]+90
    g5=9.300961+0.0047026*x[2]*x[4]+0.0012547*x[0]*x[2]+0.0019085*x[2]*x[3]-25
    g6=-9.300961-0.0047026*x[2]*x[4]-0.0012547*x[0]*x[2]-0.0019085*x[2]*x[3]+20
    r={}
    r['objectives'] = [f]
    v = []
    v.append(g1 )
    v.append(g2 )
    v.append(g3 )
    v.append(g4 )
    v.append(g5 )
    v.append(g6 )
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
    x['pheno'] = [78,33, 29.9952560256815985, 45,36.7758129057882073]
    print evaluate(x)
    
    
