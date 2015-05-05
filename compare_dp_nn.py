import os, sys, traceback
from nntsp.nngraph import nnGraph
#from antTSP.antcolony import AntColony
#from antTSP.antgraph import AntGraph
from dptsp.dptsp import dp
num_input = 495
if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[2]:
        num_of_comparison = int(sys.argv[2])
        input_dir = sys.argv[1]
    else:
        print("usage: python compare_dp_nn.py [instance_dir] [num_of_comparison")
        sys.exit(1)
    # assume that input is in directory e.g. ./testin/
    # output answer to ./anwswer.out
    fout = open("answer.out", "w")
    os.chdir(os.path.expanduser(input_dir))
    counter = 0
    for t in range(1, num_input+1):
        if counter >= num_of_comparison:
            exit(0)
        fin = open(str(t) + ".in", "r")
        numCity = int(fin.readline())
        if numCity <= 20:
            counter += 1
        else:
            continue
        distMatr = [[] for i in range(numCity)]
        for i in range(numCity):
            distMatr[i] = [int(x) for x in fin.readline().split()]
        colorList = fin.readline().strip() #strip is necessary to remove space
        
        print '\n'
        print "working on " + str(t) + ".in.............................."
        print "problem size: ", numCity
        print '\n'
###########################################
## Nearest neighbor
###########################################
        g = nnGraph(distMatr, colorList, numCity)
        nn_tour = g.nn_best_reversed()[0]
        nn_assign = [c + 1 for c in nn_tour]
        print "-----------NN Result-------------"
        print "without revsersal:", nn_assign
        print "color:",''.join(g._colorList[i] for i in nn_tour)
        print "tour cost is", g.tour_cost(nn_tour)
###########################################                                    
## Dynamic programming
########################################### 
        
        dp_assign = dp(numCity, distMatr, colorList, True)[0]
        dp_tour = [c - 1 for c in dp_assign]
        if g.tour_cost(nn_tour) > g.tour_cost(dp_tour):
            fout.write("%s\n"% " ".join(map(str, dp_assign)))
        else:
            fout.write("%s\n"% " ".join(map(str, nn_assign)))
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
        """
    fout.close()
    os.chdir(os.path.expanduser("../"))
