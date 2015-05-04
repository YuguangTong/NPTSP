import os, sys, traceback
from nntsp.nngraph import nnGraph
from antTSP.antcolony import AntColony
from antTSP.antgraph import AntGraph

T = 1
if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1]:
        T = int(sys.argv[1])
    else:
        print("usage: python test.py [num_of_input_files]")
        sys.exit(1)
    # assume that input is in directory ./testin/
    # output answer to ./anwswer.out
    fout = open("answer.out", "w")
    os.chdir(os.path.expanduser("./testin"))
    for t in range(1, T + 1):
        fin = open(str(t) + ".in", "r")
        numCity = int(fin.readline())
        distMatr = [[] for i in range(numCity)]
        for i in range(numCity):
            distMatr[i] = [int(x) for x in fin.readline().split()]
        colorList = fin.readline()
        
        print '\n'
        print "working on " + str(t) + ".in.............................."
        print '\n'
###########################################
## Nearest neighbor
###########################################
        g = nnGraph(distMatr, colorList, numCity)
        tour1 = g.nn_best()[0]
        assign1 = [c + 1 for c in tour1]
        tour2 = g.nn_best_reversed()[0]
        assign2 = [c + 1 for c in tour2]
        fout.write("%s\n"% " ".join(map(str, assign2)))
        print "-----------NN Result-------------"
        print "without revsersal:", assign1
        print "tour cost is", g.tour_cost(tour1)
        print "color:", ''.join(g._colorList[i] for i in tour1)
        print "without revsersal:", assign2
        print "tour cost is", g.tour_cost(tour2)
        print "color:",''.join(g._colorList[i] for i in tour2)
###########################################
## Ant colony
###########################################
        """
        num_nodes = 10
        num_ants = 30
        num_iterations = 10
        num_repetitions = 1
        try:
            graph = AntGraph(numCity, distMatr)
            best_path_vec = None
            best_path_cost = sys.maxsize
            for i in range(0, num_repetitions):
                graph.reset_tau()
                ant_colony = AntColony(graph, num_ants, num_iterations, colorList)
                ant_colony.start(colorList)
                if ant_colony.best_path_cost < best_path_cost:
                    best_path_vec = ant_colony.best_path_vec
                    best_path_cost = ant_colony.best_path_cost

            best_path_vec = [x+1 for x in best_path_vec]
            
            print "-----------AntColony Result-------------"
            print "best path = ", best_path_vec
            print "best path cost is", best_path_cost
        
        except Exception as e:
            print "exception: ", str(e)
            traceback.print_exc()
    fout.close()
    os.chdir(os.path.expanduser("../"))
    """
