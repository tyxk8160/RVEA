'''
Created on 2013-1-20

@author: Administrator
'''
import math
import g13_conf
#import protools


moudle=g13_conf
upper=moudle.upper
lower=moudle.lower
prec=moudle.prec
keys=moudle.keys
constraints_num=3
objective_num=1
division = 6
n = 5

def problem_initialize():
    
    return n,upper,lower,prec,constraints_num,objective_num

def evaluate(ind):
    x = ind['pheno']
    
    f=math.pow(math.e, x[0]*x[1]*x[2]*x[3]*x[4])
    h1=math.fabs(x[0]*x[0]+x[1]*x[1]+x[2]*x[2]+x[3]*x[3]+x[4]*x[4]-10)-0.0001
    h2=math.fabs(x[1]*x[2]-5*x[3]*x[4])-0.0001
    h3=math.fabs(x[0]*x[0]*x[0]+x[1]*x[1]*x[1]+1)-0.0001
    r={}
    r['objectives'] = [f]
    v = []
    v.append(h1)
    v.append(h2)
    v.append(h3)
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
    x['pheno'] = [-1.71714224003, 1.59572124049468, 1.8272502406271,-0.763659881912867,-0.76365986736498]
    print evaluate(x)
    
    
