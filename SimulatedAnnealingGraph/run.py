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
    for t in range(10, T + 1):
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
        nn_input = nnGraph(distMatr, colorList, numCity)
        nn_tour = nn_input.nn_best_reversed()[0]

        maxIterations = 50
        cooling_factor = .995
        startTemp = 120
        endTemp = .1
        anneal_calls = 10

        solution_cities = []
        solution_weight = 5000

        seed = time.time()
        random.seed(seed)

        time_begin = time.time()

        print 'Starting simulated annealing on ' + str(t) + '.in, CTRL+C to interrupt...'

        for call in range(anneal_calls):
            instance = SimulatedAnnealingGraph(distMatr, colorList, numCity, maxIterations, cooling_factor, startTemp, endTemp)
            (annealing_result, distances_current, distances_best, starting_weight) = instance.anneal()
            case_cities = annealing_result
            case_cost = instance.tour_cost(annealing_result)
            if case_cost < solution_weight:
                solution_cities = case_cities
                solution_weight = case_cost

        time_end = time.time()

        print 'Result: ' + str(solution_cities)
        if instance.is_valid_tour(solution_cities):
            print "This tour is valid."
        """
        # write to answer.out
        tour = annealing_result
        assign = [c + 1 for c in tour]
        fout.write("%s\n"% " ".join(map(str, assign)))
        """
        print 'Result cost:             %8.0f'     % solution_weight
        print 'Time:                    %8.0f sec' % (time_end - time_begin)
        print 'Initial cost:            %8.0f'     % instance.tour_cost(nn_tour)
        


      
