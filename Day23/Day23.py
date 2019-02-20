import re
import time
import networkx as nx


def readInput(fileName):
    """
    Read input file and parse it into a string
    :param fileName: name of input file
    :return: list of input file content (each line is new element)
    """
    with open(fileName, 'r') as file:

        fileContent = file.read()

        return fileContent.split("\n")

def parseInput(inputList):
    '''
    
    :param inputList: 
    :return: 
    '''

    positionDictinary = {}
    for line in inputList:
        m = re.search("pos=<([-]?\d+),([-]?\d+),([-]?\d+)>, r=(\d+)", line)
        positionDictinary[(int(m.group(1)), int(m.group(2)), int(m.group(3)))] = int(m.group(4))

    return positionDictinary

def largestNonobot(positionDictinary):
    '''
    
    :param positionDictinary: 
    :return: 
    '''

    largestNanoBotRadius = 0
    largestNanoBotKey = (0, 0, 0)

    for key, value in positionDictinary.items():

        if value > largestNanoBotRadius:
            largestNanoBotRadius = value
            largestNanoBotKey = key

    print(f"Bot: {largestNanoBotKey} with radius: {largestNanoBotRadius}")

    count = 0
    for nanoBot in positionDictinary.keys():

        distance = abs(nanoBot[0] - largestNanoBotKey[0]) + abs(nanoBot[1] - largestNanoBotKey[1]) + abs(nanoBot[2] - largestNanoBotKey[2])

        if distance <= largestNanoBotRadius:
            count += 1

    print(f"Bot: {largestNanoBotKey} with radius: {largestNanoBotRadius}. Bots in range: {count}")


def mostNonobots(positionDictinary):
    '''

    :param positionDictinary: 
    :return: 
    '''

    largestNanoBotRadius = 0
    largestNanoBotKey = (0, 0, 0)

    for key, value in positionDictinary.items():

        if value > largestNanoBotRadius:
            largestNanoBotRadius = value
            largestNanoBotKey = key

    modifier = 10000000
    oldCountCoordinate = (0, 0, 0)
    while(modifier >= 1):
        maxCount = 0
        maxCountCoordinate = (0, 0, 0)

        print(oldCountCoordinate)
        for x in range(oldCountCoordinate[0] , oldCountCoordinate[0]  + 10):
            for y in range(oldCountCoordinate[1] , oldCountCoordinate[1]  + 10):
                for z in range(oldCountCoordinate[2] , oldCountCoordinate[2]  + 10):
                    count = 0
                    for key, value in positionDictinary.items():

                        if (abs(key[0]//modifier - x ) + abs(key[1]//modifier - y ) + abs(key[2]//modifier - z )) <= value//modifier:
                            count += 1

                    if count > maxCount:
                        maxCount = count
                        maxCountCoordinate = (x, y, z)

        print(f"Test soultion: {maxCountCoordinate}, {maxCount}. modifier: {modifier}")
        modifier = modifier / 10
        oldCountCoordinate = maxCountCoordinate


if __name__ == '__main__':

    inputList = readInput("input.txt")

    print(inputList)

    positionDictinary = parseInput(inputList)

    print(positionDictinary)

    #largestNonobot(positionDictinary)

    mostNonobots(positionDictinary)
