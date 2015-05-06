from random import randint
from copy import copy
import sys
from nptspGraph import nptspGraph

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
        nptspGraph(distMatr, colorList, numCity)

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

    def nn_tour(self, start = 0):
        """
        Return a nearest neighbor tour starting from START
        """
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
        """
        Return the shortest nearest-neighbor tour starting from any node.
        """
        curTour, curCost = [], sys.maxsize 
        for c in range(self._numCity):
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
        for c in range(self._numCity):
            newTour = self.alter_tour(self.nn_tour(c))
            newCost = self.tour_cost(newTour)
            if newCost < curCost:
                curTour, curCost = newTour, newCost
        return curTour, curCost
            
    def reverse_segment_if_better(self, tour, i, j):
        """
        Reverse the tour[i:j] if it renders a shorter tour.
        
        """
        if not self.check_reversed_tour_1(tour, i, j):
            return

        a, b, c, d = tour[i-1], tour[i], tour[j-1], tour[j]
        
        if self._distMatr[a][b] + self._distMatr[c][d] > \
                self._distMatr[a][c] + self._distMatr[b][d]:
            tour[i:j] = reversed(tour[i:j])

    def check_tour(self, tour):
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

    def check_reversed_tour_1(self, tour, i, j):
        """
        Naive implementation to check if TOUR is still valid
        after tour[i:j] is reversed. May not be efficient enough.
        """
        new_tour = copy(tour)
        new_tour[i:j] = reversed(new_tour[i:j])
        count = 0
        prev = 'X'
        for k in range(self._numCity):
            cur = self._colorList[new_tour[k]]
            if cur == prev:
                count += 1
                if count > 3:
                    return False
            else:
                prev = cur
                count = 1
        return True
        
    
    def check_reversed_tour_2(self, tour, i, j):
        """
        Check if the TOUR satisfies the color constraint
        after revese TOUR[i:j]
        Return True iff the reversed TOUR is valid
        A faster version than check_reversed_tour_1. But seems not necessary.

        """
        #print(tour)
        #print(''.join([self._colorList[l] for l in tour]))
        a, b, c, d = tour[i-1], tour[i], tour[j-1], tour[j]
        acleft, acright = tour[max(0, i-3) : i], tour[j-1: j+2]
        bdleft, bdright = tour[i: i-3: -1], tour[j: j+3]
        ac, bd = acleft + acright, bdleft + bdright
        
        for segment in [ac, bd]:
            count = 0
            prev = 'X'
            for k in segment:
                cur = self._colorList[tour[k]]
                if cur == prev:
                    count += 1
                    if count > 3:
                        return False
                else:
                    prev = cur
                    count = 1
        return True


    def alter_tour(self, tour):
        """
        
        """
        originalCost = self.tour_cost(tour)
        for (start, end) in self.all_segments:
            self.reverse_segment_if_better(tour, start, end)
        if self.tour_cost(tour) < originalCost:
            return self.alter_tour(tour)
        return tour

    @property
    def all_segments(self):
        """
        Return (start, end) pairs of indices that form segment of tours

        """
        return [(start, start + length)
                for length in range(2, self._numCity-2)
                for start in range(1, self._numCity - length)]
        
    
