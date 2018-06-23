'''
Created on 2013-6-24

@author: Administrator
'''
import math
import g22_conf
#import protools


moudle=g22_conf
upper=moudle.upper
lower=moudle.lower
prec=moudle.prec
keys=moudle.keys
constraints_num=20
objective_num=1

n = 22

def problem_initialize():
    
    return n,upper,lower,prec,constraints_num,objective_num

def evaluate(ind):
    x= ind['pheno']
    
    f=x[0]
    
    #g1=-x[0]+pow(x[1],0.6)
    g1=-x[0]+pow(x[1],0.6)+pow(x[2],0.6)+pow(x[3],0.6)
    g2=x[4]-100000*x[7]+1e+7
    g2=abs(g2)-0.0001
    g3=x[5]+100000*x[7]-100000*x[8]
    g3=abs(g3)-0.0001
    g4=x[6]+100000*x[8]-5e+7
    g4=abs(g4)-0.0001
    g5=x[4]+100000*x[9]-3.3e+7
    g5=abs(g5)-0.0001
    g6=x[5]+100000*x[10]-4.4e+7
    g6=abs(g6)-0.0001
    g7=x[6]+100000*x[11]-6.6e+7
    g7=abs(g7)-0.0001
    g8=x[4]-120*x[1]*x[12]
    g8=abs(g8)-0.0001
    g9=x[5]-80*x[2]*x[13]
    g9=abs(g9)-0.0001
    g10=x[6]-40*x[3]*x[14]
    g10=abs(g10)-0.0001
    g11=x[7]-x[10]+x[15]
    g11=abs(g11)-0.0001
    g12=x[8]-x[11]+x[16]
    g12=abs(g12)-0.0001
    g13=-x[17]+math.log(x[9]-100)
    g13=abs(g13)-0.0001
    g14=-x[18]+math.log(-x[7]+300)
    g14=abs(g14)-0.0001
    g15=-x[19]+math.log(x[15])
    g15=abs(g15)-0.0001
    g16=-x[20]+math.log(-x[8]+400)
    g16=abs(g16)-0.0001
    g17=-x[21]+math.log(x[16])
    g17=abs(g17)-0.0001
    g18=-x[7]-x[9]+x[12]*x[17]-x[12]*x[18]+400
    g18=abs(g18)-0.0001
    g19=x[7]-x[8]-x[10]+x[13]*x[19]-x[13]*x[20]+400
    g19=abs(g19)-0.0001
    g20=x[8]-x[11]-4.60517*x[14]+x[14]*x[21]+100
    g20=abs(g20)-0.0001
    
    
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
    v.append(g9 )
    v.append(g10 )
    v.append(g11 )
    v.append(g12 )
    v.append(g13 )
    v.append(g14 )
    v.append(g15 )
    v.append(g16 )
    v.append(g17 )
    v.append(g18 )
    v.append(g19 )
    v.append(g20 )
   
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
    x['pheno'] =[236.430975504001054, 135.82847151732463, 204.818152544824585, 6446.54654059436416,
3007540.83940215595, 4074188.65771341929, 32918270.5028952882, 130.075408394314167,
170.817294970528621, 299.924591605478554, 399.258113423595205, 330.817294971142758,
184.51831230897065, 248.64670239647424, 127.658546694545862, 269.182627528746707,
160.000016724090955, 5.29788288102680571, 5.13529735903945728, 5.59531526444068827,
5.43444479314453499, 5.07517453535834395]

    print evaluate(x)
