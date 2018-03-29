import random
import copy
import math
import numpy as np
from collections import defaultdict
def init(popsize,generation,genecount):#gegerating parent population
    global pop
    pop=[]
    for i in range(popsize):
        ind={}
        ind['id']=i
        ind['genes']=[random.uniform(0,1)for j in range(genecount)]
        pop.append(ind)
        pop[i]=evaluate(pop[i])
    return pop
F=0.5
CR=0.9
def offspring_pop(pop,popsize,genecount):#generating offspring population
    global _pop
    _pop=copy.deepcopy(pop)
    for i in range(popsize):
        n=random.sample(range(popsize),3)
        j=random.randint(0,genecount-1)
        for k in range(genecount):
            a=pop[n[0]]['genes'][j]
            b=pop[n[1]]['genes'][j]
            c=pop[n[2]]['genes'][j]
            u=a+(b-c)*F
            if u>1 or u<0:
                u=random.uniform(0,1)
            r=random.random()
            if r<CR or k==genecount:
                _pop[i]['genes'][k]=u
            else:
                _pop[i]['genes'][k]=pop[i]['genes'][k]
        j=(j+1)%genecount
    _pop[i]=evaluate(_pop[i])
    return _pop

def evaluate(ind):#evaluate individuals
    r=ind
    g3=0.0
    x=ind['genes']
    # print(len(x))
    for i in range(len(x)):
        g1=math.cos(20*math.pi*(x[i]-0.5))
        g2=(x[i]-0.5)**2
        g3+=g2
    for i in range(len(x)):
        g1=math.cos(20*math.pi*(x[i]-0.5))
        g=100*(g3-g1)
        f1=0.50*x[0]*x[1]*(1+g)
        f2=0.50*x[0]*(1-x[1])*(1+g)
        f3=0.50*(1-x[0])*(1+g)
    d = defaultdict(list)
    d['objectives'].append(f1)
    d['objectives'].append(f2)
    d['objectives'].append(f3)
    r['objectives']=d['objectives']
    return r
def creat_pop(pop,_pop):
    C=[]
    for i in range(len(pop)):
        C.append(pop[i])
    for i in range(len(_pop)):
        C.append(_pop[i])
    return C