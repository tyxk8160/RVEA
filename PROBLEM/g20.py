'''
Created on 2013-1-20

@author: Administrator
'''
import math
import g20_conf
#import protools


moudle=g20_conf
upper=moudle.upper
lower=moudle.lower
prec=moudle.prec
keys=moudle.keys
constraints_num=20
objective_num=1

n = 24

def problem_initialize():
    
    return n,upper,lower,prec,constraints_num,objective_num

def evaluate(ind):
    x= ind['pheno']
    
    a=[0.0693,0.0577,0.05,0.2,0.26,0.55,0.06,0.1,0.12,0.18,0.1,0.09,0.0693,0.0577,0.05,0.2,0.26,0.55,0.06,0.1,0.12,0.18,0.1,0.09]
    b=[44.094,58.12,58.12,137.4,120.9,170.9,62.501,84.94,133.425,82.507,46.07,60.097,44.094,58.12,58.12,137.4,120.9,170.9,62.501,84.94,133.425,82.507,46.07,60.097]
    c=[123.7,31.7,45.7,14.7,84.7,27.7,49.7,7.1,2.1,17.7,0.85,0.64]
    d=[31.244,36.12,34.784,92.7,82.7,91.6,56.708,82.7,80.8,64.517,49.4,49.1]
    e=[0.1,0.3,0.4,0.3,0.6,0.3]
    f1=0.0
    for i in range(24):
        f1=f1+a[i]*x[i]
    f=f1
    gg1=0.0
    for i in range(24):
        gg1=gg1+x[i]
    g1=(x[0]+x[12])/(gg1+e[0])
    g2=(x[1]+x[13])/(gg1+e[1])
    g3=(x[2]+x[14])/(gg1+e[2])
    g4=(x[6]+x[18])/(gg1+e[3])
    g5=(x[7]+x[19])/(gg1+e[4])
    g6=(x[8]+x[20])/(gg1+e[5])
    gg2=0.0
    for i in range(12,24):
        gg2=gg2+x[i]/b[i]
    gg3=0.0
    for i in range(12):
        gg3=gg3+x[i]/b[i]
    h1=math.fabs(x[12]/(b[12]*gg2)-(c[0]*x[0])/(40*b[0]*gg3))-0.0001
    h2=math.fabs(x[13]/(b[13]*gg2)-(c[1]*x[1])/(40*b[1]*gg3))-0.0001
    h3=math.fabs(x[14]/(b[14]*gg2)-(c[2]*x[2])/(40*b[2]*gg3))-0.0001
    h4=math.fabs(x[15]/(b[15]*gg2)-(c[3]*x[3])/(40*b[3]*gg3))-0.0001
    h5=math.fabs(x[16]/(b[16]*gg2)-(c[4]*x[4])/(40*b[4]*gg3))-0.0001
    h6=math.fabs(x[17]/(b[17]*gg2)-(c[5]*x[5])/(40*b[5]*gg3))-0.0001
    h7=math.fabs(x[18]/(b[18]*gg2)-(c[6]*x[6])/(40*b[6]*gg3))-0.0001
    h8=math.fabs(x[19]/(b[19]*gg2)-(c[7]*x[7])/(40*b[7]*gg3))-0.0001
    h9=math.fabs(x[20]/(b[20]*gg2)-(c[8]*x[8])/(40*b[8]*gg3))-0.0001
    h10=math.fabs(x[21]/(b[21]*gg2)-(c[9]*x[9])/(40*b[9]*gg3))-0.0001
    h11=math.fabs(x[22]/(b[22]*gg2)-(c[10]*x[10])/(40*b[10]*gg3))-0.0001
    h12=math.fabs(x[23]/(b[23]*gg2)-(c[11]*x[11])/(40*b[11]*gg3))-0.0001
    h13=math.fabs(gg1-1)-0.0001
    gg4=0.0
    for i in range(12):
        gg4=gg4+x[i]/d[i]
    k=0.7302*530*(14.7/40)
    h14=math.fabs(gg4+k*gg2-1.671)-0.0001
    
    r={}
    r['objectives'] = [f]
    v = []
    v.append(g1)
    v.append(g2)
    v.append(g3)
    v.append(g4)
    v.append(g5)
    v.append(g6)
    v.append(h1)
    v.append(h2)
    v.append(h3)
    v.append(h4)
    v.append(h5)
    v.append(h6)
    v.append(h7)
    v.append(h8)
    v.append(h9)
    v.append(h10)
    v.append(h11)
    v.append(h12)
    v.append(h13)
    v.append(h14)
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
    x['pheno'] = [1.28582343498528086e-18, 4.83460302526130664e-34, 0, 0, 6.30459929660781851e-18, 7.57192526201145068e-34, 5.03350698372840437e-34,9.28268079616618064e-34, 0, 1.76723384525547359e-17, 3.55686101822965701e-34,2.99413850083471346e-34, 0.158143376337580827, 2.29601774161699833e-19, 1.06106938611042947e-18, 1.31968344319506391e-18, 0.530902525044209539, 0,2.89148310257773535e-18,3.34892126180666159e-18, 0, 0.310999974151577319, 5.41244666317833561e-05, 4.84993165246959553e-16]
    x['pheno']= [i/10 for i in x['pheno']]
    print evaluate(x)
