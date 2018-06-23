'''
Created on 2013-6-24

@author: Administrator
'''
import math
import g24_conf
#import protools


moudle=g24_conf
upper=moudle.upper
lower=moudle.lower
prec=moudle.prec
keys=moudle.keys
constraints_num=2
objective_num=1
division = 12
n = 2

def problem_initialize():
    
    return n,upper,lower,prec,constraints_num,objective_num

def evaluate(ind):
    x= ind['pheno']
    
    f=-x[0]-x[1]
    
    g1=-2*pow(x[0],4)+8*pow(x[0],3)-8*pow(x[0],2)+x[1]-2    
    g2=-4*pow(x[0],4)+32*pow(x[0],3)-88*pow(x[0],2)+96*x[0]+x[1]-36  
    r={}
    r['objectives'] = [f]
    v = []
    v.append(g1)
    v.append(g2)

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
    x['pheno']=[2.32952019747762,3.17849307411774]
    print evaluate(x)
