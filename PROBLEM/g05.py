'''
Created on 2013-1-22

@author: Administrator
'''
import math
import g05_conf
#import protools

n = 4
upper=g05_conf.upper
lower=g05_conf.lower
prec=g05_conf.prec
keys=g05_conf.keys
constraints_num=5
objective_num=1
division = 3
def problem_initialize():
    
    return n,upper,lower,prec,constraints_num,objective_num

def evaluate(ind):
    x=ind['pheno']

    f=3*x[0]+0.000001*pow(x[0],3)+2*x[1]+(0.000002/3)*pow(x[1],3)
    g1=-x[3]+x[2]-0.55
    g2=-x[2]+x[3]-0.55
    p=0.0001
    h1=1000*math.sin(-x[2]-0.25)+1000*math.sin(-x[3]-0.25)+894.8-x[0]
    h2=1000*math.sin(x[2]-0.25)+1000*math.sin(x[2]-x[3]-0.25)+894.8-x[1]
    h3=1000*math.sin(x[3]-0.25)+1000*math.sin(x[3]-x[2]-0.25)+1294.8
    h1=abs(h1)-p
    h2=abs(h2)-p
    h3=abs(h3)-p
    r={}
    r['objectives'] = [f]
    v = []
    v.append(g1 )
    v.append(g2 )

    v.append(h1 )
    v.append(h2 )
    v.append(h3 )
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
    x['pheno'] = [679.945148297028709, 1026.06697600004691, 0.118876369094410433,-0.39623348521517826]
    print evaluate(x)
