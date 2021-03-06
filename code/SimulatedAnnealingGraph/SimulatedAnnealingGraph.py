nealimport random
import math 
from nngraph import nnGraph
import sys, os
import time


class SimulatedAnnealingGraph(object): 

    """Creates a graph object for finding a tour using simulated annealing!"""

    def __init__(self, distMatrix, colorList, numCity, iterations, cooling_factor=.995, startTemp=100, endTemp=.1): 
        
        # conditions for the input values
        assert 0 < cooling_factor < 1, "Cooling factor (alpha) must be a float in (0, 1) --> " + cooling_factor
        assert 0 < endTemp, "The ending temperature must be greater than 0 --> " + endTemp
        assert startTemp > endTemp, "The starting temperature must be greater than the ending temperature"

        # check number of cities and input matrix are same length
        assert len(distMatrix) == numCity, "Size of the input matrix must match the njumber of cities. \
        cities: " + numCity + ", length of input: " + len(distMatrix) 
        
        self.cities = distMatrix
        self.colorList = colorList
        self.numcities = numCity
        self.redSet = set()
        self.blueSet = set()
        for c in range(self.numcities):
            if colorList[c] == 'R':
                self.redSet.add(c)
            else:
                self.blueSet.add(c)
        self.start_temp = startTemp
        self.end_temp = endTemp
        self.alpha = cooling_factor
        self.bestTour = None
        self.bestScore = None
        self.nnGraph = nnGraph(distMatrix, colorList, numCity)
        self.maxIterations = iterations

    def visit_city(self, city): 
        if (city in redSet) or (city in blueSet): 
            if colorList[city] == 'R': 
                redSet.remove(city)
            else: 
                blueSet.remove(city)
        else: 
            print "Error: Invalid City"


    def tour_cost(self, tour): 
        assert len(tour) == self.numcities
        cost = 0
        for i in range(self.numcities-1):
            cost += self.cities[tour[i]][tour[i+1]]
            # print "What is i -->" + str(i)
        return cost

    def is_valid_tour(self, tour): 

        """Same as Yuguang's check tour method, that returns TRUE iff the tour (represented
        as the list of cities) does not violate constraints"""

        count = 0
        prev = 'X'
        for k in range(self.numcities):
            cur = self.colorList[tour[k]]
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
                city = reds[x]
                reds.remove(city)
                tour.append(city)
                red = False
            else: 
                x = (random.randint(0,1) * (len(blues) - 1)) // 1
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

    def distance_swap(self, list_of_cities, index_a, index_b):
        
        """
        Takes a list of cities in output form and two indices, and returns the list with
        cities swapped. 

        """
        newList = list_of_cities[:]
        swapThis = list_of_cities[index_a]
        newList[index_a] = list_of_cities[index_b]
        newList[index_b] = swapThis
        return newList

    def reverse_cities(self, tour, index_a, index_b):

        newList=tour[:]
        newList[index_a:index_b] = reversed(newList[index_a:index_b])
        return newList
    

    def anneal(self): 
        
        """
        Returns a tour using simulated annealing.

        Assumes a correct input graph.
      
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
        # naive solution to start
        naive = nnGraph(self.cities, self.colorList, self.numcities)
        citiesBest = naive.nn_best_reversed()[0]
        # print "What is the length of citiesBest? --> " + str(len(citiesBest))
        currentBest_weight = self.tour_cost(citiesBest)
        starting_weight = currentBest_weight
        
        distances_current = []
        distances_best = []

        try:
            for iteration in range(self.maxIterations):
                # search is restarted at every iteration from the best known solution
                temperature = self.start_temp
                cities_current = citiesBest
                cities_new = citiesBest
                distance_current = currentBest_weight
                distance_new = currentBest_weight
                
                ### TEST ###
                # print "Initialized parameters: "
                # print "starting temperature --> " , temperature
                """
                print "iteration #" , iteration
                print "input list of cities (should be a list of indices 0-49) -->" + str(cities_current)
                print "weight of the tour above --> " , distance_current 
                """

                step = 0
                while temperature > self.end_temp:
                    # computing indices of the two cities to swap
                    # never move the first city (??)
                    index = random.sample(xrange(self.numcities-1), 2)
                    # print "indices: " , index
                    ### TEST ###
                    # print "These are the indices of cities to be swapped " + str(index)
                    # why this? not sure that we need it
                    # index[0] += 1
                    # index[1] += 1
                    # naming the swapped cities
                    cityA = index[0]
                    cityB = index[1]

                    # optimize by recomputing only the changed distances
                    
                    ha = random.randint(0,1)

                    # creating a new list of the swapped cities
                    if (ha > .2):
                        swap_before = self.distance_swap(cities_new, cityA, cityB)
                        # ensure that this swap creates a valid path, otherwise start over
                        if self.is_valid_tour(swap_before) == False:
                        # print "Does this part actually run?"
                            continue
                    else:
                        swap_before = self.reverse_cities(cities_new, cityA, cityB)
                        if self.is_valid_tour(swap_before) == False:
                            continue

                    ### TESTING TO SEE IF THIS IS THE PROBLEM
                    # cities_new[cityA], cities_new[cityB] = cities_new[cityB], cities_new[cityA]
                    swap_after = cities_new
                    """
                    print "Step: " , step
                    print "before: " , str(swap_before)
                    print "after: " , str(swap_after)
                    """

                    # and their costs
                    ### TEST ###
                    # print "Now, cities_current and cities_new should only differ in their indices, " + str(cityA) + ", " + str(cityB)
                    # print "cities_current / cost --> " , cities_current , " / " , self.tour_cost(cities_current)
                    # print "cities_new / cost -->" , cities_new , " / " , self.tour_cost(cities_new)

                    # compute the distance of the swapped city list
                    # not exactly sure why these additions and subtractions work this way
                    distance_new = self.tour_cost(swap_before)
                    distance_current = self.tour_cost(swap_after)
                    """
                    print "What are distance new and distance current?"
                    print "current: " , distance_current
                    print "new: " , distance_new
                    """
                    # Kirkpatrick acceptance probability
                    
                    diff = distance_new - distance_current
                    """
                    current_cost = self.tour_cost(cities_current)
                    new_cost = self.tour_cost(swap_before)

                    diff = new_cost - current_cost
                    """

                    # print "What is diff? --> " , diff
                    if diff < 0 or math.exp( -diff / temperature ) > random.randint(0,1):
                        # print "Does this ever execute?"
                        cities_current = swap_before
                        distance_current = distance_new

                    """
                    else:
                        # no improvement and worsened result not within alpha
                        distance_new = distance_current
                        cities_current = cities_current[:]
                    """

                    # update the best known if solution is an improvement
                    # not for the annealing, but for restarts (in which we start
                    # with the best solution known)
                    if distance_current < currentBest_weight:
                        citiesBest = cities_current
                        currentBest_weight = distance_current

                    # decrease temperature by alpha, increment step counter
                    distances_current.append(distance_current)
                    distances_best.append(currentBest_weight)
                    temperature = temperature * self.alpha
                    step += 1

                self.bestScore = currentBest_weight
                self.bestTour = citiesBest

        except KeyboardInterrupt, e:
            print "Interrupted on user demand"
            print "performed iterations: " + str(iteration)
            print "current best tour: " + str(citiesBest)
            print "cost of current best tour: " + str(currentBest_weight)

        
        return citiesBest, distances_current, distances_best, starting_weight

    def display_usage():
        print 'usage: performs simulated annealing global metaheurisitic on input XXX.in'
        print '@input a standard NPTSP instance with the .in extension'
        print '@output an NPTSP solution with .out extension'
        print '@param distMatrix: a symmetric 2-dimensional list values 0 <= x <= 100'
        print '@param colorList: a strong of Rs and Bs in order representing the indices of the distMatrix'
        print '@param numCities: the number of indices in the distMatrix'
