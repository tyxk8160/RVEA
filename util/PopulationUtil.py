#/usr/bin/python

import numpy as np

def CreatePopulation(PopDescibe):
    '''
    describe:
        create Population from numpy array
    Args:
        PopDescibe: np.array
    return:
        pop： Populations
    '''
    pop = []
    N,_ =PopDescibe.shape
    for i in range(N):
        ind = {"genes":list(PopDescibe[i,:])}
        pop.append(ind)
    return pop

def initpopulation(popsize,D,lower,upper):
    '''
    Describe:
        initial populations
    Args:
        popsize：  the size of population
        D: the genes count
        lower: the lower boundary
        upper: the upper boundary
    return:
        population
    '''
    PopDes = lower + (upper-lower)*np.random.rand(popsize,D)

    return CreatePopulation(PopDes)



def evaluate_pop(pop,problem):
    '''
    may have some error
    '''
    for ind in pop:
        ind = problem.evaluate(ind)
    return pop
