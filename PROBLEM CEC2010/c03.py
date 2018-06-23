#####################################
#
#Last modified: 2018-02-02
#By:            Jiao Ruwang
#
#####################################

# coding: utf-8
import math
import c03_conf
#import protools


moudle          = c03_conf
upper           = moudle.upper
lower           = moudle.lower
prec            = moudle.prec
keys            = moudle.keys
constraints_num = 1
objective_num   = 1
n               = moudle.D
p               = 0.0001

def problem_initialize():
    return n, upper, lower, prec, constraints_num, objective_num

def evaluate(ind):
    x = ind['pheno']
    o = [111.17633500088529,	92.07880492633424,	417.9818592609036,	253.16188128024302,	363.5279986597767,	314.334093889305,	187.32739056163342,	240.4363027535162,	422.60090880560665,	327.63042902581515,	62.04762897064405,	25.435663968682125,	360.56773191905114,	154.9226721156832,	33.161292034425806,	177.8091733067186,	262.58198940407755,	436.9800562237075,	476.6400624069227,	331.2167787340325,	75.205948242522,	484.33624811710115,	258.4696246506982,	419.8919566566751,	357.51468895930395,	166.3771729386268,	47.59455935830133,	188.20606700809785,	184.7964918401363,	267.9201349178807]
    z = []
    for i in xrange(n):
        z.append(x[i] - o[i])
    fsum1 = 0.0
    gsum2 = 0.0
    for i in xrange(n-1):
        fsum1 += 100*(z[i]*z[i] - z[i+1])*(z[i]*z[i] - z[i+1]) + (z[i] - 1)*(z[i] - 1)
        gsum2 += (z[i] - z[i+1])*(z[i] - z[i+1])
    
    f = fsum1
    h = abs(gsum2)-p
    r = {}
    r['objectives'] = [f]
    v = []
    v.append(h)
    r['constraints'] = v
    r["violations"]  = v
    if ind.get("id") != None:#####!!!!
        r['id'] = ind['id']
    r['valid']  = True
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
