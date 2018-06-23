'''
Created on 2013-1-20

@author: Administrator
'''
import math
import g11_conf
#import protools


moudle=g11_conf
upper=moudle.upper
lower=moudle.lower
prec=moudle.prec
keys=moudle.keys
constraints_num=1
objective_num=1
division = 90
n = 2

def problem_initialize():
    
    return n,upper,lower,prec,constraints_num,objective_num

def evaluate(ind):
    x= ind['pheno']
    h1=x[1]-x[0]*x[0]
    h2=math.fabs(h1)-0.0001
    f=x[0]*x[0]+math.pow((x[1]-1), 2)
    r={}
    r['objectives'] = [f]
    v = []
    v.append(h2)
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
    x['pheno'] = [-0.707036070037170616,0.500000004333606807]
    x['pheno']=[(x['pheno'][i]+1)/2 for i in range(2)]
    print evaluate(x)
