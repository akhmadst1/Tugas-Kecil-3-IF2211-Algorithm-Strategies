from utility import *
from classes import *
from astar import Astar
from ucs import UCS
from flask import Flask, render_template
import json
from flask.json import jsonify

app = Flask(__name__)
# file input validation
while True:
    filename = input("Input filename: ")
    try:
        file = open("test/" + filename)
        break
    except FileNotFoundError:
        print("File Not Found!")

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

graph = initializeGraph(file)
graph.printGraph()

# Flask
@app.route("/get-data")
def getData():
    arrDict = solveNeighbor(graph)
    return jsonify(arrDict = arrDict)

@app.route("/")
def init():
    start, goal, path, distance = main(graph, method)
    dict, lat, long = solvePath(path)
    marklat, marklong = solveGraph(graph)
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
        slat = startLatitude,
        slong = startLongitude,
        dlat = goalLatitude,
        dlong = goalLongitude,
        spath = solution,
        latss = latitudes,
        longss = longitudes,
        sspath = paths,
        dist = distance,
        marklat = marklat,
        marklong = marklong)