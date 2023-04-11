from math import *
from classes import *

# find the distance on actual earth (distance on sphere)
# earth radius is approximately 6371 km
def haversine(node1, node2, radius = 6371):
    lat1 = radians(node1.getLatitude())
    lat2 = radians(node2.getLatitude())
    dLat = radians(lat2 - lat1)
    dLon = radians(node2.getLongitude() - node1.getLongitude())

    a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
    c = 2*asin(sqrt(a))
    
    distance = radius * c
    return distance

# graph initializer from file.txt
def initializeGraph(filename):
    text = filename.read().splitlines()
    nodeCount = int(text[0])
    nodes = text[1:nodeCount+1]
    fileMatrix = text[nodeCount+1:]
    adjacencyMatrix = [[0 for i in range(nodeCount)] for j in range(nodeCount)]

    graph = Graph(nodeCount)
    # add node from file.txt
    for i in range(nodeCount):
        splitString = nodes[i].split(" ", 2)
        newNode = Node(float(splitString[0]), float(splitString[1]), splitString[2])
        graph.addNode(newNode)
        adjacencyMatrix[i] = [int(x) for x in fileMatrix[i].split(" ")]
    graph.addEdges(adjacencyMatrix)
    return graph

# lat and long getter
def solveGraph(graph):
    latitude = []
    longitude = []
    for i in range(len(graph.graphNodes)):
        latitude.append(graph.graphNodes[i].getLatitude())
        longitude.append(graph.graphNodes[i].getLongitude())
    return latitude, longitude

# neighbor solver
def solveNeighbor(graph):
    arrDict = []
    nodes = graph.graphNodes
    for i in range(len(nodes)):
        arrDict.append({
            'latitude': nodes[i].getLatitude(),
            'longitude': nodes[i].getLongitude(),
            'neighbor': []
        })
        for j in range(len(nodes[i].neighbor)):
            arrDict[i]['neighbor'].append({
                'latitude': nodes[i].neighbor[j].getLatitude(),
                'longitude': nodes[i].neighbor[j].getLongitude()
            })
    return arrDict

# path solver
def solvePath(path):
    name = []
    latitude = []
    longitude = []
    for i in range(len(path)):
        name.append(path[i].name)
        latitude.append(path[i].getLatitude())
        longitude.append(path[i].getLongitude())
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
