#####################################
#
#Last modified: 2018-02-02
#By:            Jiao Ruwang
#
#####################################

# coding: utf-8
import math
import c01_conf
#import protools


moudle          = c01_conf
upper           = moudle.upper
lower           = moudle.lower
prec            = moudle.prec
keys            = moudle.keys
constraints_num = 2
objective_num   = 1
n               = moudle.D


def problem_initialize():
    return n, upper, lower, prec, constraints_num, objective_num

def evaluate(ind):
    x = ind['pheno']
    o = [0.030858718087483, -0.078632292353156, 0.048651146638038, -0.069089831066354, -0.087918542941928, 0.088982639811141, 0.074143235639847, -0.086527593580149, -0.020616531903907, 0.055586106499231, 0.059285954883598, -0.040671485554685, -0.087399911887693, -0.01842585125741, -0.005184912793062, -0.039892037937026, 0.036509229387458, 0.026046414854433,	-0.067133862936029, 0.082780189144943, -0.049336722577062, 0.018503188080959, 0.051610619131255, 0.018613117768432, 0.093448598181657, -0.071208840780873, -0.036535677894572, -0.03126128526933, 0.099243805247963, 0.053872445945574]
    z = []
    for i in xrange(n):
        z.append(x[i] - o[i])
    fsum1 = 0.0
    fsum2 = 1.0
    fsum3 = 0.0
    gsum4 = 1.0
    gsum5 = 0.0
    for i in xrange(n):
        fsum1 += pow(math.cos(z[i]), 4)
        fsum2 = fsum2*pow(math.cos(z[i]), 2)
        fsum3 += (i+1)*z[i]*z[i]
        gsum4 = gsum4*z[i]
        gsum5 += z[i]
    
    f  = -abs((fsum1 - 2*fsum2)/pow(fsum3, 0.5))
    g1 = 0.75 - gsum4
    g2 = gsum5 - 7.5*n
    
    r  = {}
    r['objectives'] = [f]
    v = []
    v.append(g1 )
    v.append(g2 )
    r['constraints'] = v
    r["violations"]  = v
    if ind.get("id") != None:#####!!!!
        r['id'] = ind['id']
    r['valid'] = True
    r['extrainfo'] = {}
    r['extrainfo']['filename'] = None
    r['modifypheno']=0
    
    return r


if __name__ == '__main__':
    x={}
    x['pheno'] = [3.16246061572185,3.12833142812967,3.09479212988791,3.06145059523469,3.02792915885555,
         2.99382606701730,2.95866871765285,2.92184227312450,0.49482511456933,0.48835711005490,
         0.48231642711865,0.47664475092742,0.47129550835493,0.46623099264167,0.46142004984199,
         0.45683664767217,0.45245876903267,0.44826762241853,0.44424700958760,0.44038285956317]
    print evaluate(x)
