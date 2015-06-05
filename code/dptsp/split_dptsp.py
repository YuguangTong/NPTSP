from dptsp2 import dp
from random import randint

if __name__=="__main__":
    T= 1
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

def split_dp(num_cities, distances, colors, split, print_path=False):
    assert split % 2 == 0, "split must be divisible by two"
    split_solutions = []
    remainder = num_cities % split
    actual_size = range(num_cities)
    while num_cities > 0:
        if num_cities >= split: mini_size = split 
        else: mini_size = remainder
        part = dp(mini_size, actual_size, distances, colors)
        split_solutions.append(part) 
        for city in part[0]:
            actual_size.remove(city-1)
        num_cities -= mini_size
    total_length = 0
    final_path = []
    final_colors = []
    for i in split_solutions:
        total_length += i[1]
        final_path += i[0]
        final_colors += [colors[x-1] for x in i[0]]
    for i in range(len(split_solutions)-1):
        total_length += \
        distances[split_solutions[i][0][-1]-1][split_solutions[i+1][0][0]-1]
    print total_length
    print final_path
    print final_colors
    '''
    red = []
    blue = []
    for city in range(num_cities):
        if colors[city] == 'R':
            red.append(city)
        else:
            blue.append(city)
    
    num_problems = num_cities / split
    mini_problems = []
    mini_colors = []
    for i in range(num_problems):
        mini_problem = []
        for j in range(split/2):
            index = randint(0, len(red)-1)
            mini_problem.append(red.pop(index))
            mini_problem.append(blue.pop(index))
        mini_problems.append(mini_problem)

        mini_color = []
        for x in range(split):
            mini_color.append(colors[mini_problem[x]])
        mini_colors.append(mini_color)
     
    remainder = num_cities % split
    mini_problem = []
    for i in range(remainder/2):
        index = randint(0, len(red)-1)
        mini_problem.append(red.pop(index))
        mini_problem.append(blue.pop(index))
    mini_problems.append(mini_problem)
    
    mini_color = []
    for x in range(remainder):
        mini_color.append(colors[mini_problem[x]])
    mini_colors.append(mini_color)
    
    mini_distances = []
    for problem in mini_problems:
        problem_distances = []
        for city in problem:
            city_distances = []
            for comparison_city in problem:
                city_distances.append(distances[city][comparison_city])
            problem_distances.append(city_distances)
        mini_distances.append(problem_distances) 
    
    mini_solutions = []
    for i in range(num_problems+1): 
        local_distances = mini_distances[i]
        mini_solutions.append(dp(len(local_distances), local_distances, 
                                 mini_colors[i], False))
    
    relative_solution = []
    relative_colors = [] 
    for i in range(num_problems+1):
        for x in range(len(mini_problems[i])):
            relative_solution.append(mini_problems[i] \
                                     [mini_solutions[i][0][x]-1])
            relative_colors.append(mini_colors[i][mini_solutions[i][0][x]-1])
    
    length = 0
    for i in range(len(relative_solution)-1):
        print relative_solution[i]+1, '->', relative_solution[i+1]+1, ':', \
              distances[relative_solution[i]][relative_solution[i+1]]
        length += distances[relative_solution[i]][relative_solution[i+1]]
    '''
split_dp(num_cities, distances, colors, 6) 
