# A* method for finding shortest path
class Astar:
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal
        self.frontier = PriorityQueue()
        self.initialPlace = {self.start: None}
        self.totalCost = {self.start: 0}

    def solve(self):
        self.start.f = 0 + haversine(self.start, self.goal)
        self.frontier.insert(self.start)
        while not self.frontier.empty():
            current = self.frontier.pop()
            if current == self.goal:
                break
            for neighbour in current.neighbour:
                new_cost = self.totalCost[current] + haversine(current, neighbour)
                if neighbour not in self.totalCost or new_cost < self.totalCost[neighbour]:
                    self.totalCost[neighbour] = new_cost
                    neighbour.f = new_cost + haversine(neighbour, self.goal)
                    self.frontier.insert(neighbour)
                    self.initialPlace[neighbour] = current
        if (self.goal not in self.initialPlace):
            self.initialPlace = {}
        return self.initialPlace, self.totalCost
    
    def get_path(self):
        current = self.goal
        path = [current]
        while current != self.start:
            current = self.initialPlace[current]
            path.append(current)
        path.reverse()
        return path