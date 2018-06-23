#####################################
#
#Last modified: 2018-02-02
#By:            Jiao Ruwang
#
#####################################

# coding: utf-8
import math
import c13_conf
#import protools

moudle          = c13_conf
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
    o = [69.69311714880897,	1.509803311435702,	67.6746198312362,	80.43173609273597,	80.47622449424348,	51.21092936019716,	52.7723719926014,	17.248465789326257,	52.40150903116374,	39.64846247456716,	89.86375903333635,	32.079301315169474,	43.192499277837946,	70.79294586561508,	1.48440984483988,	19.8566700417119,	29.502667246412756,	34.256788127976684,	12.643016541338264,	78.57234385195876,	26.51647349482587,	97.06430708087798,	10.180504722002471,	82.90799886855778,	63.540231382573154,	74.78243308676124,	87.20817289266436,	50.779655804893764,	43.05412185616204,	33.862234518700916]
    z = []
    for i in xrange(n):
        z.append(x[i] - o[i])
    fsum1 = 0.0
    gsum2 = 0.0
    gsum3 = 0.0
    gsum4 = 0.0
    gsum5 = 1.0
    for i in xrange(n):
        fsum1 += -z[i]*math.sin(pow(abs(z[i]), 0.5))
        gsum2 += z[i]*z[i]
        gsum3 += math.sin(math.pi/50.0*z[i])
        gsum4 +=  z[i]*z[i]/4000.0
        gsum5 *=  math.cos(z[i]/pow((i+1), 0.5))
    
    f  = fsum1/n
    g1 = -50.0 + gsum2/(100.0*n)
    g2 = 50.0*gsum3/n
    g3 = 75.0 - 50.0*(gsum4 - gsum5 + 1.0)
    r = {}
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
