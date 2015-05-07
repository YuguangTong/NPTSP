import os, sys, traceback
from nngraph import nnGraph
from SimulatedAnnealingGraph import * 
import random

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
        
        maxIterations = 100
        cooling_factor = .9995
        startTemp = 110
        endTemp = .1

        instance = SimulatedAnnealingGraph(distMatr, colorList, numCity, maxIterations, cooling_factor, startTemp, endTemp)

        seed = time.time()
        random.seed(seed)

        time_begin = time.time()

        print 'Starting simulated annealing on ' + str(t) + '.in, CTRL+C to interrupt...'

        (annealing_result, distances_current, distances_best, starting_weight) = instance.anneal()

        time_end = time.time()

        # print "distances_current--> " , distances_current

        print 'Result: ' + str(annealing_result)
        if instance.is_valid_tour(annealing_result):
            print "This tour is valid."
        print 'Result cost:             %8.0f'     % instance.tour_cost(annealing_result)
        print 'Improvement:             %8.0f %%'  % (100 * (starting_weight - instance.bestScore) / starting_weight)
        print 'Time:                    %8.0f sec' % (time_end - time_begin)
        print 'Initial cost:            %8.0f'     % starting_weight
        
        


      
