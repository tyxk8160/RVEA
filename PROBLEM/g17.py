import math
import g17_conf
#import protools


moudle=g17_conf
upper=moudle.upper
lower=moudle.lower
prec=moudle.prec
keys=moudle.keys
constraints_num=4
objective_num=1

division = 6

n = 6

def problem_initialize():
    
    return n,upper,lower,prec,constraints_num,objective_num

def evaluate(ind):
    x= ind['pheno']
        
    if x[0]<300:
        f1=30*x[0]
    else:
        f1=31*x[0]

    if x[1]<100:
        f2=28*x[1]
    elif x[1]<200:
        f2=29*x[1]
    else:
        f2=30*x[1]

    
    f =f1+f2

    g1=-x[0]+300-x[2]*x[3]/131.078*math.cos(1.48477-x[5])+0.90798*pow(x[2],2)/131.078*math.cos(1.47588)
    g1=abs(g1)-0.0001
    g2=-x[1]-x[2]*x[3]/131.078*math.cos(1.48477+x[5])+0.90798*pow(x[3],2)/131.078*math.cos(1.47588)
    g2=abs(g2)-0.0001
    g3=-x[4]-x[2]*x[3]/131.078*math.sin(1.48477+x[5])+0.90798*pow(x[3],2)/131.078*math.sin(1.47588)
    g3=abs(g3)-0.0001
    g4=200-x[2]*x[3]/131.078*math.sin(1.48477-x[5])+0.90798*pow(x[2],2)/131.078*math.sin(1.47588)
    g4=abs(g4)-0.0001
    r={}
    r['objectives'] = [f]
    v = []
    v.append(g1)
    v.append(g2)
    v.append(g3)
    v.append(g4)
    r['constraints'] = v
    if ind.get("id") != None:
        r['id'] = ind['id']
    r['valid'] = True
    r['extrainfo'] = {}
    r['extrainfo']['filename'] = None
    r['modifypheno']=0

    
    return r

if __name__ == '__main__':
    x = {}
    x['pheno'] = [201.784467214523659, 99.9999999999999005,
383.071034852773266, 420,10.9076584514292652, 0.0731482312084287128]
   
    print evaluate(x)
