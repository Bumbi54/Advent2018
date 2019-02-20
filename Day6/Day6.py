import re
from collections import Counter

def readInput(fileName):
    """
    Read input file and parse it into a list
    :param fileName: name of input file
    :return: list of input file content (each line is new element)
    """
    with open(fileName, 'r') as file:

        fileContent = []
        for line in file:
            coordinates = line.strip("\n").split(",")
            fileContent.append( (int(coordinates[1]) , int(coordinates[0]) ) )

        return fileContent

def calculateBestPoint(list_Points):
    '''
    Calculate which non infinitive point has the most locations closes to it
    :param list_Points: list of points 
    :return: number of locations closes to each point
    '''

    #for the size of grid
    maximumXcoordinate = 0
    maximumYcoordinate = 0

    #create dictinary that will count location closes to point. Starts with 1 since point is also a location. Also find maximum coordinates that represent size of grid.
    pointDictionary = {}
    infinitivePoints = set()
    for point in list_Points:
        pointDictionary[point] = 1

        if maximumXcoordinate < point[0]:
            maximumXcoordinate = point[0]

        if maximumYcoordinate < point[1]:
            maximumYcoordinate = point[1]

    print(f"Size of grid: ({maximumXcoordinate},{maximumYcoordinate})")
    #iterate over all of the grid locations
    for coordinateX in range(maximumXcoordinate + 1):
        for coordinateY in range(maximumYcoordinate + 1):

            #don't calculate distance for the point themself
            if (coordinateX, coordinateY) not in list_Points:
                distanceToPoint = {}

                for point in list_Points:
                    distanceToPoint[point] = abs(point[0] - coordinateX) + abs(point[1] - coordinateY)
                    #print(f"point[0]: {point[0]}, coordinateX: {coordinateX}, point[1]: {point[1]}, coordinateY:{coordinateY}, distance: {distanceToPoint[point]}")

                #print(f"Cuerent location: ({coordinateX},{coordinateY}). Distances: {distanceToPoint}")

                min = [0, 0]
                for point,distance in distanceToPoint.items():

                    if min[1] > distance or min[0] == 0:
                        min[1] = distance
                        min[0] = point

                #only increment if there is one such distance
                if Counter(distanceToPoint.values())[min[1]] == 1:
                    pointDictionary[min[0]] += 1

                    if (coordinateX == 0) or (coordinateX == maximumXcoordinate ) or (coordinateY == 0) or (coordinateY == maximumYcoordinate ):
                        #print(f"Cuerent location: ({coordinateX},{coordinateY}). Currnet value: {min[0]}")
                        infinitivePoints.add(min[0])
                #else:
                #    print(f"Conflict. Cuerent location: ({coordinateX},{coordinateY}). Currnet value: {min[0]}")

                #print(f"Closes point is: {min[0]}, with distance: min[1]")

    print("InfinitivePoints %s " % infinitivePoints)
    for point in infinitivePoints:
        del pointDictionary[point]
    return pointDictionary


def secondPart(list_Points):
    '''
    Calculate second part of task
    :param list_Points: list of points 
    :return: size of region
    '''

    #for the size of grid
    maximumXcoordinate = 0
    maximumYcoordinate = 0

    regionSize = 0

    for point in list_Points:

        if maximumXcoordinate < point[0]:
            maximumXcoordinate = point[0]

        if maximumYcoordinate < point[1]:
            maximumYcoordinate = point[1]

    print(f"Size of grid: ({maximumXcoordinate},{maximumYcoordinate})")
    #iterate over all of the grid locations
    for coordinateX in range(maximumXcoordinate + 1):
        for coordinateY in range(maximumYcoordinate + 1):

            totalDistance = 0

            for point in list_Points:
                totalDistance = totalDistance +  abs(point[0] - coordinateX) + abs(point[1] - coordinateY)

            if totalDistance < 10000:
                regionSize += 1

    return regionSize

if __name__ == '__main__':

    list_Points = readInput("input.txt")
    print(list_Points)

    result = calculateBestPoint(list_Points)

    print(result)
    print(max(result.values()))

    result = secondPart(list_Points)
    print(result)
