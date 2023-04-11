from classes import Graph, Node
from astar import Astar
from ucs import UCS

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

# def main(graph):
#     print("Input location")
#     start = None
#     goal = None

#     while start == None or goal == None:
#         while start == None:
#             startNode = input("Input Start: ")
#             start = graph.findNode(startNode)
#             # if (start == None):
#             #     print("Invalid Location! Try Again")
#             #     print()
        
#         while goal == None:
#             goalNode = input("Input Goal: ")
#             goal = graph.findNode(goalNode)
#             # if (goal == None):
#             #     print("Invalid Location! Try Again")
#             #     print()
#     astar = Astar(graph, start, goal)
#     came_from, total_cost = astar.solve()

#     if (len(came_from) == 0):
#         path = []
#         distance = 0
#     else:
#         path = astar.get_path()
#         distance = total_cost[goal]

#     return start, goal, path, distance 

def main(graph):
    # Input Lokasi
    print("Masukkan rute lokasi yang ingin dicari:")
    start = None
    goal = None

    while start == None or goal == None:
        start_node = input("Masukkan lokasi awal: ")
        start = graph.findNode(start_node)
        goal_node = input("Masukkan lokasi tujuan: ")
        goal = graph.findNode(goal_node)
        if (start == None or start == None):
            print("Masukkan tujuan lagi! Node tidak ditemukan")
        print()

    # Penghitungan path yang benar
    astar = Astar(graph, start, goal)
    came_from, total_cost = astar.solve()

    if (len(came_from) == 0):
        path = []
        distance = 0
    else:
        path = astar.get_path()
        distance = total_cost[goal]

    return start, goal, path, distance 