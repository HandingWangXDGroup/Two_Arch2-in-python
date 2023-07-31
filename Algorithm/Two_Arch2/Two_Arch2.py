from Public.InitialPop import initial
from Algorithm.Two_Arch2.UpdateCA import UpdateCA
from Algorithm.Two_Arch2.UpdateDA import UpdateDA
from Algorithm.Two_Arch2.MatingSelection import MatingSelection 

from Operator.CrossAndMutation import crossMutation
from DrawFunction.Draw import draw
import time
import matplotlib.pyplot as plt
import numpy as np

from Metric.HV import HV


def Two_Arch2(N,maxgen,problem,encoding):
    start = time.time()
    D = problem.D
    M = problem.M
    lower = problem.lower
    upper = problem.upper

    CAsize = N
    p = 1/M

    pc = 1
    pm = 1/D

    kappa = 0.05

    pop = initial(N,D,M,lower,upper,problem,encoding)


    CA = UpdateCA([],pop, CAsize)
    DA = UpdateDA([],pop, N,p)


    
    gen = 1

    plt.ion()
    fig = plt.figure()

    while gen<=maxgen:
        ParentC, ParentM = MatingSelection(CA,DA,N)
        Offspring1 = crossMutation(ParentC, D, lower, upper, pc, 0, problem, 20, 0)
        Offspring2 = crossMutation(ParentM, D, lower, upper, 0, pm, problem, 0, 20)
        Offspring = Offspring1 + Offspring2

        CA = UpdateCA(CA,Offspring, CAsize)
        DA = UpdateDA(DA,Offspring, N,p)

    

        draw(problem,DA, M,fig)
        if gen <maxgen:
             plt.clf()


        if (gen % 10) == 0:
            print("%d gen has completed!\n" % gen)
        gen = gen + 1;
    end = time.time()

    plt.ioff()
    print("runtime: %.2fs"%(end-start))

    score = HV(DA)
    print("HV indicator:%f" % score)

    # plt.show()