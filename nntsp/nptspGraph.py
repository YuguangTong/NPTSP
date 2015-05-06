from random import shuffle
from itertools import combinations

class nptspGraph(object):
    """
    Super class of any nptsp Graphs

    A subclass would correspond to an algorithm. 
    """
    def __init__(self, distMatr, colorList, numCity):
        """
        Initiator
        distMatr: a python list representing a symmetric distance matrix.
        colorList: a string consisting only 'R' and 'B'
        numCity: number of nodes in the graph

        """
        assert len(distMatr) == numCity
        assert len(colorList) == numCity
        self.distMatr = distMatr
        self.colorList = colorList 
        self.numCity = numCity
        _rs = []
        _bs = []
        for c in range(self.numCity):
            if colorList[c] == 'R':
                _rs += [c]
            else:
                _bs += [c]
        self.redSet = frozenset(_rs)
        self.blueSet = frozenset(_bs)
        self.unvisitedRed = None
        self.unvisitedBlue = None
        self._segments = None

    def tour_cost(self, tour):
        """
        Calculate the cost of the TOUR
        """
        assert len(tour) == self.numCity
        cost = 0
        for i in range(self.numCity - 1):
            cost += self.distMatr[tour[i]][tour[i+1]]
        return cost
    
    def search_init(self):
        """
        Initialization before a tour search by set up
        unvisitedRed and unvisitedBlue.
        """
        self.unvisitedRed, self.unvistedBlue = set(self.redSet), set(self.blueSet)

    def visit_city(city):
        """
        In contruction of a tour:
        remove a red(blue) CITY from unvisitedRed (unvisitedBlue)
        """
        if city not in self.unvisitedRed and \
                city not in self.unvisitedBlue:
            raise Exception('Error: Invalid city to visit')
        if color == 'R':
            self.unvisitedRed.remove(city)
        else:
            self.unvisitedBlue.remove(city)
        return
    
    def is_valid_tour(self, tour):
        """
        Check if TOUR satisfies color constraints in NNTSP
        """
        count = 0
        prev = 'X'
        for k in range(self.numCity):
            cur = self.colorList[tour[k]]
            if cur == prev:
                count += 1
                if count > 3:
                    return False
            else:
                prev = cur
                count = 1
        return True

    def random_alternating_tour(self):
        """
        Generate a random tour in the form of "RBRBRB..."
        """
        rlist = list(self.redSet)
        blist = list(self.blueSet)
        shuffle(rlist)
        shuffle(blist)
        tour = list(range(self.numCity))
        tour[::2] = rlist
        tour[1::2] = blist
        return tour

    @property
    def all_segments(self):
        """
        return all (start, end) pairs that specify segments of tours.
        """
        if self._segments:
            return self.segments
        return [(start, start + length)
                for length in range(2, self._numCity-2)
                for start in range(1, self._numCity - length)]


        
    def random_tour(self):
        """
        Generate a completely (pseudo) random tour
        """
        while True:
            tour = list(range(self.numCity))
            shuffle(tour)
            if self.is_valid_tour(tour):
                return tour

    def get_color(self, tour):
        """
        Return the color list of the TOUR
        """
        assert len(tour) == self.numCity
        return [self.colorList[c] for c in tour]
