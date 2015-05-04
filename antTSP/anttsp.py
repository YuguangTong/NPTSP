from antcolony import AntColony
from antgraph import AntGraph

import pickle
import sys
import traceback


if __name__ == "__main__":   


    num_ants = 5
    num_iterations = 200
    num_repetitions = 1

    T = 1 # number of test cases
    fout = open ("answer.out", "w")
    for t in xrange(1, T+1):
        fin = open(str(t) + ".in", "r")
        N = int(fin.readline())
        d = [[] for i in range(N)]
        for i in xrange(N):
            d[i] = [int(x) for x in fin.readline().split()]
        c = fin.readline()

        cost_mat = d 

        print "\n"
        print "\n************************************************************"
        print "\nTest # %s" % t 
#        print d
        print "\nSize of Input: %s" % N


        try:
            graph = AntGraph(N, cost_mat)
            best_path_vec = None
            best_path_cost = sys.maxint
            for i in range(0, num_repetitions):
                graph.reset_tau()
                ant_colony = AntColony(graph, num_ants, num_iterations, c)
#                print "HANG AFTER ANYCOLONY"

                ant_colony.start(c)
#                print "HANG AFTER START?"
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

        except Exception, e:
            print "exception: " + str(e)
            traceback.print_exc()

    fout.close()

