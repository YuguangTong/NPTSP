from random import randint 
from math import exp 
from nntsp import *


class SimulatedAnnealingGraph(Object): 

    """Creates a graph object for finding a tour using simulated annealing!"""

    def __init__(self, distMatrix, colorList, numCity): 
        self.cities = distMatrix
        self.colorList = colorList
        self.numcities = numCity
        self.redSet = set()
        self.blueSet = set()
        self.temp = 100
        self.alpha = .9995
        self.bestTour = None
        self.bestScore = None
        self.currentScore = None
        self.nnGraph = nnGraph(distMatrix, colorList, numCity)
        

    def visit_city(self, city): 
        if (city in redSet) or (city in blueSet): 
            if colorList[city] == 'R': 
                redSet.remove(city)
            else: 
                blueSet.remove(city)
        else: 
            print "Error: Invalid City"

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

        return 0

    def generate_probability(prevScore, nextScore, temperature): 

        """Generate probability of choosing worse solution based on the previous score, 
        the next score generated, and the current temperature."""

        if nextScore > prevScore: 
            return 1.0
        else: 
            return math.exp( -abs(next_score-prev_score)/temperature )


    def anneal(self, maxIterations, start_temp = self.temp, alpha = self.alpha): 
        
        """Returns a tour using simulated annealing."""

        numIterations = 0 

        #take in a graph and run nnTSP on the graph 
        theBest = self.nnGraph.nn_best()
        if is_valid_tour(theBest): 
            return theBest
        else: 
            print("Error: NN Tour is invalid") 
            return None
        
        

    
    def kirkpatrick_cooling(start_temp,alpha):
        
        """Cooling schedule (determines rate of temperature decrease)"""

        T=start_temp
        while True:
            yield T
            T=alpha*T
            
            



        
        
        

    

    
