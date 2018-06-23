# -*- coding: utf-8 -*-
import random
import math   

z = 1.0e-8
Nearzero = 1.0e-15


def get_MaxR(dimension, pointAmount, upper, lower):
    production = 1.0
    difference = [0.0 for ii in range(dimension)]
    for i in range(dimension):
        difference[i] = upper[i]-lower[i]
        production *= difference[i]
    production *= 2*dimension
    R = 0.5 * pow(production/(pointAmount * math.pi), 1.0/dimension)
    return R

def reduce_radius(k, MaxK, genecount, R, upper, lower):  # Modified by JRW, 2018/03/02
    production = 1.0
    for i in xrange(genecount):
        production *= (upper[i] - lower[i])
    z1 = z/( production**(1.0/genecount) )
    C = R + z1
    c = math.sqrt(abs(math.log(C/z1, math.e)))
    D = float(MaxK)/c
    q = float(k)/D
    f = C * math.pow(math.e, -math.pow(q, 2)) - z1
    if abs(f) < Nearzero:
        f = 0.0
    return f

'''def reduce_radius(k, MaxK, genecount, R, upper, lower):
    production = 1.0
    for i in xrange(genecount):
        production *= (upper[i] - lower[i])
    z1 = z/( production**(1.0/genecount) )
    #R=get_MaxR(gencount,size,pop)
    C = R
    c = math.sqrt(abs(math.log(C/z1, math.e)))
    D = float(MaxK)/c
    q = float(k)/D
    f = C * math.pow(math.e, -math.pow(q, 2))
    if abs(f-z)<Nearzero:
        f=z
    if abs(f) < Nearzero:
        f = 0.0
    return f'''


def caculate_nichecount(_pop, _S, _genCount, r, size):#密度目标
    sum_pop = []
    sum_pop.extend(_pop)
    sum_pop.extend(_S)
    nonZero = 0
    nicheCount = [0.0 for x in range(size)]
    for i in range(size):
        for j in range (i+1, size):
            sum1 = 0.0
            for k in range(_genCount):
                difference = sum_pop[i]['genes'][k] - sum_pop[j]['genes'][k]  #X1i-X2i
                sum1 += (difference*difference)
            aDist = math.sqrt(sum1)
            if(aDist < r):
                shareF = 1 - (aDist/r)
                nicheCount[i] += shareF
                nicheCount[j] += shareF

        if nicheCount[i] != 0.0:
            nonZero +=1
        if len(sum_pop[i]['violation_objectives']) == 2:
            sum_pop[i]['violation_objectives'][1] = nicheCount[i]
        elif len(sum_pop[i]['violation_objectives']) == 1:
            sum_pop[i]['violation_objectives'].append(nicheCount[i])
        else :
            print "wrong"
    #print "nonzero", nonZero
