import DCNSGA_II_DE_conf
import math
import random
import copy
import sys

def initialize_parent_population(size, genecount): #create the initial parent popluation with given size 
    pop = []
    for i in range(size):
        ind = {}
        ind['extrainfo']={}
        ind['genes'] = [random.random() for j in range(genecount)] # every genes is created in boundary [0,1] 
        ind['extrainfo']['generation']=0
        pop.append(ind)
    return pop

def caculate_pheno(pop , upper, lower, n, size):
    for k in xrange(size):
        pop[k]['pheno'] = []
        for i in xrange(n):
            t = pop[k]["genes"][i] * (upper[i] - lower[i]) + lower[i]
            pop[k]['pheno'].append(t)

def evaluate_population(pop, evaluator, fill_result): #evaluate the pop 
    results = []
    for i in range(len(pop)):
        pop[i]['id'] = i
        results.append(evaluator(pop[i]))
    fill_result(pop, results)
    evaluationTime = len(pop)
    return evaluationTime

def get_fill_result(inds, rsts):  #put the informations of evaluate rusults into the _pop 
    mark = {}
    for rst in rsts:
        i = rst['id']
        ind = inds[i]      
        ind['objectives'] =rst['objectives']
        ind['violations']=[]
        for n in range(len(rst['constraints'])):
            if rst['constraints'][n] >0:
                ind['violations'].append(rst['constraints'][n])
            else:
                ind['violations'].append(0)
        ind['extrainfo']['filename'] = rst['extrainfo']['filename']
        ind['extrainfo']['constraints'] = rst['constraints']

def caculate_initial_max_violation(rsts): #this is used for getting the max violations in first generation
    #if maxG(i)<1,i=1,2,...,m,then set the maxG(i)=1.
    # algorithm initialize the value of maxG(i)=1
    # if there are some values >1,replace the maxG with the larger vlaue
    maxG = [1 for i in range(len(rsts[0]['violations']))]
    for rst in rsts:
        for k in range(len(rsts[0]['violations'])):
            if cmp(rst['violations'][k], maxG[k]) == 1:
                #if rst['violations'][k]<1e+8:    # delete sepeter 6,2016, by Zeng Sanyou ,Jiao Ruwang
                maxG[k] = rst['violations'][k]
    return maxG

def caculate_violation_objective(maxG, rsts):  #uesing the violations to get the violation_objective
    #violation_objective=1/m*sum(G(i)/maxG(i))  i=1,2,...,m
    m = len(rsts[0]['violations'])    
    for i in range(len(rsts)):
        vObj = 0.0
        for h in range(m):
            tmp = rsts[i]['violations'][h]/float(maxG[h])
            vObj += tmp
        rsts[i]['violation_objectives'] = []
        rsts[i]['violation_objectives'].append(vObj/m)

def mark_individual_efeasible(e, pop):   #test whether the pop[i] is e_feasible
    # boundary is vector e=(e1,e2,...,em),if vector G(x)<= vector e ,the indivial is  efeasible ,
    # then set the falg "test" is 1
    for i in xrange(len(pop)):
        test = 1
        for j in xrange(len(e)):
            if pop[i]['violations'][j] > e[j]:
                test = 0
                break
        pop[i]['efeasible'] = test

def judge_population_efeasible(tmp):   #judge whether the environment K will change
    # if the whole population is efeasible,the Flag set 1 ,otherwise 0.
    Flag = 1
    for i in range(len(tmp)):
        if tmp[i]['efeasible'] == 0:
            Flag = 0
            break
    return Flag

z = 1.0e-08
Nearzero = 1.0e-15

def reduce_boundary(eF, k, MaxK):    # Modified by JRW, 2018/03/02
    _e = []
    for i in range(len(eF)):
        temp = math.sqrt(math.log((eF[i]+z)/z, math.e))
        B = float(MaxK) / temp
        if B == 0.0:
            B = Nearzero
        A = eF[i] + z
        f = A * math.pow( math.e, -math.pow( float(k)/B, 2 ) ) - z
        if abs(f-z) < Nearzero:
            f = z
        if abs(f) < Nearzero:
            f = 0.0
        _e.append(f)
    return _e

'''def reduce_boundary(eF, k, MaxK):    #get the e_feasible elastic boundary
    _e = []
    for i in range(len(eF)):
        #c = math.sqrt(math.log(eF[i]/z, math.e))
        temp = math.sqrt(math.log((eF[i])/z, math.e))
        B = float(MaxK) / temp
        if B == 0.0:
            B = Nearzero
        A = eF[i]
        f = A * math.pow( math.e, -math.pow( float(k)/B, 2 ) )
        if abs(f-z) < Nearzero:
            f = z
        if abs(f) < Nearzero:
            f = 0.0
        _e.append(f)
    return _e'''

CR = DCNSGA_II_DE_conf.CR
Pm = DCNSGA_II_DE_conf.Pm
def generate_offspring_population(n, _size, _tmp, _genCount):   #create the offsprings
        S = []
        random.shuffle(_tmp)
        for i in range(_size):
            #offspring = []
            Tmp = []
            
            for v in range(_size):
                Tmp.append(_tmp[v]['genes'])
            offspring = create_offspring(i, Tmp, _size, _genCount)
            for k in range(_genCount):
                r = random.random()
                if r > CR:
                    offspring['genes'][k] = _tmp[i]['genes'][k]          
            for k in range(_genCount):
                r = random.random()
                if r <= Pm:
                    offspring['genes'][k] = random.random()
            offspring['extrainfo'] = {}
            offspring['extrainfo']['generation'] = n+1
            S.append(offspring)
        return S
                              
def create_offspring(n, ind, popSize, genCount):
    #vi=pa+F(pb-pc)  pa,pb,pc is random selected from the parents population 
    M = 3
    select = []
    for i in xrange(M):
        index_ind = (n + i + 1)%popSize        
        select.append(ind[index_ind])
    F = random.uniform(0,1)

    offspring = {}
    offspring['genes'] = []
    offgenes = []
    flag = 1
    #make sure the value of genes in the bound [0,1]
    '''for i in xrange(genCount):
        temp = select[0][i]+F*(select[1][i]-select[2][i])
        if temp >1 or temp<0:
            flag = 0
            break
        else:
            offgenes.append(temp)
    if flag == 0:
        _offgenes = repair(select, genCount, F)
        offspring['genes'].extend(_offgenes)
    else:
        offspring['genes'].extend(offgenes)'''
    for i in xrange(genCount):
        temp = select[0][i]+F*(select[1][i]-select[2][i])
        if temp >1 :
            temp = 1.0 - (temp - int(temp))
        if temp<0:
            temp = int(temp) - temp
        offspring['genes'].append(temp)
    return offspring
                  
def repair(select, genCount, befF):                                                
    Flist = [befF]
    for i in xrange(genCount):
        if (select[2][i]-select[1][i]) == 0:
            Flist.append(befF)
        else:
            F1 = (1- select[0][i])/(select[2][i]-select[1][i])                                              
            F2 = (0- select[0][i])/(select[2][i]-select[1][i])
            if F1 >= 0:
                Flist.append(F1)
            else:
                Flist.append(F2)
    F = min(Flist)    
    offgenes = []
    for i in xrange(genCount):
        temp = select[0][i]+F*(select[2][i]-select[1][i])
        if temp < 0.0:
            temp = 0.0
        elif temp > 1.0:
            temp = 1.0
        offgenes.append(temp)
    return offgenes
