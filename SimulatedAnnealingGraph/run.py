import os, sys, traceback
from nngraph import *
from SimulatedAnnealingGraph import * 

T = 1
if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[2]:
        T = int(sys.argv[2])
        input_dir = sys.argv[1]
    else:
        print("usage: python run.py [path_of_input_folder] [num_of_input_files]")
        sys.exit(1)
    # assume that input is in directory e.g. ./testin/
    # output answer to ./anwswer.out
    fout = open("answer.out", "w")
    os.chdir(os.path.expanduser(input_dir))
    for t in range(1, T + 1):
        fin = open(str(t) + ".in", "r")
        numCity = int(fin.readline())
        distMatr = [[] for i in range(numCity)]
        for i in range(numCity):
            distMatr[i] = [int(x) for x in fin.readline().split()]
        colorList = fin.readline().strip() #strip is necessary to remove space
        
        print '\n'
        print "working on " + str(t) + ".in.............................."
        print '\n'

#############################################################################
###### *** Make a SIMULATED ANNEALING GRAPH and run ANNEAL function. *** ####
#############################################################################
        
        maxIterations = 40
        saGraph = SimulatedAnnealingGraph(distMatr, colorList, numCity)
        print("Running simulated annealing on ", numCity, " by ", numCity, 
              "matrix.") 
        print("......................................................")
        saTour = saGraph.anneal(maxIterations) #run saTour with maxIterations
        tour, cost = saTour[0], saTour[1]
        print("Tour result: ", tour) #print result of calling anneal
        print("Tour cost: ", cost)
        print("Color list:",''.join(saGraph.colorList[i] for i in tour))
        


      
