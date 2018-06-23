#####################################
#
#Last modified: 2018-02-02
#By:            Jiao Ruwang
#
#####################################

# coding: utf-8
import math
import c18_conf
#import protools

moudle          = c18_conf
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
    o = [-2.494401436611803,	-0.306408781638572,	-2.271946840536718,	0.381278325914122,	2.394875929583502,	0.418708663782934,	-2.082663588220074,	0.776060342716238,	-0.374312845903175,	0.352372662321828,	1.172942728375508,	-0.24450210952894,	1.049793874089803,	-1.716285448140795,	-1.026167671845868,	-1.223031642604231,	0.924946651665792,	0.93270056541258,	-2.312880521655027,	-0.671857644927313,	-0.312276658254605,	-0.973986111708943,	-0.454151248193331,	2.420597958989111,	0.050346805172393,	1.050203106200361,	-0.05420584346617,	-0.081533357726523,	-0.968176219532845,	1.682281307624435]
    z = []
    for i in xrange(n):
        z.append(x[i] - o[i])
    fsum1 = 0.0
    gsum2 = 0.0
    gsum3 = 0.0

    for i in xrange(n-1):
        fsum1 += (z[i]*z[i]-z[i+1])**2
    
    for i in xrange(n):
        gsum2 += z[i]*math.sin(pow(abs(z[i]), 0.5))
    
    f  = fsum1
    g1 = -gsum2/n
    h2 = abs(gsum2/n) - p
    r = {}
    r['objectives'] = [f]
    v = []
    v.append(g1 )
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
