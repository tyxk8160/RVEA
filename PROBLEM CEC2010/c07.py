#####################################
#
#Last modified: 2018-02-02
#By:            Jiao Ruwang
#
#####################################

# coding: utf-8
import math
import c07_conf
#import protools


moudle          = c07_conf
upper           = moudle.upper
lower           = moudle.lower
prec            = moudle.prec
keys            = moudle.keys
constraints_num = 1
objective_num   = 1
n               = moudle.D

def problem_initialize():
    return n, upper, lower, prec, constraints_num, objective_num

def evaluate(ind):
    x = ind['pheno']
    o = [-1.46823271282738,	47.51401860909492,	-30.421056514069576,	-7.707941671844303,	-21.74698421666629,	-17.88116387879569,	5.274442455807971,	18.71403753778708,	-36.959734507345146,	-20.72950462154263,	25.4701966548936,	-25.439992885801573,	1.054563129830697,	-31.556579857545657,	-19.320382777005047,	17.16774285348282,	34.66536814401755,	-31.803705714749462,	-12.926898387712775,	25.489686517508602,	-45.23000430753644,	36.31774710581284,	-18.38690515559357,	34.86816378160691,	-37.530671214167334,	19.288852618585977,	0.684612418754519,	-12.636795982748637,	15.005454148879409,	-40.468678588994315]
    z = []
    y = []
    for i in xrange(n):
        z.append(x[i] + 1 - o[i])
        y.append(x[i] - o[i])
    fsum1 = 0.0
    gsum2 = 0.0
    gsum3 = 0.0
    for i in xrange(n-1):
        fsum1 += 100*pow((z[i]*z[i] - z[i+1]), 2) + (z[i]-1)**2
    for i in xrange(n):
        gsum2 += y[i]*y[i]
        gsum3 += math.cos(0.1*y[i])
    
        
    
    f = fsum1
    g1 = 0.5 - pow(math.e, (-0.1)*pow(gsum2/n, 0.5)) - 3*pow(math.e, gsum3/n) + pow(math.e, 1)
    r = {}
    r['objectives'] = [f]
    v = []
    v.append(g1 )
    r['constraints'] = v
    r["violations"] = v
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
