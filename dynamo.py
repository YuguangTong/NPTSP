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
o_cities = cities + [51]
cities.append(0)
frozen_cities = frozenset(cities)
C = {(frozenset([0]), 0, i_zero): 0}
s = 3
while s <= num_cities + 1:
    subsets = list(combinations(cities, s))
    for salami in subsets:
        salami = list(salami)
        if salami[0] == 0 and salami[-1] == 0:
            del salami[-1]
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
            salami.append(51)
        if salami == o_cities:
            pastrami = frozenset(salami)
            j = 0
            l_subset = salami[:]
            l_subset.remove(51)
            f_subset = frozenset(l_subset)
            l_subset.remove(j)
            top = float('inf')
            prev_color = None
            cur_color = cci(j)
            for v in l_subset:
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


rondo = [0]
s_cities = frozenset(cities + [51])
top = float('inf')
next_color = 0
for i in [-3, -2, -1, 1, 2, 3]:
    if (s_cities, 0, i) in C:
        comparison = C[(s_cities, 0, i)]
        if top >= comparison:
            top = comparison
            next_color = i
roc = top
prev = 0
cities = range(num_cities)
q = 0
dirk = len(cities)
while q < dirk:
    s_cities = frozenset(cities)
    top = float('inf')
    nop = 0
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
    if cities == [0]:
        end = None
    else:
        end = 0
    for j in cities:
        if j != None:
            for i in io: 
                if (s_cities, j, i) in C:
                    if C[(s_cities, j, i)] + distances[j][prev] == roc:
                        vrep = j
                        nop = i
                        cor = C[(s_cities, j, i)]
    roc = cor
    prev = vrep
    rondo.append(prev)
    cities.remove(prev)
    next_color = nop
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