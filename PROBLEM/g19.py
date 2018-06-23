import math
import g19_conf
#import protools


moudle=g19_conf
upper=moudle.upper
lower=moudle.lower
prec=moudle.prec
keys=moudle.keys
constraints_num=5
objective_num=1
division = 3
n = 15

def problem_initialize():
    
    return n,upper,lower,prec,constraints_num,objective_num

def evaluate(ind):
    x= ind['pheno']
    
    b=[-40,-2,-0.25,-4,-4,-1,-40,-60,5,1]
    e=[-15,-27,-36,-18,-12]
    c=[[30,-20,-10,32,-10],[-20,39,-6,-31,32],[-10,-6,10,-6,-10],[32,-31,-6,39,-20],[-10,32,-10,-20,30]]
    d=[4,8,10,6,2]
    a=[]
    a.append([-16,2,0,1,0])
    a.append([0,-2,0,0.4,2])
    a.append([-3.5,0,2,0,0])
    a.append([0,-2,0,-4,-1])
    a.append([0,-9,-2,1,-2.8])
    a.append([2,0,-4,0,0])
    a.append([-1,-1,-1,-1,-1])
    a.append([-1,-2,-3,-2,-1])
    a.append([1,2,3,4,5])
    a.append([1,1,1,1,1])
    sumx=0
    for j in range(5):
        tmp=0
        for i in range(5):
           tmp=tmp+c[i][j]*x[10+i]*x[10+j]
        sumx=sumx+tmp
    tmp1=0
    for j in range(5):
        tmp1=tmp1+d[j]*pow(x[10+j],3)
    tmp2=0
    for i in range(10):
        tmp2=tmp2+b[i]*x[i]
    
    f=sumx+2*tmp1-tmp2
    g=[]
    for j in range(5):
        tmp3=0
        tmp4=0
        for i in range(5):
            tmp3=tmp3+c[i][j]*x[10+i]
        for i in range(10):
            tmp4=tmp4+a[i][j]*x[i]
        _g=-2*tmp3-3*d[j]*pow(x[10+j],2)-e[j]+tmp4
        g.append(_g)
    g1=g[0]
    g2=g[1]
    g3=g[2]
    g4=g[3]
    g5=g[4]
    r={}
    r['objectives'] = [f]
    v = []
    v.append(g1)
    v.append(g2)
    v.append(g3)
    v.append(g4)
    v.append(g5)
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
    x['pheno'] = [1.66991341326291344e-17, 3.95378229282456509e-16, 3.94599045143233784, 1.06036597479721211e-16, 3.2831773458454161,
9.99999999999999822, 1.12829414671605333e-17, 1.2026194599794709e-17, 2.50706276000769697e-15, 2.24624122987970677e-15, 0.370764847417013987, 0.278456024942955571, 0.523838487672241171,
0.388620152510322781, 0.298156764974678579]
    
    print evaluate(x)
