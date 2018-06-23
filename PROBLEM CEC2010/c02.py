#####################################
#
#Last modified: 2018-02-02
#By:            Jiao Ruwang
#
#####################################

# coding: utf-8
import math
import c02_conf
#import protools


moudle          = c02_conf
upper           = moudle.upper
lower           = moudle.lower
prec            = moudle.prec
keys            = moudle.keys
constraints_num = 3
objective_num   = 1
n               = moudle.D
p               = 0.0001


def problem_initialize():  
    return n, upper, lower, prec, constraints_num, objective_num

def evaluate(ind):
    x = ind['pheno']
    o = [-0.066939099286697,	0.470966419894494,	-0.490528349401176,	-0.312203454689423,	-0.124759576300523,	-0.247823908806285,	-0.448077079941866,	0.326494954650117,	0.493435908752668,	0.061699778818925,	-0.30251101183711,	-0.274045146932175,	-0.432969960330318,	0.062239193145781,	-0.188163731545079,	-0.100709842052095,	-0.333528971180922,	-0.496627672944882,	-0.288650116941944,	0.435648113198148,	-0.348261107144255,	0.456550427329479,	-0.286843419772511,	0.145639015401174,	-0.038656025783381,	0.333291935226012,	-0.293687524888766,	-0.347859473554797,	-0.089300971656411,	0.142027393193559]
    z = []
    y = []
    for i in xrange(n):
        z.append(x[i] - o[i])
        y.append(x[i] - o[i] - 0.5)
    f = max(z)
    gsum1 = 0.0
    gsum2 = 0.0
    for i in xrange(n):
        gsum1 += z[i]*z[i] - 10*math.cos(2*math.pi*z[i]) + 10
        gsum2 += y[i]*y[i] - 10*math.cos(2*math.pi*y[i]) + 10
    g1 = 10 - gsum1/n
    g2 = gsum1/n - 15
    h1 = gsum2/n - 20
    h1  = abs(h1)-p
    r={}
    r['objectives'] = [f]
    v = []
    v.append(g1 )
    v.append(g2 )
    v.append(h1 )
    r['constraints'] = v
    r["violations"]  = v
    if ind.get("id") != None:#####!!!!
        r['id'] = ind['id']
    r['valid']     = True
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
