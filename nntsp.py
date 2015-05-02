import numpy as np
from random import randint
from copy import copy

class Graph(object):
    """
    Graph representing cities.
    """
    # assume distMatr is a 2d python list
    def __init__(self, distMatr, colorList):
        self._distMatr = distMatr
        self._colorList = colorList 
        self._numCity = len(colorList)
        self._rSet = set()
        self._bSet = set()
        for c in range(self._size):
            if colorList[c] == 'R':
                self._rSet.add(c)
            else:
                self._bSet.add(c)

    def tour_cost(self, tour):
        assert len(tour) = self.numCity - 1
        cost = 0
        for i in range(self.numCity - 1):
            cost += self.distMatr[tour[i]][tour[i+1]]
        return cost
    
    # class method to remove a red(blue) CITY from RSET (BSET)
    def remove_city(rset, bset, city, color):
        if color = 'R':
            rset.remove(city)
        else:
            bset.remove(city)
        return
    
    def opposite_color(color):
        if color == 'R':
            return 'B'
        return 'R'

    # return a nearest neighbor tour starting from START
    def nn_tour(self, start = 0):
        unvistRed, unvistBlue = copy(self._rSet), copy(self._bSet)
        tour = [start]
        Graph.remove_city(unvistRed, unvistBlue, first, self._colorList[start])
        while unvistRed or unvistBlue:
            

