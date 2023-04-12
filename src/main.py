import json
import sys
from utility import *
from classes import *
from astar import Astar
from ucs import UCS
from flask import Flask, render_template
from flask.json import jsonify

app = Flask(__name__)
# file input validation
while True:
    filename = input("Input filename: ")
    try:
        file = open("test/" + filename)
        break
    except FileNotFoundError:
        print("File Not Found!\n")

graph, method = initializeGraph(file)
graph.printGraph()

while True:
    visualize = input("Visualize the solution with google maps API? (y/n): ")
    if visualize.lower() == "n" or visualize.lower() == "no":
         printSolution(graph, method)
         sys.exit()
    elif visualize.lower() == "y" or visualize.lower() == "yes":
        print("Run http://127.0.0.1:5000 in your local browser, then enter start and goal node")
        print()
        break
    else:
        print("Invalid Input!\n")

# Flask
@app.route("/get-data")
def getData():
    arrDict = solveNeighbor(graph)
    return jsonify(arrDict = arrDict)

@app.route("/")
def init():
    start, goal, path, distance = main(graph, method)
    dict, lat, long = solvePath(path)
    markLatitude, markLongitude = solveGraph(graph)
    solution = json.dumps(dict)
    latitudes = json.dumps(lat)
    longitudes = json.dumps(long)
    startLatitude = start.latitude
    startLongitude = start.longitude
    goalLatitude = goal.latitude
    goalLongitude = goal.longitude
    paths = path
    return render_template(
        'visualization.html',
        method = method.upper(),
        startLat = startLatitude,
        startLong = startLongitude,
        goalLat = goalLatitude,
        goalLong = goalLongitude,
        solution = solution,
        solutionPath = paths,
        latitudes = latitudes,
        longitudes = longitudes,
        markLatitude = markLatitude,
        markLongitude = markLongitude,
        dist = round(distance*1000, 3))