import os, sys, traceback
from nntsp.new_nngraph import nnGraph
from antTSP.antcolony import AntColony
from antTSP.antgraph import AntGraph

T = 1
if __name__ == "__main__":
    if len(sys.argv) == 4:
        S = int(sys.argv[2])
        T = int(sys.argv[3])
        input_dir = sys.argv[1]
    else:
        print("usage: python run.py [path_of_input_folder] [start_file_num] [num_of_input_files]")
        sys.exit(1)
    # assume that input is in directory e.g. ./testin/
    # output answer to ./anwswer.out
    fout = open("answer.out", "w")
    os.chdir(os.path.expanduser(input_dir))
    for t in range(S, T + S):
        fin = open(str(t) + ".in", "r")
        numCity = int(fin.readline())
        distMatr = [[] for i in range(numCity)]
        for i in range(numCity):
            distMatr[i] = [int(x) for x in fin.readline().split()]
        colorList = fin.readline().strip() #strip is necessary to remove space
        
        print '\n'
        print "working on " + str(t) + ".in ===================="
        print '\n'
        
        best_assign = None
        best_cost = 5000
###########################################
## Nearest neighbor
###########################################
        g = nnGraph(distMatr, colorList, numCity)
        tour, cost = g.nn_best_reversed()
        assign = [c + 1 for c in tour]
        best_assign = assign
        best_cost = cost
        print "---NN + reversal-------------"
        #print assign
        #print "color:", g.get_color(tour)
        print "cost", cost
##########################################
## Hill climbing
##########################################
        tour, cost = g.hill_climbing(2000)
        print "---Hill climbing-------------"
        assign = [c+1 for c in tour]
        #print "color:", g.get_color(tour)
        print "cost:", g.tour_cost(tour)
        if cost < best_cost:
            best_cost = cost
            best_assign = assign
##########################################
## Swap combined with reversal    
##########################################          
        tour, cost = g.nn_best_reversed_swapped()
        print "---NN + reversal + swap------"
        assign = [c+1 for c in tour]
        #print "color:", g.get_color(tour)
        print "cost:", g.tour_cost(tour)        
        if cost < best_cost:
            best_cost = cost
            best_assign = assign

        fout.write("%s\n"% " ".join(map(str, best_assign)))
