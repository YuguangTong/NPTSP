import os, sys, traceback
#from nntsp.nngraph import Graph
from antcolony import AntColony
from antgraph import AntGraph

T = 1
if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1]:
        T = int(sys.argv[1])
    else:
        print("usage: python3 test.py [num_of_input_files]")
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
        
        print("working on " + str(t) + ".in....................")
###########################################
## Nearest neighbor
###########################################
        """
        g = Graph(distMatr, colorList, numCity)
        tour = g.nn_best()[0]
        assign = [c + 1 for c in tour]
        fout.write("%s\n"% " ".join(map(str, assign)))
        print("-----------NN Result-------------")
        print(assign)
        print("tour cost is", g.tour_cost(tour))
        """
###########################################
## Ant colony
###########################################
        num_nodes = 10
        num_ants = 20
        num_iterations = 1
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
            
            print("-----------AntColony Result-------------")
            print "best path = ", str(best_path_vec)
            print "best path cost is", str(best_path_cost)
        
        except Exception as e:
            print "exception: ", str(e)
            traceback.print_exc()
    fout.close()
    os.chdir(os.path.expanduser("../"))
