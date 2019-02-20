import re
import time

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

    plantResolver = {}

    for entry in inputList:

        result = entry.split(" => ")
        plantResolver[result[0]] = result[1]

    return plantResolver

def calculatePorts(initialState, plantResolver):
    '''
    
    :param initialState: 
    :param plantResolver: 
    :return: 
    '''

    initialState = initialState.replace("initial state: ", "")

    emptyPots = ["." for _ in range(20)]

    listOfPots = emptyPots + list(initialState) + emptyPots

    print(listOfPots)

    for _ in range(20):

        oldGeneration = listOfPots[:]
        for index in range(len(listOfPots)):

            plantString = ''

            for neighbour in range (index - 2, index + 3):

                if neighbour < 0 or neighbour > (len(listOfPots) - 1):
                    plantString = plantString + '.'
                else:
                    plantString = plantString + oldGeneration[neighbour]

            if plantResolver.get(plantString):
                listOfPots[index] = plantResolver.get(plantString)
            else:
                listOfPots[index] = '.'


    return listOfPots


def calculatePortsSecond(initialState, plantResolver):
    '''

    :param initialState: 
    :param plantResolver: 
    :return: 
    '''

    initialState = initialState.replace("initial state: ", "")

    listOfPots =  list(initialState)

    print(listOfPots)
    indexAddedToLeft = 0
    previousGenertionSum = 0

    for generation in range(50000000000):

        if listOfPots[-1] == '#':
            listOfPots = listOfPots + ['.']

        if listOfPots[0] == '#':
            listOfPots = ['.'] + listOfPots
            indexAddedToLeft += 1

        oldGeneration = listOfPots[:]
        for index in range(len(listOfPots)):

            plantString = ''

            for neighbour in range(index - 2, index + 3):

                if neighbour < 0 or neighbour > (len(listOfPots) - 1):
                    plantString = plantString + '.'
                else:
                    plantString = plantString + oldGeneration[neighbour]

            if plantResolver.get(plantString):
                listOfPots[index] = plantResolver.get(plantString)
            else:
                listOfPots[index] = '.'

        indexSum = 0
        for index in range(len(listOfPots)):


            if listOfPots[index] == '#':
                indexSum += index - indexAddedToLeft
        if (indexSum - previousGenertionSum) == 73:
            print(f"Generation: {generation} Where 73 difference starts")
        previousGenertionSum = indexSum
        print(f"generation: {generation} indexSum: {indexSum}")

    return listOfPots

if __name__ == '__main__':
    inputList = readInput("input.txt")

    print(inputList)

    plantResolver = parseInput(inputList[2:])

    print(plantResolver)

    twentyGenerations  = calculatePorts(inputList[0], plantResolver)

    plantIndex = -20
    indexSum = 0
    for index in range(len(twentyGenerations)):

        if twentyGenerations[index] == '#':
            indexSum += plantIndex

        plantIndex += 1


    print(''.join(twentyGenerations))
    print(indexSum)

    #fiftyBillion  = calculatePortsSecond(inputList[0], plantResolver)

    #from generation 162 which has sum 12203 difference beetween each generation is 73
    sum = 12203 + (50000000000 - 162) * 73
    print(sum)