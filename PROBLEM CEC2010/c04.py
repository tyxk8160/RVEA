#####################################
#
#Last modified: 2018-02-02
#By:            Jiao Ruwang
#
#####################################

# coding: utf-8
import math
import c04_conf
#import protools


moudle          = c04_conf
upper           = moudle.upper
lower           = moudle.lower
prec            = moudle.prec
keys            = moudle.keys
constraints_num = 4
objective_num   = 1
n               = moudle.D


def problem_initialize():  
    return n, upper, lower, prec, constraints_num, objective_num

p = 0.0001
def evaluate(ind):
    x = ind['pheno']
    o = [0.820202353727904, 5.260154140335203,	-1.694610371739177,	-5.589298730330406,	-0.141736605495543,	9.454675508078164,	8.795744608532939,	9.687346331423548,	-3.246522827444976,	6.647399971577617,	1.434490229836026,	-0.506531215086801,	0.558594225280784,	7.919942423520642,	1.383716002673571,	-1.520153615528276,	-2.266737465474915,	6.48052999726508,	-8.893207968949003,	-3.528743044935322,	6.063486037065154,	-4.51585211274229,	7.320477892009357,	-8.990263774675665,	9.446412007392851,	-6.41068985463494,	-9.135251626491991,	2.07763837492787,	8.051026378030816,	-1.002691032064544]
    z = []
    for i in xrange(n):
        z.append(x[i] - o[i])
    gsum1 = 0.0
    gsum2 = 0.0
    gsum3 = 0.0
    gsum4 = 0.0
    
    for i in xrange(n):
        gsum1 += z[i]*math.cos(pow(abs(z[i]), 0.5))
        gsum4 += z[i]

    for i in xrange(n/2, n-1):
        gsum3 += (z[i]*z[i] - z[i+1])*(z[i]*z[i] - z[i+1])

    for i in xrange(n/2-2):
        gsum2 += (z[i] - z[i+1])*(z[i] - z[i+1])
    
    f  = max(z)
    h1 = abs(gsum1/n) - p
    h2 = abs(gsum2) -p
    h3 = abs(gsum3) -p
    h4 = abs(gsum4) -p
    r = {}
    r['objectives'] = [f]
    v = []
    v.append(h1 )
    v.append(h2 )
    v.append(h3 )
    v.append(h4 )
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
