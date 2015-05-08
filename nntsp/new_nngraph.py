from random import randint
from copy import copy
import sys
from nptspGraph import nptspGraph
from itertools import combinations

class nnGraph(nptspGraph):
    """
    Graph representing cities.
    """
    # assume distMatr is a 2d python list

    def __init__(self, distMatr, colorList, numCity):
        """
        Initiator
        distMatr: a python list representing a symmetric distance matrix.
        colorList: a string consisting only 'R' and 'B'
        numCity: number of nodes in the graph

        """
        nptspGraph.__init__(self, distMatr, colorList, numCity)
        self._swap_combinations = None 

    def alternate_color(self, curCity):
        """
        Assume visit in alternating color and
        return the nearest neighboring city of the opposite color to visit.. 

        """
        if self.colorList[curCity] == 'R':
            nextCity = min(self.unvisitedBlue, key = lambda c: self.distMatr[c][curCity])
        else:
            nextCity = min(self.unvisitedRed, key = lambda c: self.distMatr[c][curCity])
        return nextCity

    def nn_tour(self, start = 0):
        """
        Return a nearest neighbor tour starting from START
        """
        self.search_init()
        tour = [start]
        self.visit_city(start)
        while self.unvisitedRed or self.unvisitedBlue:
            curCity = tour[-1]
            nextCity = self.alternate_color(curCity)
            tour.append(nextCity)
            self.visit_city(nextCity)
        return tour
    
    def nn_best(self):
        """
        Return the shortest nearest-neighbor tour starting from any node.
        """
        curTour, curCost = [], sys.maxsize 
        for c in range(self.numCity):
            newTour = self.nn_tour(c)
            newCost = self.tour_cost(newTour)
            if newCost < curCost:
                curTour, curCost = newTour, newCost
        return curTour, curCost

    def nn_best_reversed(self):
        """
        Return the shortest nearest-neighbor tour with reversal tweaks.
        """

        curTour, curCost = [], sys.maxsize
        for c in range(self.numCity):
            newTour = self.alter_tour(self.nn_tour(c))
            newCost = self.tour_cost(newTour)
            if newCost < curCost:
                curTour, curCost = newTour, newCost
        return curTour, curCost

    def nn_best_reversed_swapped(self):
        """
        Return the shortest path tweaking from nearest-neighbor tour
        using both secton reversal and city swapping.
        """
        curTour, curCost = [], sys.maxsize
        for c in range(self.numCity):
            newTour = self.new_alter_tour(self.nn_tour(c))
            newCost = self.tour_cost(newTour)
            if newCost < curCost:
                curTour, curCost = newTour, newCost
        return curTour, curCost
        

    def swap_if_better(self, tour, i, j):
        """
        Swap two cities in a tour
        """
        new_tour = tour[:]
        temp, new_tour[i] = tour[i], tour[j]
        new_tour[j] = temp
        if not self.is_valid_tour(new_tour):
            return
        if self.tour_cost(new_tour) < self.tour_cost(tour):
            temp, tour[i] = tour[i], tour[j]
            tour[j] = temp
        return

    @property
    def swap_combinations(self):
        if not self._swap_combinations:
            self._swap_combinations = list(combinations(range(self.numCity - 1), 2))
        return self._swap_combinations

    def improve_by_swap(self, tour):
        """
        try to improve a tour by swap two cities.
        """
        for (i, j) in self.swap_combinations:
            self.swap_if_better(tour, i, j)
        return tour

    def improve_by_reversal(self, tour):
        """
        try to improve a tour by section reversal.
        """
        for (i, j) in self.all_segments:
            self.reverse_segment_if_better(tour, i, j)
        return tour
        
    def hill_climbing(self, n):
        """                                                                     
        Use hill climbing strategy with on N random tours
        """

        curTour, curCost = [], sys.maxsize
        for _ in range(n):
            newTour = self.new_alter_tour(self.random_alternating_tour())
            newCost = self.tour_cost(newTour)
            if newCost < curCost:
                curTour, curCost = newTour, newCost
        return curTour, curCost

            
    def reverse_segment_if_better(self, tour, i, j):
        """
        Reverse the tour[i:j] if it renders a shorter tour.
        
        """
        new_tour = copy(tour)
        new_tour[i:j] = reversed(new_tour[i:j])
        if not self.is_valid_tour(new_tour):
            return
        a, b, c, d = tour[i-1], tour[i], tour[j-1], tour[j]
        
        if self.distMatr[a][b] + self.distMatr[c][d] > \
                self.distMatr[a][c] + self.distMatr[b][d]:
            tour[i:j] = reversed(tour[i:j])

    def alter_tour(self, tour, method = 'reverse'):
        """
        
        """
        originalCost = self.tour_cost(tour)
        if method == 'reverse':
            for (start, end) in self.all_segments:
                self.reverse_segment_if_better(tour, start, end)
            if self.tour_cost(tour) < originalCost:
                return self.alter_tour(tour, 'reverse')
            return tour
        if method == 'swap':
            for (i, j) in self.swap_combinations:
                self.swap_if_better(tour, i, j)
            if self.tour_cost(tour) < originalCost:
                return self.alter_tour(tour, 'swap')
            return tour

    def new_alter_tour(self, tour):
        """
        check both section reversal and city swapping
        """
        originalCost = self.tour_cost(tour)
        for (i, j) in self.all_segments:
            self.reverse_segment_if_better(tour, i, j)
        for (i, j) in self.swap_combinations:
            self.swap_if_better(tour, i, j)
        if self.tour_cost(tour) < originalCost:
            return self.new_alter_tour(tour)
        return tour
    
