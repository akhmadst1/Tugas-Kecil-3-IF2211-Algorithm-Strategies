from classes import Graph, Node
from astar import Astar
from ucs import UCS
import sys
import time

# graph initializer from file.txt
def initializeGraph(filename):
    text = filename.read().splitlines()
    nodeCount = int(text[0])
    if (nodeCount < 8):
        print("Please fix your file, the nodes must be greater or equal than 8")
        sys.exit()
    nodes = text[1:nodeCount+1]
    fileMatrix = text[nodeCount+1:]
    adjacencyMatrix = [[0 for i in range(nodeCount)] for j in range(nodeCount)]

    # input searching method
    while True:
        method = input("Input Method (ucs/astar): ")
        if method.lower() == "ucs":
            method = "ucs"
            break
        elif method.lower() == "astar":
            method = "astar"
            break
        else:
            print("Invalid Method!")

    graph = Graph(nodeCount)
    # add node from file.txt
    for i in range(nodeCount):
        splitString = nodes[i].split(" ", 2)
        newNode = Node(float(splitString[0]), float(splitString[1]), splitString[2])
        graph.addNode(newNode)
        adjacencyMatrix[i] = [int(x) for x in fileMatrix[i].split(" ")]
    graph.addEdges(adjacencyMatrix)
    return graph, method

# lat and long getter
def solveGraph(graph):
    latitude = []
    longitude = []
    for i in range(len(graph.graphNodes)):
        latitude.append(graph.graphNodes[i].latitude)
        longitude.append(graph.graphNodes[i].longitude)
    return latitude, longitude

# neighbor solver
def solveNeighbor(graph):
    arrDict = []
    nodes = graph.graphNodes
    for i in range(len(nodes)):
        arrDict.append({
            'latitude': nodes[i].latitude,
            'longitude': nodes[i].longitude,
            'neighbor': []
        })
        for j in range(len(nodes[i].neighbors)):
            arrDict[i]['neighbor'].append({
                'latitude': nodes[i].neighbors[j].latitude,
                'longitude': nodes[i].neighbors[j].longitude
            })
    return arrDict

# path solver
def solvePath(path):
    name = []
    latitude = []
    longitude = []
    for i in range(len(path)):
        name.append(path[i].name)
        latitude.append(path[i].latitude)
        longitude.append(path[i].longitude)
    # get names
    node = dict(enumerate(name))
    names = []
    names.append(node)
    # get latitudes
    lat = dict(enumerate(latitude))
    latitudes = []
    latitudes.append(lat)
    # get longitudes
    long = dict(enumerate(longitude))
    longitudes = []
    longitudes.append(long)
    return names, latitudes, longitudes

def main(graph, method):
    print("Input location")
    start = None
    goal = None
    while start == None or goal == None:
        # get start node
        while start == None:
            startNode = input("Input Start: ")
            start = graph.findNode(startNode)
            if (start == None):
                print("Invalid Location! Try Again")
                print()
        # get goal node
        while goal == None:
            goalNode = input("Input Goal: ")
            goal = graph.findNode(goalNode)
            if (goal == None):
                print("Invalid Location! Try Again")
                print()

    # using ucs alogrithm
    if method == "ucs":
        startTime = time.time()
        ucs = UCS(graph, start, goal)
        explored, totalCost = ucs.solve()
        if (len(explored) == 0):
            path = []
            distance = 0
        else:
            path = ucs.getPath()
            distance = totalCost[goal]
        endTime = time.time()

    # using astar algorithm
    else:
        startTime = time.time()
        astar = Astar(graph, start, goal)
        explored, totalCost = astar.solve()
        if (len(explored) == 0):
            path = []
            distance = 0
        else:
            path = astar.getPath()
            distance = totalCost[goal]
        endTime = time.time()
    execTime = endTime - startTime
    return start, goal, path, distance, execTime
