from math import *
from classes import PriorityQueue

# find the distance on actual earth (distance on sphere)
# earth radius is approximately 6371 km
def haversine(node1, node2, radius = 6371):
    lat1 = radians(node1.latitude)
    lat2 = radians(node2.latitude)
    dLat = radians(lat2 - lat1)
    dLon = radians(node2.longitude - node1.longitude)
    a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
    c = 2*asin(sqrt(a))
    distance = radius * c
    return distance

# A* search algorithm
class Astar:
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal
        self.explored = {self.start: None} # dictionary for explored node
        self.totalCost = {self.start: 0} # dictionary for the total cost of explored node
        self.toVisit = PriorityQueue()
    
    def solve(self):
        # heuristic cost from start to goal node
        self.start.cost = 0 + haversine(self.start, self.goal)
        self.toVisit.enqueue(self.start)
        while not self.toVisit.isEmpty(): # search until empty or reach the goal node
            current = self.toVisit.dequeue()
            if current == self.goal:
                break
            for neighbor in current.neighbors:
                newCost = self.totalCost[current] + haversine(current, neighbor)
                # update the node with lowest cost
                if (neighbor not in self.totalCost) or (newCost < self.totalCost[neighbor]):
                    self.totalCost[neighbor] = newCost
                    neighbor.cost = newCost + haversine(neighbor, self.goal)
                    self.toVisit.enqueue(neighbor)
                    self.explored[neighbor] = current

        # if goal node is not found, return empty
        if (self.goal not in self.explored):
            self.explored = {}
        
        # return node and total cost
        return self.explored, self.totalCost
    
    def getPath(self):
        current = self.goal
        path = [current]
        while current != self.start:
            current = self.explored[current]
            path.append(current)
        
        # get the path from start to goal
        path.reverse()
        return path
    