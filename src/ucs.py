from utility import *

# Uniform-Cost-Search (UCS) algorithm
class UCS:
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal
        self.explored = {self.start: None} # dictionary for explored node
        self.totalCost = {self.start: 0} # dictionary for the total cost of explored node
        self.toVisit = PriorityQueue()
    
    def solve(self):
        # cost without heuristic
        self.start.cost = 0
        self.toVisit.enqueue(self.start)
        while not self.toVisit.isEmpty(): # search until empty or reach the goal node
            current = self.toVisit.dequeue()
            if current == self.goal:
                break
            for neighbor in current.neighbors:
                newCost = self.totalCost[current]
                # update the node with lowest cost
                if neighbor not in self.totalCost or newCost < self.totalCost[neighbor]:
                    self.totalCost[neighbor] = newCost
                    neighbor.cost = newCost
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
    