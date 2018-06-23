#####################################
#
#Last modified: 2018-02-02
#By:            Jiao Ruwang
#
#####################################

# coding: utf-8
import math
import c12_conf
#import protools


moudle          = c12_conf
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
    o = [18.889635068428205,	-59.265426383246485,	33.25998466165768,	20.152694275194037,	-10.734106238462502,	-90.85053128520764,	-12.073899411249897,	59.72307696259165,	-37.44193247323578,	25.963111555782035,	6.251460324561279,	41.478172862575434,	86.54258849813075,	34.94822787072172,	26.864471649916382,	79.55580868986908,	-44.66218241775459,	-7.305741544994362,	87.75843366209835,	33.836473236958284,	84.53385936725138,	80.89850629751817,	48.46967726645195,	-82.0758049330533,	-98.54273249151939,	19.55069746505636,	8.33657824668768,	88.54888769408086,	-79.08282398956031,	63.254014133387614]
    z = []
    for i in xrange(n):
        z.append(x[i] - o[i])
    fsum1 = 0.0
    hsum2 = 0.0
    gsum3 = 0.0
    
    for i in xrange(n):
        fsum1 += z[i]*math.sin(pow(abs(z[i]), 0.5))
        gsum3 += z[i] - 100.0*math.cos(0.1*z[i]) + 10.0
    for i in xrange(n - 1):
        hsum2 += (z[i]*z[i] - z[i+1])*(z[i]*z[i] - z[i+1])
    
    f  = fsum1
    h1 = abs(hsum2) - p
    g2 = gsum3
    r = {}
    r['objectives'] = [f]
    v = []
    v.append(h1 )
    v.append(g2 )
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
