'''
Created on 2013-1-22

@author: Administrator
'''
import math
import g09_conf
#import protools

n = 7
moudle=g09_conf
upper=moudle.upper
lower=moudle.lower
prec=moudle.prec
keys=moudle.keys
constraints_num=4
objective_num=1
division = 4
def problem_initialize():
    
    return n,upper,lower,prec,constraints_num,objective_num

def evaluate(ind):
    x= ind['pheno']
    
    f=math.pow(x[0]-10,2)+5*pow(x[1]-12,2)+pow(x[2],4)+3*pow(x[3]-11,2)+10*pow(x[4],6)+7*pow(x[5],2)+pow(x[6],4)-4*x[5]*x[6]-10*x[5]-8*x[6]
    g1=-127+2*pow(x[0],2)+3*pow(x[1],4)+x[2]+4*pow(x[3],2)+5*x[4]
    g2=-282+7*x[0]+3*x[1]+10*pow(x[2],2)+x[3]-x[4]
    g3=-196+23*x[0]+pow(x[1],2)+6*pow(x[5],2)-8*x[6]
    g4=4*pow(x[0],2)+pow(x[1],2)-3*x[0]*x[1]+2*pow(x[2],2)+5*x[5]-11*x[6]
    
    r={}
    r['objectives'] = [f]
    v = []
    v.append(g1 )
    v.append(g2 )
    v.append(g3 )
    v.append(g4 )
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
    x['pheno'] = [2.33049935147405174,1.95137236847114592,-0.477541399510615805, 4.36572624923625874,-0.624486959100388983,1.03813099410962173, 1.5942266780671519]
    #x = [i/10 for i in x]
    print evaluate(x)
