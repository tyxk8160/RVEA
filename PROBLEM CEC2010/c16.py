#####################################
#
#Last modified: 2018-02-02
#By:            Jiao Ruwang
#
#####################################

# coding: utf-8
import math
import c16_conf
#import protools


moudle          = c16_conf
upper           = moudle.upper
lower           = moudle.lower
prec            = moudle.prec
keys            = moudle.keys
constraints_num = 4
objective_num   = 1
p               = 0.0001
n               = moudle.D

def problem_initialize():
    return n, upper, lower, prec, constraints_num, objective_num

def evaluate(ind):
    x = ind['pheno']
    o = [0.365972807627352,	0.429881383400138,	-0.420917679577772,	0.984265986788929,	0.324792771198785,	0.463737106835568,	0.989554882052943,	0.307453878359996,	0.625094764380575,	-0.358589007202526,	0.24624504504104,	-0.96149609569083,	-0.184146201911073,	-0.030609388103067,	0.13366054512765,	0.450280168292005,	-0.662063233352676,	0.720384516339946,	0.518473305175091,	-0.969074121149791,	-0.221655317677079,	0.327361832246864,	-0.695097713581401,	-0.671724285177815,	-0.534907819936839,	-0.003991036739113,	0.486452090756303,	-0.689962754053575,	-0.138437260109118,	-0.626943354458217]
    z = []
    for i in xrange(n):
        z.append(x[i] - o[i])
    fsum1 = 0.0
    fsum2 = 1.0
    gsum3 = 0.0
    gsum4 = 1.0
    gsum5 = 0.0
    for i in xrange(n):
        fsum1 += z[i]**2/4000.0
        fsum2 *= math.cos(z[i]/pow((i+1), 0.5))
        gsum3 += z[i]*z[i] - 100.0*math.cos(math.pi*z[i]) + 10.0
        gsum4 *= z[i]
        gsum5 += z[i]*math.sin(pow(abs(z[i]), 0.5))
    
    f = fsum1 - fsum2 + 1.0
    g1 = gsum3
    g2 = gsum4
    h3 = abs(gsum5)  -p
    h4 = abs(-gsum5) -p
    r = {}
    r['objectives'] = [f]
    v = []
    v.append(g1 )
    v.append(g2 )
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
