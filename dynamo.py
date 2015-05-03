from itertools import combinations

T = 1 # number of test cases
fout = open ("answer.out", "w")
for t in xrange(1, T+1):
    fin = open(str(t) + ".in", "r")
    N = int(fin.readline())
    d = [[] for i in range(N)]
    for i in xrange(N):
        d[i] = [int(x) for x in fin.readline().split()]
    c = fin.readline()
fout.close()

num_cities = N
distances = d
colors = c

def cci(city):
    if colors[city] == 'R':
        return -1
    else:
        return 1

i_zero = cci(0)
cities = range(num_cities)
C = {(frozenset([0]), 0, i_zero): 0}
s = 2

while s <= num_cities:
    subsets = list(combinations(cities, s))
    for salami in subsets:
        if 0 in salami:
            pastrami = frozenset(salami)
            C[(pastrami, 0, i_zero)] = float('inf')
            for j in salami:
                if j != 0:
                    l_subset = list(salami)
                    l_subset.remove(j)
                    f_subset = frozenset(l_subset)
                    top = float('inf')
                    prev_color = None
                    cur_color = cci(j)
                    for v in f_subset:
                        indicator = cci(v)
                        for i in [-3, -2, -1, 1, 2, 3]:
                            if (f_subset, v, i) in C and indicator + i not in [-4, 4]:
                                comparison = C[(f_subset, v, i)] + distances[v][j]
                                if top >= comparison:
                                    top = comparison
                                    prev_color = i
                    if (cur_color < 0 and prev_color < 0) or (cur_color > 0 and prev_color > 0):
                        C[(pastrami, j, prev_color+cur_color)] = top
                    else:
                        C[(pastrami, j, cur_color)] = top

    s += 1

rondo = []
while cities:
    s_cities = frozenset(cities)
    top = float('inf')
    dop = 0
    for j in cities:
        if j != 0:
            for i in [-3, -2, -1, 1, 2, 3]:
                if (s_cities, j, i) in C and i_zero + i not in [-4, 4]:
                    comparison = C[(s_cities, j, i)] + distances[j][0]
                    if top >= comparison:
                        top = comparison
                        dop = j
    rondo.append(dop)
    cities.remove(dop)
wat = distances[rondo[0]][0]
for i in range(len(rondo)-1):
    wat += distances[rondo[i]][rondo[i+1]]
print 'OPTIMUM TOUR:'
print 'Order:', rondo
print 'Length:', wat


