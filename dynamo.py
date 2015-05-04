from itertools import combinations

T = 1 # number of test cases
for t in xrange(1, T+1):
    fin = open(str(t) + ".in", "r")
    N = int(fin.readline())
    d = [[] for i in range(N)]
    for i in xrange(N):
        d[i] = [int(x) for x in fin.readline().split()]
    c = fin.readline()

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
cities.append(0)
frozen_cities = frozenset(cities)
C = {(frozenset([0]), 0, i_zero): 0}
s = 3
while s <= num_cities:
    subsets = list(combinations(cities, s))
    for salami in subsets:
        salami = list(salami)
        if 0 in salami:
            pastrami = frozenset(salami) 
            for j in salami:
                if j != 0:
                    l_subset = salami[:]
                    l_subset.remove(j)
                    f_subset = frozenset(l_subset)
                    top = float('inf')
                    prev_color = None
                    cur_color = cci(j)
                    for v in f_subset:
                        for i in [-3, -2, -1, 1, 2, 3]:
                            if (f_subset, v, i) in C and cur_color + i not in [-4, 4]:
                                comparison = C[(f_subset, v, i)] + distances[v][j]
                                if top > comparison:
                                    top = comparison
                                    prev_color = i
                    if prev_color:
                        if cur_color * prev_color > 0:
                            C[(pastrami, j, prev_color + cur_color)] = top
                        else:
                            C[(pastrami, j, cur_color)] = top 
    s += 1


rondo = []
s_cities = frozenset(cities)
roc = float('inf')
next_color = None
prev = None
for j in cities:
    if j != 0:
        for i in [-3, -2, -1, 1, 2, 3]:
            if (s_cities, j, i) in C:
                comparison = C[(s_cities, j, i)]
                if roc >= comparison:
                    roc = comparison
                    next_color = i
                    prev = j
rondo.append(prev)
cities.remove(prev)
dirk = len(cities)
q = 0
while q < dirk:
    s_cities = frozenset(cities)
    top = float('inf')
    nop = None
    cor = 0
    vrep = 0
    if next_color > 1:
        io = [next_color - 1]
    elif next_color == 1:
        io = [-3, -2, -1]
    elif next_color < -1:
        io = [next_color + 1]
    elif next_color == -1:
        io = [3, 2, 1]
    else:
        print 'color error'
    for j in cities:
        for i in io: 
            if (s_cities, j, i) in C:
                if C[(s_cities, j, i)] + distances[j][prev] == roc:
                    vrep = j
                    nop = i
                    cor = C[(s_cities, j, i)]
    roc = cor
    prev = vrep
    next_color = nop
    rondo.append(prev)
    cities.remove(prev)
    q += 1

wat = 0
for i in range(len(rondo)-1):
    print rondo[i], '->', rondo[i+1], ':', distances[rondo[i]][rondo[i+1]]
    wat += distances[rondo[i]][rondo[i+1]]

donda = []
for r in rondo:
    donda.append(colors[r])

print 'Dynamic Programming Algorithm'
print 'Order:', rondo
print 'Colors:', donda
print 'Length:', wat