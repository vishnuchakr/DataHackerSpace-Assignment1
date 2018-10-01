#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import math
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
    dims = points.shape
    returnArr = []
    
    for i in range(0, dims[1]):
        vec = np.transpose(np.matrix(points[:, i]))
        vec[1] = 2 - vec[1]
        
        rotMat = np.array([[0, -1], [1, 0]])
        vec = np.matmul(rotMat, vec)
        
        projMat = np.array([[1, 3], [3, 9]])
        projMat = (1/10) * projMat
        vec = np.matmul(projMat, vec)
        vec = np.transpose(vec)
        
        returnArr.append(vec)
        
    return np.transpose(np.concatenate(returnArr))
    
def normalize(image):
    image = np.array(image)
    max = np.amax(image)
    min = np.amin(image)
    scalar = 255 / (max - min)
    for arr in image:
        for pixel in arr:
            pixel = scalar * (pixel - min)
    
    return image

def sigmoid_normalize(image, a):
    image = np.array(image)
    
    for arr in image:
        for pixel in arr:
            base = 1 + math.exp((-a ** -1) * (pixel - 128))
            pixel = 255 * (base ** -1)
    
    return image
