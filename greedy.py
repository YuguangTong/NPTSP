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

cur_city = 0
cities = range(num_cities)
cities.remove(0)
path = [0]
at = cci(cur_city)
while cities:
    top = float('inf')
    bop = 0
    for next_city in cities:
        if at + cci(next_city) not in [-4, 4]: 
            comparison = distances[cur_city][next_city]
            if top > comparison:
                top = comparison
                bop = next_city
    cur_city = bop
    if at * cci(bop) > 0:
        at += cci(bop)
    else:
        at = cci(bop)
    path.append(cur_city)
    cities.remove(cur_city)

wat = 0
for i in range(len(path)-1):
    print path[i], '->', path[i+1], ':', distances[path[i]][path[i+1]]
    wat += distances[path[i]][path[i+1]]

donda = []
for r in path:
    donda.append(colors[r])

print 'Greedy Algorithm'
print 'Order:', path
print 'Colors:', donda
print 'Length:', wat
