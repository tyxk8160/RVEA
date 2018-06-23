'''
Created on 2013-1-12

@author: Administrator
'''
import math
import g02_conf
#import protools


moudle=g02_conf
upper=moudle.upper
lower=moudle.lower
prec=moudle.prec
keys=moudle.keys
constraints_num=2
objective_num=1

division = 12   

n=20
def problem_initialize():
    
    return n,upper,lower,prec,constraints_num,objective_num

def evaluate(ind):
    x= ind['pheno']
    g1 = 1.0
    for i in x:
        g1 *= i
    g1 = 0.75 - g1
    g2 = sum(x) - 7.5 * 20
    f1 = [math.cos(i)**4 for i in x]
    f1 = sum(f1)
    f2 = 1.0
    for i in x:
        f2 *= math.cos(i)**2
    f2 *= 2
    f3 = 0.0
    for i in range(n):
        f3+=(i+1)*x[i]**2
    f3 = f3**0.5
    f = -abs((f1-f2)/f3)
    r={}
    r['objectives'] = [f]
    v = []
    v.append(g1 )
    v.append(g2 )
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
    x['pheno'] = [3.16246061572185,3.12833142812967,3.09479212988791,3.06145059523469,3.02792915885555,
         2.99382606701730,2.95866871765285,2.92184227312450,0.49482511456933,0.48835711005490,
         0.48231642711865,0.47664475092742,0.47129550835493,0.46623099264167,0.46142004984199,
         0.45683664767217,0.45245876903267,0.44826762241853,0.44424700958760,0.44038285956317]
    x['pheno'] = [i/10 for i in x['pheno']]
    print evaluate(x)
