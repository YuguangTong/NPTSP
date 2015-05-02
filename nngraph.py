from random import randint
from copy import copy

class Graph(object):
    """
    Graph representing cities.
    """
    # assume distMatr is a 2d python list

    def __init__(self, distMatr, colorList, numCity):
        self._distMatr = distMatr
        self._colorList = colorList 
        self._numCity = numCity
        assert len(self._distMatr) == numCity
        self._rSet = set()
        self._bSet = set()
        for c in range(self._numCity):
            if colorList[c] == 'R':
                self._rSet.add(c)
            else:
                self._bSet.add(c)

    def tour_cost(self, tour):
        assert len(tour) == self._numCity
        cost = 0
        for i in range(self._numCity - 1):
            cost += self._distMatr[tour[i]][tour[i+1]]
        return cost
    
    # class method to remove a red(blue) CITY from RSET (BSET)
    @staticmethod
    def remove_city(rset, bset, city, color):
        if color == 'R':
            rset.remove(city)
        else:
            bset.remove(city)
        return
    
    @staticmethod
    def opposite_color(color):
        if color == 'R':
            return 'B'
        return 'R'

    def alternate_color(self, unvistR, unvistB, curCity):
        """
        Assume visit in alternating color and
        return the nearest neighboring city of the opposite color to visit.. 

        """
        if self._colorList[curCity] == 'R':
            nextCity = min(unvistB, key = lambda c: self._distMatr[c][curCity])
        else:
            nextCity = min(unvistR, key = lambda c: self._distMatr[c][curCity])
        return nextCity

    # return a nearest neighbor tour starting from START
    def nn_tour(self, start = 0):
        unvistRed, unvistBlue = copy(self._rSet), copy(self._bSet)
        tour = [start]
        self.remove_city(unvistRed, unvistBlue, start, self._colorList[start])
        while unvistRed or unvistBlue:
            curCity = tour[-1]
            nextCity = self.alternate_color(unvistRed, unvistBlue, curCity)
            tour.append(nextCity)
            self.remove_city(unvistRed, unvistBlue, nextCity, self._colorList[nextCity])
        return tour
    
    def nn_best(self):
        curTour, curCost = [], 50000 
        for c in range(self._numCity):
            newTour = self.nn_tour(c)
            newCost = self.tour_cost(newTour)
            if newCost < curCost:
                curTour, curCost = newTour, newCost
        return curTour, curCost

