'''
Created on 2013-1-20

@author: Administrator
'''
import math
import g03_conf
#import protools


n = 10
upper=g03_conf.upper
lower=g03_conf.lower
prec=g03_conf.prec
keys=g03_conf.keys
constraints_num=1
objective_num=1

division = 90  
def problem_initialize():
    
    return n,upper,lower,prec,constraints_num,objective_num

def evaluate(ind):
    x=ind['pheno']
    f1 = 1.0
    for i in x:
        f1 *= i
    f2=-pow(math.sqrt(10),10)
    f=f2*f1
    g1=0.0
    for i in x:
        g1+= pow(i,2)
    g1=g1-1
    g1=abs(g1)-0.0001
    r={}
    r['objectives'] = [f]
    v = []
    v.append(g1 )
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
    x['pheno'] = [0.31624357647283069,0.316243577414338339, 0.316243578012345927,
         0.316243575664017895,0.316243578205526066,0.31624357738855069,
         0.316243575472949512,0.316243577164883938,0.316243578155920302,
         0.316243576147374916]
    
    print evaluate(x)
