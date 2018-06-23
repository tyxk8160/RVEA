'''
Created on 2013-1-20

@author: Administrator
'''
import math
import g08_conf
#import protools

upper=g08_conf.upper
lower=g08_conf.lower
prec=g08_conf.prec
keys=g08_conf.keys
constraints_num=2
objective_num=1
division = 12
n = 2
def problem_initialize():
    
    return n,upper,lower,prec,constraints_num,objective_num

def evaluate(ind):
    x= ind['pheno']
    f1=math.pow(math.sin(2*math.pi*x[0]),3)*math.sin(2*math.pi*x[1])
    f=(-1)*(f1/((x[0]+x[1])*math.pow(x[0], 3)))
    g1=x[0]*x[0]-x[1]+1
    g2=1-x[0]+(x[1]-4)*(x[1]-4)
    r={}
    r['objectives'] = [f]
    v = []
    v.append(g1 )
    v.append(g2 )
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
    x['pheno'] = [1.22797135260752599, 4.24537336612274885]
    x['pheno'] = [i/10 for i in x['pheno']]
    print evaluate(x)
