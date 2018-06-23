import math
import g14_conf
#import protools


moudle=g14_conf
upper=moudle.upper
lower=moudle.lower
prec=moudle.prec
keys=moudle.keys
constraints_num=3
objective_num=1

division =6
n = 10

def problem_initialize():
    
    return n,upper,lower,prec,constraints_num,objective_num

def evaluate(ind):
    x = ind['pheno']
   
    c=[-6.089,-17.164,-34.054,-5.914,-24.721,-14.986,-24.1,-10.708,-26.662,-22.179]
    sumx=0
    for j in range(10):
       sumx=sumx+x[j]
    f=0
    for i in range(10):
       f=f+x[i]*(c[i]+math.log(x[i]/sumx))   
    g1=x[0]+2*x[1]+2*x[2]+x[5]+x[9]-2
    g1=abs(g1)-0.0001
    g2=x[3]+2*x[4]+x[5]+x[6]-1
    g2=abs(g2)-0.0001
    g3=x[2]+x[6]+x[7]+2*x[8]+x[9]-1
    g3=abs(g3)-0.0001
    r={}
    r['objectives'] = [f]
    v = []
    v.append(g1)
    v.append(g2)
    v.append(g3)
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
    x['pheno'] = [0.0406684113216282, 0.147721240492452, 0.783205732104114,0.00141433931889084, 0.485293636780388, 0.000693183051556082, 0.0274052040687766,
0.0179509660214818, 0.0373268186859717, 0.0968844604336845]
    
    print evaluate(x)
