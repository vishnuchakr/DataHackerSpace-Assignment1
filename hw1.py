#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np

def histogram_times(filename):
    crashCount = [0] * 24
    with open (filename) as f:
        csvReader = csv.reader(f)
        airplaneData = list(csvReader)
    
    for i in range(0, len(airplaneData)):
        time = airplaneData[i][1]
        check = False
        hour = 0
        try:
            hour = int(time.split(':')[0])
            check = True
        except:
            check = False
        if check and hour <= 24:
            crashCount[hour] += 1
         
    return crashCount
        
def weigh_pokemons(filename, weight):
    pokemon = []
    dict = None
    with open(filename, 'r') as f:
        dict = json.load(f)
    
    for i in dict["pokemon"]:
        check = False
        w = 0.0
        try:
            w = float(i["weight"].split(" ")[0])
            check = True
        except:
            check = False
        
        if check and w == weight:
            pokemon.append(i["name"])

    return pokemon
    
def single_type_candy_count(filename):
    dict = None
    candy = 0
    with open(filename, 'r') as f:
        dict = json.load(f)
    for i in dict["pokemon"]:
        if len(i["type"]) == 1:
            try:
                candy += int(i["candy_count"])
            except:
                candy = candy

    return candy

def reflections_and_projections(points):
    points = np.array(points)
    #reflects over y = 1
    for i in range(0, len(points[1])):
        points[1][i] =  points[1][i] * -1 + 2
    
            
    #rotates by pi/2 radians
    for i in range(0, len(points[0])):
        points[0][i] = points[0][i] * -1
    
    for i in range(0, len(points[1])):
        points[1][i] = points[1][i] * -1
    
    #projects the point onto y = 3x
    

    print(points)

    
def normalize(image):
    pass

def sigmoid_normalize(image):
    pass

histogram_times('airplane_crashes.csv')
weigh_pokemons("pokedex.json", 10.0)
single_type_candy_count("pokedex.json")
reflections_and_projections([[1.32,5.57,3.01,6.34],[5.12,7.92,3.41,9.70]])