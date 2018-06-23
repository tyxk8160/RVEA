#####################################
#
#Last modified: 2018-02-02
#By:            Jiao Ruwang
#
#####################################

# coding: utf-8
import math
import c05_conf
#import protools


moudle          = c05_conf
upper           = moudle.upper
lower           = moudle.lower
prec            = moudle.prec
keys            = moudle.keys
constraints_num = 2
objective_num   = 1
p               = 0.0001
n               = moudle.D

def problem_initialize():
    return n, upper, lower, prec, constraints_num, objective_num

def evaluate(ind):
    x = ind['pheno']
    o = [72.10900225247575,	9.007673762322495,	51.86632637302316,	41.365704820161,	93.18768763916974,	74.53341902482204,	63.745479932407655,	7.496986033468282,	56.16729598807964,	17.71630810614085,	28.009655663065143,	29.36357615570272,	26.966653374740996,	6.892189514516317,	44.29071160734624,	84.35803966449319,	81.16906730972529,	92.76919270133271,	3.826058034047476,	7.231864548985054,	14.446069444832405,	46.49943418775763,	22.155722253817412,	69.11723738661682,	88.99628570349459,	58.74823912291344,	52.265369214509846,	47.030120955005074,	53.23321779503931,	5.778976086909701]
    z = []
    for i in xrange(n):
        z.append(x[i] - o[i])
    hsum1 = 0.0
    hsum2 = 0.0
    
    for i in xrange(n):
        hsum1 += -z[i]*math.sin(pow(abs(z[i]), 0.5))
        hsum2 += -z[i]*math.cos(0.5*pow(abs(z[i]), 0.5))
        
    
    f  = max(z)
    h1 = abs(hsum1/n) - p
    h2 = abs(hsum2/n) - p
    r = {}
    r['objectives'] = [f]
    v = []
    v.append(h1 )
    v.append(h2 )
    r['constraints'] = v
    r["violations"]  = v
    if ind.get("id") != None:#####!!!!
        r['id'] = ind['id']
    r['valid'] = True
    r['extrainfo'] = {}
    r['extrainfo']['filename'] = None
    r['modifypheno'] = 0
    return r

if __name__ == '__main__':
    x = {}
    x['pheno'] = [3.16246061572185,3.12833142812967,3.09479212988791,3.06145059523469,3.02792915885555,
         2.99382606701730,2.95866871765285,2.92184227312450,0.49482511456933,0.48835711005490,
         0.48231642711865,0.47664475092742,0.47129550835493,0.46623099264167,0.46142004984199,
         0.45683664767217,0.45245876903267,0.44826762241853,0.44424700958760,0.44038285956317]
    print evaluate(x)
