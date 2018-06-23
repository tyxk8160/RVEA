'''
Created on 2013-1-22

@author: Administrator
'''
import math
import g07_conf
#import protools

n = 10
upper=g07_conf.upper
lower=g07_conf.lower
prec=g07_conf.prec
keys=g07_conf.keys
constraints_num=8
objective_num=1
def problem_initialize():
    
    return n,upper,lower,prec,constraints_num,objective_num

def evaluate(ind):
    x=ind['pheno']
    f1=x[0]*x[0]+x[1]*x[1]+x[0]*x[1]-14*x[0]-16*x[1]
    f2=(x[2]-10)*(x[2]-10)+4*(x[3]-5)*(x[3]-5)
    f3=(x[4]-3)*(x[4]-3)+2*(x[5]-1)*(x[5]-1)+5*x[6]*x[6]
    f4=7*(x[7]-11)*(x[7]-11)+2*(x[8]-10)*(x[8]-10)+(x[9]-7)*(x[9]-7)+45
    f=f1+f2+f3+f4
    g1=-105+4*x[0]+5*x[1]-3*x[6]+9*x[7]
    g2=10*x[0]-8*x[1]-17*x[6]+2*x[7]
    g3=-8*x[0]+2*x[1]+5*x[8]-2*x[9]-12
    g4=3*(x[0]-2)*(x[0]-2)+4*(x[1]-3)*(x[1]-3)+2*x[2]*x[2]-7*x[3]-120
    g5=5*x[0]*x[0]+8*x[1]+(x[2]-6)*(x[2]-6)-2*x[3]-40
    g6=x[0]*x[0]+2*(x[1]-2)*(x[1]-2)-2*x[0]*x[1]+14*x[4]-6*x[5]
    g7=0.5*(x[0]-8)*(x[0]-8)+2*(x[1]-4)*(x[1]-4)+3*x[4]*x[4]-x[5]-30
    g8=-3*x[0]+6*x[1]+12*(x[8]-8)*(x[8]-8)-7*x[9]

    r={}
    r['objectives'] = [f]
    v = []
    v.append(g1 )
    v.append(g2 )
    v.append(g3 )
    v.append(g4 )
    v.append(g5 )
    v.append(g6 )
    v.append(g7 )
    v.append(g8 )
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
    x['pheno'] = [2.17199634142692, 2.3636830416034,8.77392573913157, 5.09598443745173, 0.990654756560493, 1.43057392853463, 1.32164415364306,9.82872576524495, 8.2800915887356, 8.3759266477347]
    print evaluate(x)
