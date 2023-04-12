class PriorityQueue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    # dequeue with the lowest cost priority
    def dequeue(self):
        minIdx = 0
        for i in range(len(self.queue)):
            if self.queue[i].cost < self.queue[minIdx].cost:
                minIdx = i
        val = self.queue.pop(minIdx)
        return val

class Graph(object):
    def __init__(self, nodeCount):
        self.nodeCount = nodeCount
        self.graphNodes = []

    def addNode(self, node):
        self.graphNodes.append(node)

    def printGraph(self):
        print("List of nodes:")
        for node in self.graphNodes:
            node.printNode()
            print()

    def addEdges(self, adjacencyMatrix):
        for i in range(self.nodeCount):
            for j in range(self.nodeCount):
                if adjacencyMatrix[i][j] != 0:
                    self.graphNodes[i].addNeighbor(self.graphNodes[j])

    def findNode(self, nodeName):
        for node in self.graphNodes:
            if node.name == nodeName:
                return node

class Node(object):
    def __init__(self, lat, long, name):
        self.latitude = lat
        self.longitude = long
        self.name = name
        self.cost = 0
        self.neighbors = []

    def getLatitude(self):
        return self.latitude

    def getLongitude(self):
        return self.longitude

    def printNode(self):
        print("Name:", self.name)
        print("Latitude:", self.latitude)
        print("Longitude:", self.longitude)
        print("Neighbors: ", end="")
        for i, neighbor in enumerate(self.neighbors):
            if i == len(self.neighbors) - 1:
                print(neighbor.name)
            else:
                print(neighbor.name, end=", ")

    def addNeighbor(self, node):
        self.neighbors.append(node)
