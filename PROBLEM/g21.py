import math
import g21_conf
#import protools


moudle=g21_conf
upper=moudle.upper
lower=moudle.lower
prec=moudle.prec
keys=moudle.keys
constraints_num=6
objective_num=1


n = 7

def problem_initialize():
    
    return n,upper,lower,prec,constraints_num,objective_num

def evaluate(ind):
    x= ind['pheno']
    
    f=x[0]   
    g1=-x[0]+35*pow(x[1],0.6)+35*pow(x[2],0.6)
    g2=-300*x[2]+7500*x[4]-7500*x[5]-25*x[3]*x[4]+25*x[3]*x[5]+x[2]*x[3]
    g2=abs(g2)-0.0001
    g3=100*x[1]+155.365*x[3]+2500*x[6]-x[1]*x[3]-25*x[3]*x[6]-15536.5
    g3=abs(g3)-0.0001
    g4=-x[4]+math.log(-x[3]+900)
    g4=abs(g4)-0.0001
    g5=-x[5]+math.log(x[3]+300)
    g5=abs(g5)-0.0001
    g6=-x[6]+math.log(-2*x[3]+700)
    g6=abs(g6)-0.0001
    r={}
    r['objectives'] = [f]
    v = []
    v.append(g1)
    v.append(g2)
    v.append(g3)
    v.append(g4)
    v.append(g5)
    v.append(g6)
    
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
    x['pheno'] = [193.724510070034967, 5.56944131553368433e-27, 17.3191887294084914, 100.047897801386839, 6.68445185362377892, 5.99168428444264833,
6.21451648886070451]
    
    print evaluate(x)
