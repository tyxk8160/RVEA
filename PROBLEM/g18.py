'''
Created on 2013-1-20

@author: Administrator
'''
import math
import g18_conf
#import protools


moudle=g18_conf
upper=moudle.upper
lower=moudle.lower
prec=moudle.prec
keys=moudle.keys
constraints_num=13
objective_num=1

n = 9

def problem_initialize():
    
    return n,upper,lower,prec,constraints_num,objective_num

def evaluate(ind):
    x= ind['pheno']
    
    f=-0.5*(x[0]*x[3]-x[1]*x[2]+x[2]*x[8]-x[4]*x[8]+x[4]*x[7]-x[5]*x[6])
    g1=x[2]*x[2]+x[3]*x[3]-1
    g2=x[8]*x[8]-1
    g3=x[4]*x[4]+x[5]*x[5]-1
    g4=x[0]*x[0]+(x[1]-x[8])*(x[1]-x[8])-1
    g5=pow(x[0]-x[4],2)+pow(x[1]-x[5],2)-1
    g6=pow(x[0]-x[6],2)+pow(x[1]-x[7],2)-1
    g7=pow(x[2]-x[4],2)+pow(x[3]-x[5],2)-1
    g8=pow(x[2]-x[6],2)+pow(x[3]-x[7],2)-1
    g9=x[6]*x[6]+pow(x[7]-x[8],2)-1
    g10=x[1]*x[2]-x[0]*x[3]
    g11=-x[2]*x[8]
    g12=x[4]*x[8]
    g13=x[5]*x[6]-x[4]*x[7]
    r={}
    r['objectives'] = [f]
    v = []
    v.append(g1)
    v.append(g2)
    v.append(g3)
    v.append(g4)
    v.append(g5)
    v.append(g6)
    v.append(g7)
    v.append(g8)
    v.append(g9)
    v.append(g10)
    v.append(g11)
    v.append(g12)
    v.append(g13)
    
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
    x['pheno'] = [-0.657776192427943163,-0.153418773482438542,0.323413871675240938,
         -0.946257611651304398,-0.657776194376798906,-0.753213434632691414,
         0.323413874123576972,-0.346462947962331735,0.59979466285217542]
    print evaluate(x)
    
    
