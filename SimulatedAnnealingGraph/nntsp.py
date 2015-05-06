from nngraph import nnGraph

# python2 script
# input: 1.in, 2.in etc
# output: answer.out
T = 1
fout = open("answer.out", "w")
for t in range(1, T + 1):
    fin = open(str(t) + ".in", "r")
    numCity = int(fin.readline())
    distMatr = [[] for i in range(numCity)]
    for i in range(numCity):
        distMatr[i] = [int(x) for x in fin.readline().split()]
    colorList = fin.read().strip()
    fin.close()
    print numCity
    print colorList, "distrance matrix:"
    print distMatr


    g = nnGraph(distMatr, colorList, numCity)
    
    assign = [0] * numCity
    tour = g.nn_best()[0]
    for i in tour:
        assign[i] = tour[i] + 1
    fout.write("%s\n"% " ".join(map(str, assign)))
    print assign
    print "tour cost is", g.tour_cost(tour)
fout.close()
