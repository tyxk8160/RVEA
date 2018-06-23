'''
Created on 2013-6-24

@author: Administrator
'''
import math
import g16_conf
#import protools


moudle=g16_conf
upper=moudle.upper
lower=moudle.lower
prec=moudle.prec
keys=moudle.keys
constraints_num=38
objective_num=1

n = 5

def problem_initialize():
    
    return n,upper,lower,prec,constraints_num,objective_num

def evaluate(ind):
    x= ind['pheno']
    
    y1=x[1]+x[2]+41.6
    c1=0.024*x[3]-4.62
    y2=12.5/c1+12
    c2=0.0003535*x[0]*x[0]+0.5311*x[0]+0.08705*y2*x[0]
    c3=0.052*x[0]+78+0.002377*y2*x[0]
    y3=c2/c3
    y4=19*y3
    c4=0.04782*(x[0]-y3)+0.1956*(x[0]-y3)*(x[0]-y3)/x[1]+0.6376*y4+1.594*y3
    c5=100*x[1]
    c6=x[0]-y3-y4
    c7=0.950-c4/c5
    y5=c6*c7
    y6=x[0]-y5-y4-y3
    c8=(y5+y4)*0.995
    y7=c8/y1
    y8=c8/3798
    c9=y7-0.0663*y7/y8-0.3153
    y9=96.82/c9+0.321*y1
    y10=1.29*y5+1.258*y4+2.29*y3+1.71*y6
    y11=1.71*x[0]-0.452*y4+0.580*y3
    c10=12.3/752.3
    c11=(1.75*y2)*(0.995*x[0])
    c12=0.995*y10+1998
    y12=c10*x[0]+c11/c12
    y13=c12-1.75*y2
    y14=3623+64.4*x[1]+58.4*x[2]+146312/(y9+x[4])
    c13=0.995*y10+60.8*x[1]+48*x[3]-0.1121*y14-5095
    y15=y13/c13
    y16=148000-331000*y15+40*y13-61*y15*y13
    c14=2324*y10-28740000*y2
    y17=14130000-1328*y10-531*y11+c14/c12
    c15=y13/y15-y13/0.52
    c16=1.104-0.72*y15
    c17=y9+x[4]
    
    f=0.000117*y14+0.1365+0.00002358*y13+0.000001502*y16+0.0321*y12+0.004324*y5+0.0001*(c15/c16)+37.48*(y2/c12)-0.0000005843*y17
    
    g1=0.28/0.72*y5-y4
    g2=x[2]-1.5*x[1]
    g3=3496*(y2/c12)-21
    g4=110.6+y1-62212/c17
    g5=213.1-y1
    g6=y1-405.23
    g7=17.505-y2
    g8=y2-1053.6667
    g9=11.275-y3
    g10=y3-35.03
    g11=214.2278-y4
    g12=y4-665.585
    g13=7.458-y5
    g14=y5-584.463
    g15=0.961-y6
    g16=y6-265.916
    g17=1.612-y7
    g18=y7-7.046
    g19=0.146-y8
    g20=y8-0.222
    g21=107.99-y9
    g22=y9-273.366
    g23=922.693-y10
    g24=y10-1286.105
    g25=926.832-y11
    g26=y11-1444.046
    g27=18.766-y12
    g28=y12-537.141
    g29=1072.163-y13
    g30=y13-3247.039
    g31=8961.448-y14
    g32=y14-26844.086
    g33=0.063-y15
    g34=y15-0.386
    g35=71084.33-y16
    g36=-140000+y16
    g37=2802713-y17
    g38=y17-12146108
    
    
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
    v.append(g14)
    v.append(g15)
    v.append(g16)
    v.append(g17)
    v.append(g18)
    v.append(g19)
    v.append(g20)
    v.append(g21)
    v.append(g22)
    v.append(g23)
    v.append(g24)
    v.append(g25)
    v.append(g26)
    v.append(g27)
    v.append(g28)
    v.append(g29)
    v.append(g30)
    v.append(g31)
    v.append(g32)
    v.append(g33)
    v.append(g34)
    v.append(g35)
    v.append(g36)
    v.append(g37)
    v.append(g38)
    
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
    x['pheno'] = [705.174537070090537, 68.5999999999999943, 102.899999999999991,282.324931593660324,37.5841164258054832]
    print evaluate(x)
