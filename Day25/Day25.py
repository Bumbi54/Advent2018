import re
from collections import deque
from copy import copy, deepcopy
import time

import math



def readInput(fileName):
    """
    Read input file and parse it into a string
    :param fileName: name of input file
    :return: list of input file content (each line is new element)
    """
    with open(fileName, 'r') as file:

        fileContent = file.read()

        return fileContent.split("\n")

def calculateConstellation(parsedInput):
    '''
    
    :param parsedInput: 
    :return: 
    '''

    constellationList = []

    for point in parsedInput:

        print(f"point: {point}")
        if not constellationList:
            constellationList.append([point])

        else:
            possibleConstellation = []
            possibleConstellationIndex = []

            for index, constellation in enumerate(constellationList):

                for constellationPoint in constellation:

                    if abs(constellationPoint[0] - point[0]) + abs(constellationPoint[1] - point[1]) + abs(constellationPoint[2] - point[2]) + abs(constellationPoint[3] - point[3]) <= 3:
                        possibleConstellation.append(constellation)
                        possibleConstellationIndex.append(index)
                        possibleConstellationIndex = sorted(list(set(possibleConstellationIndex)))
                        break

                #print(f"I ma out: {point} {index}, {constellation}, {constellationList}")

            #print(f"possibleConstellation: {possibleConstellation}")
            if len(possibleConstellation) == 1:
                possibleConstellation[0].append(point)

            elif len(possibleConstellation) == 1:
                constellationList.append([point])

            else:
                mergedConstellation =[]
                for constellation in possibleConstellation:
                    mergedConstellation += constellation

                mergedConstellation += [point]
                constellationList.append(mergedConstellation)

                #print(f"possibleConstellationIndex: {possibleConstellationIndex}")
                for index in reversed(possibleConstellationIndex):
                    constellationList.pop(index)

        #print(f"Point: {point} constellationList: {constellationList}")

    print(f"Number of constellations: {len(constellationList)}")


if __name__ == "__main__":


    inputList = readInput("input.txt")
    print(inputList)

    parsedInput = [(int(line.split(",")[0]), int(line.split(",")[1]), int(line.split(",")[2]), int(line.split(",")[3])  ) for line in inputList ]

    print(parsedInput)

    calculateConstellation(parsedInput)
