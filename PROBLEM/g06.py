'''
Created on 2013-1-20

@author: Administrator
'''
import math
import g06_conf
#import protools

n = 2
upper=g06_conf.upper
lower=g06_conf.lower
prec=g06_conf.prec
keys=g06_conf.keys
constraints_num=2
objective_num=1
division = 12 
def problem_initialize():
    
    return n,upper,lower,prec,constraints_num,objective_num

def evaluate(ind):
    x=ind['pheno']
    f=pow(x[0]-10, 3)+pow(x[1]-20,3)
    g1=-(x[0]-5)*(x[0]-5)-(x[1]-5)*(x[1]-5)+100
    g2=(x[0]-6)*(x[0]-6)+(x[1]-5)*(x[1]-5)-82.81
    r={}
    r['objectives'] = [f]
    v = []
    v.append(g1 )
    v.append(g2 )
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
    x['pheno'] = [14.09500000000000064,0.8429607892154795668]
    print evaluate(x)
    
    
