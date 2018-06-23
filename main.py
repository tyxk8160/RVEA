####################################################
# Note: This is 3-objective version of NSGA-II
# Last modified: 2018-02-03
# By: Jiao Ruwang    ruwangjiao@gmail.com
####################################################

# -*- coding: utf-8 -*-
import DCNSGA_II_DE_tools
import DCNSGA_II_DE_conf
import dyanmic_tools
import copy
import os
import nichec
import sys
from RVEA_tools import RVEA
#import numpy as np
#import matplotlib.pyplot as plt

WORKING_DIR  = os.getcwd()
PROBLEM_DIR = WORKING_DIR + r"/PROBLEM CEC2010"
PROBLEM_DIR2 = WORKING_DIR +r"/PROBLEM"
RESULT_DIR = WORKING_DIR + r"/RESULT"
LOCAL_PATH = [WORKING_DIR, PROBLEM_DIR,PROBLEM_DIR2, RESULT_DIR]
sys.path.extend(LOCAL_PATH)

def init(popSize,  problem_initialize, evaluator):
    global parent_size, offspring_size,  _genCount, _evaluator, parent_pop, upper, lower, constraints_num, objectives_number, evaluationTime
    parent_size, offspring_size, _genCount, _evaluator, upper, lower = popSize, popSize, problem_initialize[0], evaluator, problem_initialize[1], problem_initialize[2]
    constraints_num, objectives_number = problem_initialize[4], problem_initialize[5]
    if constraints_num == 0:
        # constraints_num = 1    # delete Setepeter 6,2016, by Zeng Sanyou , Jiao Ruwang
        exit(0)                  # add ,Setepeter 6,2016, by Zeng Sanyou , Jiao Ruwang
    parent_pop = dyanmic_tools.initialize_parent_population(parent_size, _genCount)
    dyanmic_tools.caculate_pheno(parent_pop, upper, lower, _genCount, parent_size)
    evaluationTime = 0
    evaluationTime += dyanmic_tools.evaluate_population(parent_pop, _evaluator, dyanmic_tools.get_fill_result)  

def loop(generation, outputfreq, condition,rvea):
    global parent_pop, evaluationTime
    global parent_size,offspring_size
    initialMaxViolation = dyanmic_tools.caculate_initial_max_violation(parent_pop)
    e = initialMaxViolation
    dyanmic_tools.caculate_violation_objective(initialMaxViolation, parent_pop)
    dyanmic_tools.mark_individual_efeasible(e, parent_pop)
    K = 0
    g = 0
    MaxK = DCNSGA_II_DE_conf.MaxK
    normalized_upper = [1.0] * _genCount
    normalized_lower = [0.0] * _genCount
    R = nichec.get_MaxR(_genCount, parent_size + offspring_size, normalized_upper, normalized_lower)    # modify, Setepeter 6,2016, by Zeng Sanyou , Jiao Ruwang
    while K <= MaxK:
        print "g:",g," K:",K
        bool_efeasible = dyanmic_tools.judge_population_efeasible(parent_pop)
        if bool_efeasible == 1 :
            K += 1
            
            if K >= MaxK+1:
                break
            e = dyanmic_tools.reduce_boundary(initialMaxViolation, K, MaxK)
            r = nichec.reduce_radius(K, MaxK, _genCount, R, upper, lower)
            dyanmic_tools.mark_individual_efeasible(e, parent_pop)

                
              
        offspring_pop = dyanmic_tools.generate_offspring_population(g, offspring_size, parent_pop, _genCount)
        dyanmic_tools.caculate_pheno(offspring_pop, upper, lower, _genCount, offspring_size)
        evaluationTime += dyanmic_tools.evaluate_population(offspring_pop, _evaluator, dyanmic_tools.get_fill_result)
        dyanmic_tools.caculate_violation_objective(initialMaxViolation, offspring_pop)
        dyanmic_tools.mark_individual_efeasible(e, offspring_pop)
        nichec.caculate_nichecount(parent_pop, offspring_pop, _genCount, r, parent_size + offspring_size)
        #
        # x = [pop_tmp['violation_objectives'] for pop_tmp in parent_pop]
        # print x
        # parent_pop = DCNSGA_II_DE_tools.select_next_parent_population(offspring_pop, parent_pop, parent_size)
        parent_pop,parent_size = rvea.select(offspring_pop, parent_pop, parent_size)
        offspring_size = parent_size
        if g == generation:
            break
        else:
           g += 1

    #nondominated = DCNSGA_II_DE_tools.fast_non_dominated_sort(parent_pop, len(parent_pop))
    #bestObj = copy.deepcopy(nondominated[0][:])
    parent_pop.sort(cmp = compare)
    bestObj = parent_pop[0]
    return bestObj, evaluationTime, g    #return the Pareto front,the last environment K,the last generation

