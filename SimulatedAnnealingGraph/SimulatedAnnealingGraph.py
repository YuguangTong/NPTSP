from random import randint 
from math import exp 
from nntsp import *


class SimulatedAnnealingGraph(Object): 

    """Creates a graph object for finding a tour using simulated annealing!"""

    def __init__(self, distMatrix, colorList, numCity, cooling_factor=.995, startTemp=100, endTemp=.1): 
        
        # conditions for the input values
        assert 0 < cooling_factor < 1, "Cooling factor (alpha) must be a float in (0, 1) --> " + cooling_factor
        assert 0 < endTemp, "The ending temperature must be greater than 0 --> " + endTemp
        assert startTemp > endTemp, "The starting temperature must be greater than the ending temperature"

        # check number of cities and input matrix are same length
        assert len(distMatrix) = numCity, "Size of the input matrix must match the njumber of cities. \
        cities: " + numCity + ", length of input: " + len(distMatrix) 
        
        self.cities = distMatrix
        self.colorList = colorList
        self.numcities = numCity
        self.redSet = set()
        self.blueSet = set()
        self.startTemp = startTemp
        self.endTemp = endTemp
        self.alpha = cooling_factor
        self.bestTour = None
        self.bestScore = None
        self.nnGraph = nnGraph(distMatrix, colorList, numCity)
        

    def visit_city(self, city): 
        if (city in redSet) or (city in blueSet): 
            if colorList[city] == 'R': 
                redSet.remove(city)
            else: 
                blueSet.remove(city)
        else: 
            print "Error: Invalid City"


    def tour_cost(self, tour): 
        assert len(tour) = self.numcities
        cost = 0
        for i in range (self.numcities):
            cost += self.cities[tour[i]][tour[i+1]]
        return cost

    



    def is_valid_tour(self, tour): 

        """Same as Yuguang's check tour method, that returns TRUE iff the tour (represented
        as the list of cities) does not violate constraints"""

        count = 0
        prev = 'X'
        for k in range(self._numCity):
            cur = self._colorList[tour[k]]
            if cur == prev:
                count += 1
                if count > 3:
                    return False
            else:
                prev = cur
                count = 1
        return True


    def select_random_tour(self): #May or may not be useful

        """Returns a random tour."""

        tour = []
        reds = list(self.redSet)
        blues = list(self.blueSet)
        
        
        red = False
        for i in range (self.numcities):
            if red: 
                x = (random.randint(0,1) * (len(reds) - 1) ) // 1
                print("x: ", x)
                city = reds[x]
                reds.remove(city)
                tour.append(city)
                red = False
            else: 
                x = (random.randint(0,1) * (len(blues) - 1)) // 1
                print("x: ", x)
                city = blues[x]
                blues.remove(city)
                tour.append(city)
                red = True

        if self.is_valid_tour(tour) and len(tour) == self.numcities: 
            return tour
        else: 
            print("RANDOM TOUR IS BAD")
            
        return None


    def generate_probability(prevScore, nextScore, temperature): 

        """Generate probability of choosing worse solution based on the previous score, 
        the next score generated, and the current temperature."""

        if nextScore > prevScore: 
            return 1.0
        else: 
            return math.exp( -abs(next_score-prev_score)/temperature )

    def distance_swap(list_of_cities, index_a, index_b):
        
        """
        Takes a list of cities in output form and two indices, and returns the list with
        cities swapped. 

        """
        swapThis = list_of_cities[index_a]
        list_of_cities[index_a] = list_of_cities[index_b]
        list_of cities[index_b] = swapThis
        return list_of_cities
    

    def anneal(self, maxIterations, start_temp = self.startTemp, end_temp = self.endTemp, alpha = self.alpha): 
        
        """
        Returns a tour using simulated annealing.

        @param: maxIterations --> the number of interations in the restart process
        @param: start_temp --> 

        """

        # starting from a random path may be more effective, because it could
        # cool very quickly with a nearestneighbor
        
        """

        # take in a graph and run nnTSP on the graph 
        currentBest = self.nnGraph.nn_best_reversed()
        if is_valid_tour(currentBest[0]): 
            # the eventual ouput of cities, but intially the input list
            citiesBest = currentBest[0]
            # the prelimary weight of the path (second index of nn_graph tuple)
            currentBest_weight = currentBest[1]
        else: 
            print("Error: NN Tour is invalid") 
            return None

        """
        citiesBest = self.select_random_tour()
        currentBest_weight = self.tour_cost(citiesBest)
        
        distances_current = []
        distances_best = []
        ids_iteration = []

        try:
            for iteration in range(maxIterations):
                # search is restarted at every iteration from the best known solution
                temperature = start_temp
                cities_current = citiesBest
                distance_current = currentBest_weight
                distance_new = currentBest_weight
                cities_new = citiesBest
                ### TEST ###
                print "Initialized parameters:"
                print "starting temperature --> " + temperature
                print "input list of cities (should be a list of indices 0-49) -->"
                    + str(cities_current)
                print "weight of the tour above --> " + distance_current 

                step = 0
                while temperature > end_temp:
                    # computing indices of the two cities to swap
                    # never move the first city (??)
                    index = random.sample(self.numcities-1, 2)
                    ### TEST ###
                    print "These are the indices of cities to be swapped " + str(index)
                    # why this? not sure that we need it
                    # index[0] += 1
                    # index[1] += 1
                    # naming the swapped cities
                    cityA = index[0]
                    cityB = index[1]

                    # optimize by recomputing only the changed distances
                    
                    # creating a new list of the swapped cities
                    swap_before = distance_swap(cities_new, cityA, cityB)
                    # ensure that this swap creates a valid path, otherwise start over
                    if self.is_valid_tour(swap_before) == False:
                        continue

                    cities_new[cityA], cities_new[cityB] = cities_new[cityB], cities_new[cityA]
                    swap_after = distance_swap(cities_new, cityA, cityB)

                    # and their costs
                    swap_before_cost = tour_cost(swap_before)
                    swap_after_cost = tour_cost(swap_after)
                    ### TEST ###
                    print "Now, cities_current and cities_new should only differ in their indices, "
                        + cityA + ", " + cityB
                    print "cities_current / cost --> " + cities_current + " / " + self.tour_cost(cities_current)
                    print "cities_new / cost -->" + cities_new + " / " + self.tour_cost(cities_new)

                    # compute the distance of the swapped city list
                    # not exactly sure why these additions and subtractions work this way
                    distance_new = distance_new - swap_before_cost + swap_after_cost

                    # Kirkpatrick acceptance probability
                    diff = distance_new - distance_current
                    if diff < 0 or math.exp( -diff / temperature ) > random.random():
                        cities_current = cities_new[:]
                        distance_current = distance_new

                    else:
                        # no improvement and worsened result not within alpha
                        distance_new = distance_current
                        cities_new = cities_current[:]

                    # update the best known if solution is an improvement
                    # not for the annealing, but for restarts (in which we start
                    # with the best solution known)
                    if distance_current < currentBest_weight:
                        citiesBest = cities_current[:]
                        currentBest_weight = distance_current

                    # decrease temperature by alpha, increment step counter
                    if True:
                        distances_current.append(distance_current)
                        distances_best.append(distance_best)
                    temperature = temperature * alpha
                    step += 1

                ids_iteration.append(len(distances_current))

        except KeyboardInterrupt, e:
            print "Interrupted on user demand"
            print "performed iterations: " + iteration
            print "current best tour: " + citiesBest
            print "cost of current best tour: " + currentBest_weight

        self.bestScore = currentBest_weight
        self.bestTour = citiesBest
        
        return citiesBest, distances_current, distances_best, ids_iteration     





        
        
        

    

    
