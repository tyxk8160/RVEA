#####################################
#
#Last modified: 2018-02-02
#By:            Jiao Ruwang
#
#####################################

# coding: utf-8
import math
import c14_conf
#import protools


moudle          = c14_conf
upper           = moudle.upper
lower           = moudle.lower
prec            = moudle.prec
keys            = moudle.keys
constraints_num = 3
objective_num   = 1
n               = moudle.D

def problem_initialize():
    return n, upper, lower, prec, constraints_num, objective_num

def evaluate(ind):
    x = ind['pheno']
    o = [-31.718907007204272,	-39.536680684207184, -46.033718058035944,	-42.2004014684422,	-28.331307546159135,	-38.64403177375364,	-11.313371899853626,	-11.717383190039943,	-43.345049558717875, -31.46016185891229,	-35.57742732758397,	-45.49638850141341,	-4.177473725277878,	-26.974808661067083,	-46.30991533784743,	-45.997883193212814,	-29.479673271045964,	-4.336542960830036,	-43.66244285780764,	-22.43896852522004,	-25.89273808052249,	-24.221450510218993,	-30.3952886350567,	-31.170730638052895,	-9.859463575974534,	-16.727846507426452,	-44.35226340706524,	-33.10843069426064,	-7.175153678947718,	-4.601421202670486]
    z = []
    y = []
    for i in xrange(n):
        z.append(x[i] + 1.0 - o[i])
        y.append(x[i] - o[i])
    fsum1 = 0.0
    gsum2 = 0.0
    gsum3 = 0.0
    for i in xrange(n - 1):
        fsum1 += 100.0*(z[i]*z[i] - z[i+1])**2 + (z[i] - 1)**2
    for i in xrange(n):
        gsum2 += y[i]*math.cos(pow(abs(y[i]), 0.5))
        gsum3 += y[i]*math.sin(pow(abs(y[i]), 0.5))
    
    f  = fsum1
    g1 = -gsum2 - n
    g2 = gsum2 - n
    g3 = gsum3 - 10.0*n
    r  = {}
    r['objectives'] = [f]
    v = []
    v.append(g1 )
    v.append(g2 )
    v.append(g3 )
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
