from antcolony import AntColony
from antgraph import AntGraph

import pickle
import sys
import traceback

#default
num_nodes = 10

if __name__ == "__main__":   
    if len(sys.argv) > 1 and sys.argv[1]:
        num_nodes = int(sys.argv[1])

    num_ants = 30
    num_iterations = 2
    num_repetitions = 1

    T = 1
    fout = open ("answer.out", "w")
    for t in xrange(1, T+1):
        fin = open(str(t) + ".in", "r")
        N = int(fin.readline())
        d = [[] for i in range(N)]
        for i in xrange(N):
            d[i] = [int(x) for x in fin.readline().split()]
        c = fin.readline()

    cost_mat = d 

    print N
    print d
    print c


    try:
        graph = AntGraph(N, cost_mat)
        best_path_vec = None
        best_path_cost = sys.maxint
        for i in range(0, num_repetitions):
            graph.reset_tau()
            ant_colony = AntColony(graph, num_ants, num_iterations, c)
            ant_colony.start(c)
            if ant_colony.best_path_cost < best_path_cost:
                best_path_vec = ant_colony.best_path_vec
                best_path_cost = ant_colony.best_path_cost


        best_path_vec = [x+1 for x in best_path_vec]

        print "\n------------------------------------------------------------"
        print "                     Results                                "
        print "------------------------------------------------------------"
        print "\nBest path = %s" % (best_path_vec,)
        print "\nBest path cost = %s\n" % (best_path_cost,)
        for node in best_path_vec:
            print c[node - 1] + " ",
    
        fout.write("%s\n" % " ".join(map(str, best_path_vec)))
        fout.close()

    except Exception, e:
        print "exception: " + str(e)
        traceback.print_exc()
