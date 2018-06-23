#####################################
#
#Last modified: 2018-02-02
#By:            Jiao Ruwang
#
#####################################

# coding: utf-8
import math
import c17_conf
#import protools

moudle          = c17_conf
upper           = moudle.upper
lower           = moudle.lower
prec            = moudle.prec
keys            = moudle.keys
constraints_num = 3
objective_num   = 1
p               = 0.0001
n               = moudle.D

def problem_initialize():
    return n, upper, lower, prec, constraints_num, objective_num

def evaluate(ind):
    x = ind['pheno']
    o = [-0.628245703945122,	0.331024455127249,	0.402617203423807,	0.462742527496583,	-0.513329779137884,	0.288191632492259,	0.41479349370103,	0.916196063289011,	-0.427742767473712,	0.811971694633694,	-0.202953396286476,	0.786617208861492,	-0.583805982901842,	0.91666360939369,	-0.602135912772221,	0.503807046950863,	-0.196264987447976, -0.565579687152807,	0.540878947793462,	0.183666358669345,	-0.303576255198908,	-0.896405440407756,	-0.101939801890135,	-0.049819872322279,	0.434240825173134,	0.946552963504364,	-0.32578927683003,	-0.154255792477949,	0.577967633549953,	-0.573697797217518]
    z = []
    for i in xrange(n):
        z.append(x[i] - o[i])
    fsum1 = 0.0
    gsum2 = 1.0
    gsum3 = 0.0
    gsum4 = 0.0
    for i in xrange(n-1):
        fsum1 += (z[i]-z[i+1])**2
    for i in xrange(n):
        gsum2 *= z[i]
        gsum3 += z[i]
        gsum4 += z[i]*math.sin(4.0*pow(abs(z[i]), 0.5))
    
    f  = fsum1
    g1 = gsum2
    g2 = gsum3
    h3 = abs(gsum4) - p
    r = {}
    r['objectives'] = [f]
    v = []
    v.append(g1 )
    v.append(g2 )
    v.append(h3 )
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
