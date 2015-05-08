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

min_path_length = float('inf')
min_path_order = []

for city in range(num_cities):
    cur_city = city
    cities = range(num_cities)
    cities.remove(cur_city)
    path = [cur_city]
    at = cci(cur_city)
    while cities:
        top = float('inf')
        bop = None
        for next_city in cities:
            if at + cci(next_city) not in [-4, 4]: 
                comparison = distances[cur_city][next_city]
                if top > comparison:
                    top = comparison
                    bop = next_city
        cur_city = bop
        if cur_city != None:
            if at * cci(bop) > 0:
                at += cci(bop)
            else:
                at = cci(bop)        
            path.append(cur_city)
            cities.remove(cur_city)
        else:
            path = []
            cities = []
    if path == []:
        pass
    else:
        wat = 0
        for i in range(len(path)-1):
            wat += distances[path[i]][path[i+1]]
        if wat < min_path_length and wat != 0:
            min_path_length = wat
            min_path_order = path

print 'Greedy Algorithm'
print '================'

for i in range(len(min_path_order)-1):
    print min_path_order[i]+1, '->', min_path_order[i+1]+1, ':', \
          distances[min_path_order[i]][min_path_order[i+1]]

donda = []
for r in min_path_order:
    donda.append(colors[r])

for t in range(len(min_path_order)):
    min_path_order[t] += 1

if min_path_length != float('inf'):
    print '================'
    print 'Order:', min_path_order
    print 'Colors:', donda
    print 'Length:', min_path_length
else:
    print 'NO PATH FOUND'
