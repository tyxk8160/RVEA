#####################################
#
#Last modified: 2018-02-02
#By:            Jiao Ruwang
#
#####################################

# coding: utf-8
import math
import c09_conf
#import protools


moudle          = c09_conf
upper           = moudle.upper
lower           = moudle.lower
prec            = moudle.prec
keys            = moudle.keys
constraints_num = 1
objective_num   = 1
p               = 0.0001
n               = moudle.D


def problem_initialize(): 
    return n, upper, lower, prec, constraints_num, objective_num

def evaluate(ind):
    x = ind['pheno']
    o = [-41.03250252873486,	-35.70280591875908,	-48.66938576680659,	94.51946988004894,	31.68700466174738,	99.69508270219342,	30.778279925351967,	-31.041222172110807,	-46.21010370947247,	27.26190010072706,	-2.093622677920422,	22.246274570582585,	-42.887366421312436,	89.88377145577851,	-6.731523713182725,	97.86439204258224,	49.49993772881544,	23.210695390854696,	-81.36716857155828,	-20.15688556597543,	36.692155371634726,	44.37408948075327,	-15.984549833405907,	-49.68391424581281,	98.3715576810595,	0.127593155843627,	61.709914317965655,	-84.0189999580673,	-35.39565398431638,	-5.143979333218638]
    z = []
    y = []
    for i in xrange(n):
        y.append(x[i] - o[i])
        z.append(x[i] + 1.0 - o[i])
    fsum1 = 0.0
    hsum2 = 0.0
    
    for i in xrange(n-1):
        fsum1 += 100*pow((z[i]*z[i] - z[i+1]) ,2) + (z[i] - 1)*(z[i] - 1)
    for i in xrange(n):
        hsum2 += y[i]*math.sin(pow(abs(y[i]), 0.5))
    
    f  = fsum1
    h1 = abs(hsum2) - p
    r = {}
    r['objectives'] = [f]
    v = []
    v.append(h1 )
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