def compare(a, b):
    if a["violation_objectives"][0] < b["violation_objectives"][0]:
        return -1
    elif a["violation_objectives"][0] > b["violation_objectives"][0]:
        return 1
    else:
        if a["objectives"] < b["objectives"]:
            return -1
        elif a["objectives"] > b["objectives"]:
            return 1
        else:
            return 0
        
def run(problem_initialize, generation, _popsize, evaluator, outputfreq = 1, condition = lambda x : False):
    global popsize
    rvea = RVEA(_popsize,2+problem_initialize[5],generation)
    popsize = rvea.popsize
    init(popsize, problem_initialize, evaluator)
    return loop(generation, outputfreq, condition,rvea)
    
def get_average(res):
    c = sum(res)
    ave = float(c)/len(res)
    return ave

def get_variance(res,ave):
    sumvar = 0.0
    for i in range(len(res)):
        sumvar = sumvar+pow(float(res[i])-ave,2)
    var = pow(sumvar/len(res),0.5)
    return var
       
if __name__ == '__main__':
    import c01,c02,c03,c04,c05,c06,c07,c08,c09,c10,c11,c12,c13,c14,c15,c16,c17,c18
    import g01,g02,g03,g04,g05,g06,g07,g08,g09,g10,g11,g12,g13,g14,g15,g16,g17,g18,g19,g20,g21,g22,g23,g24
    # problemModule = [c01,c02,c03,c04,c05,c06,c07,c08,c09,c10,c11,c12,c13,c14,c15,c16,c17,c18]
    problemModule = [g01,g02,g03,g04,g05,g06,g07,g08,g09,g10,g11,g12,g13,g14,g15,g16,g17,g18,g19,g20,g21,g22,g23,g24]
    print "this is Dynamic_RVEA"
    start = 0
    end = len(problemModule)
    if len(sys.argv)>1:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
    for m in problemModule[start:end]:
        print "this is",m.__name__,"problem"
        problem_initialize = m.problem_initialize()
        print "D is ",problem_initialize[0]
        t = 25
        res = []
        res1 = []
        res2 = []
        initFile = open(RESULT_DIR+"/"+str(m.__name__)+".txt",'w')
        initFile.write("this is nsga_ii")
        initFile.write('\n')
        initFile.close()
        while t > 0:
            avr=(run(problem_initialize,10000, 105,m.evaluate ,0))
            res.append(avr[0])
            res1.append(avr[1])
            res2.append(avr[2])
            initFile = open(RESULT_DIR+"/"+str(m.__name__)+".txt",'a')
            initFile.write('run is '+str(t))
            initFile.write('\n')
            initFile.write(str(avr))         
            initFile.write('\n')
            t -= 1
            initFile.close()
        tmp_avr = []
        for i in range(len(res)):
            tmp_avr.append(res[i]["objectives"][0])
        initFile = open(RESULT_DIR+"/"+str(m.__name__)+".txt",'a')
        print tmp_avr
        print "tmp_avr ",tmp_avr
        print 'the Max is :',max(tmp_avr)
        print 'the Min is :',min(tmp_avr)
        maxo = max(tmp_avr)
        mino = min(tmp_avr)
        ave = get_average(tmp_avr)
        print 'the average is :',ave
        var = get_variance(tmp_avr,ave)
        print 'the variance is :',var
        initFile.write("maxo is "+str(maxo))
        initFile.write('\n')
        initFile.write("mino is "+str(mino))
        initFile.write('\n')
        initFile.write("the average is "+str(ave))
        initFile.write('\n')
        initFile.write("variance is "+str(var))
        initFile.write('\n')
        initFile.write('the generation is '+str(res2))
        initFile.write('\n')
        ave_g = get_average(res2)
        var_g = get_variance(res2,ave_g)
        initFile.write("the average generation is "+str(ave_g))
        initFile.write('\n')
        initFile.write("variance generation is "+str(var_g))
        initFile.write('\n')
        initFile.write('the evaTime is '+str(res1))
        initFile.write('\n')
        ave_evaTime = get_average(res1)
        var_evaTime = get_variance(res1,ave_evaTime)
        initFile.write("the average evaTime is "+str(ave_evaTime))
        initFile.write('\n')
        initFile.write("variance evaTime "+str(var_evaTime))
        initFile.write('\n')
        initFile.close()
