from itertools import combinations

def dp(num_cities, actual_size, distances, colors, print_path=False):
    def cci(city):
        if colors[city] == 'R':
            return -1
        else:
            return 1    
    C={}
    cities = actual_size
    for city in cities:
        C[(frozenset([city]), city, cci(city))] = 0

    s = 2
    while s <= num_cities:
        subsets = list(combinations(cities, s))
        for salami in subsets:
            salami = list(salami)
            pastrami = frozenset(salami) 
            for j in salami:
                l_subset = salami[:]
                l_subset.remove(j)
                f_subset = frozenset(l_subset)
                top = float('inf')
                prev_color = None
                cur_color = cci(j)
                for v in f_subset:
                    for i in [-3, -2, -1, 1, 2, 3]:
                        if (f_subset, v, i) in C and \
                           cur_color + i not in [-4, 4]:
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
    solutions = None
    potentials = list(combinations(cities, num_cities))
    for p in potentials:
        list_p = list(p)
        frozen_p = frozenset(list_p)
        for j in frozen_p:
            for i in [-3, -2, -1, 1, 2, 3]:
                if (frozen_p, j, i) in C:
                    comparison = C[(frozen_p, j, i)]
                    if roc >= comparison:
                        roc = comparison
                        next_color = i
                        prev = j
                        solutions = list_p[:]
    rondo.append(prev)
    relevant_cities = solutions[:]
    relevant_cities.remove(prev)
    dirk = num_cities-1
    q = 0
    while q < dirk:
        s_cities = frozenset(relevant_cities)
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
        for j in relevant_cities:
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
        relevant_cities.remove(prev)
        q += 1
    
    if print_path:
        print 'Dynamic Programming Algorithm'
        print '============================='
    
    wat = 0
    for i in range(len(rondo)-1):
        if print_path: print rondo[i]+1, '->', rondo[i+1]+1, ':', \
           distances[rondo[i]][rondo[i+1]]
        wat += distances[rondo[i]][rondo[i+1]]
    
    donda = []
    for r in rondo:
        donda.append(colors[r])

    for t in range(len(rondo)):
        rondo[t] += 1

    if print_path:
        print '============================='
        print 'Order:', rondo
        print 'Colors:', donda
        print 'Length:', wat
    return rondo, wat, donda


if __name__=="__main__":
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
    dp(N, d, c)
    
