import re
import time
import pickle
import simplejson

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

    print(positionDictinary)

    for key, value in positionDictinary.items():

        if value > largestNanoBotRadius:
            largestNanoBotRadius = value
            largestNanoBotKey = key

    modifier = 10000000
    oldCountCoordinate = (0, 0, 0)
    visistedOld = []
    n = 0
    while(modifier >= 1):
        maxCount = 0
        maxCountCoordinate = (0, 0, 0)

        for x in range(oldCountCoordinate[0] * 10 - (12 + n), oldCountCoordinate[0] * 10 + (12 + n)):
            for y in range(oldCountCoordinate[1] * 10 - (12 + n), oldCountCoordinate[1] * 10 + (12 + n)):
                for z in range(oldCountCoordinate[2] * 10 - (12 + n), oldCountCoordinate[2] * 10 + (12 + n)):
                    count = 0

                    if modifier == 1000000000:
                        print(x,y,z)
                        print(range(oldCountCoordinate[2] * 9 - 9, oldCountCoordinate[2] * 10 + 10))
                        print((oldCountCoordinate[2] * 9 , oldCountCoordinate[2] * 10 ))
                        print((oldCountCoordinate[2] * 9, oldCountCoordinate[2] * 10))

                    for key, value in positionDictinary.items():

                        #print(key[0]//modifier, key[1]//modifier, key[2]//modifier, value//modifier)
                        if (abs(key[0]/modifier - x ) + abs(key[1]/modifier - y ) + abs(key[2]/modifier - z )) <= value/modifier:
                            count += 1

                    if count > maxCount:
                        maxCount = count
                        maxCountCoordinate = (x, y, z)
        n += 1

        print(f"Test soultion: {maxCountCoordinate}, {maxCount}. modifier: {modifier}")
        modifier = modifier / 10
        oldCountCoordinate = maxCountCoordinate
        #print(oldCountCoordinate)





def mostNonobots2(positionDictinary):
    '''

    :param positionDictinary:
    :return:
    '''


    largestNanoBotRadius = 0
    largestNanoBotKey = (0, 0, 0)

    minX = 0
    minY = 0
    minZ = 0

    maxX = 0
    maxY = 0
    maxZ = 0

    for key, value in positionDictinary.items():

        if key[0] > maxX:
            maxX = key[0]

        if key[1] > maxY:
            maxY = key[1]

        if key[2] > maxZ:
            maxZ = key[2]

        if key[0] < minX:
            minX = key[0]

        if key[1] < minY:
            minY = key[1]

        if key[2] < minZ:
            minZ = key[2]

    #print(minX, minY, minZ)
    #print(maxX, maxY, maxZ)


    middleLeft = (0, 0, 0)
    middleRight = (0, 0, 0)
    maxCoordinates = (maxX, maxY, maxZ)
    minCoordinates = (minX, minY, minZ)

    for _ in range(1):

        #find 5 points on left
        botListLeft = []
        for index in range(1, 10000):

            point = (minCoordinates[0] - middleLeft[0], minCoordinates[1] - middleLeft[1], minCoordinates[2] - middleLeft[2])
            count = 0
            for key,value in positionDictinary.items():
                if (abs(key[0]  - point[0]) / index + abs(key[1]  - point[0]) / index + abs(key[2]  - point[0]) / index ) <= value :
                        count += 1

            botListLeft.append((point, count))
        print("End of iteration")
        print(botListLeft)

        max = 0
        maxCoordinate = (0, 0, 0)
        for newMiddle in botListLeft:
            if newMiddle[1] > max:
                maxCoordinate = newMiddle[0]
                max = newMiddle[1]

        print(f"Left max: {maxCoordinate}. Count: {max}")

        #find 5 points on right
        botListRight = []
        for index in range(1, 6):

            point = (maxCoordinates[0] - middleRight[0], maxCoordinates[1] - middleRight[1], maxCoordinates[2] - middleRight[2])
            count = 0
            for key,value in positionDictinary.items():
                if (abs(key[0]  - point[0]) / index + abs(key[1]  - point[0]) / index + abs(key[2]  - point[0]) / index ) <= value :
                        count += 1

            botListRight.append((point, count))
        print("End of iteration")
        print(botListRight)

        max = 0
        maxCoordinate = (0, 0, 0)
        for newMiddle in botListRight:
            if newMiddle[1] > max:
                maxCoordinate = newMiddle[0]
                max = newMiddle[1]

        print(f"Right max: {maxCoordinate}. Count: {max}")



def mostNonobots3(positionDictinary):
    '''

    :param positionDictinary:
    :return:
    '''

    banList = []

    largestNanoBotRadius = 0
    largestNanoBotKey = (0, 0, 0)

    minX = 0
    minY = 0
    minZ = 0

    maxX = 0
    maxY = 0
    maxZ = 0

    for key, value in positionDictinary.items():

        if key[0] > maxX:
            maxX = key[0]

        if key[1] > maxY:
            maxY = key[1]

        if key[2] > maxZ:
            maxZ = key[2]

        if key[0] < minX:
            minX = key[0]

        if key[1] < minY:
            minY = key[1]

        if key[2] < minZ:
            minZ = key[2]

    print(minX, minY, minZ)
    print(maxX, maxY, maxZ)


    middleLeft = (0, 0, 0)
    middleRight = (0, 0, 0)
    #middleLeft = (39518994, 36744388, 31005584)
    #middleRight = (-18017, -3083, -2823)

    maxCoordinates = (20000000, 40000000, 50000000)
    minCoordinates = (minX, minY, minZ)

    #maxCoordinates = (maxX, maxY, maxZ)
    #minCoordinates = (0, 0, 0)

    countNumber = 10000
    heap = []

    print("")
    print("")
    for iterationNumber in range(10):

        print("Start")
        print(f"minCoordinates: {minCoordinates}. maxCoordinates: {maxCoordinates}")
        print(f"middleLeft: {middleLeft}. middleRight: {middleRight}")

        #find 5 points on left
        botListLeft = []
        for index in range(1, countNumber):

            #point = (minCoordinates[0] + abs(middleLeft[0] - minCoordinates[0]  ) //countNumber  * index  , minCoordinates[1] +  abs(middleLeft[1] - minCoordinates[1]  ) //countNumber  * index, minCoordinates[2] + abs(middleLeft[2] - minCoordinates[2]  ) //countNumber  * index )
            point = (middleLeft[0] - abs(middleLeft[0] - minCoordinates[0]) // countNumber * index,
                     middleLeft[1]  - abs(middleLeft[1] - minCoordinates[1]) // countNumber * index,
                     middleLeft[2] - abs(middleLeft[2] - minCoordinates[2]) // countNumber * index)
            #print(point)

            count = 0
            for key,value in positionDictinary.items():
                if (abs(key[0]  - point[0]  ) + abs(key[1]  - point[0]  )  + abs(key[2]  - point[0]  )  ) <= value :
                        count += 1

            botListLeft.append((point, count))

        print("End of iteration")
        #print(botListLeft)

        maxLeft = 0
        maxCoordinateLeft = (0, 0, 0)
        for newMiddle in botListLeft:
            if newMiddle[1] > maxLeft and newMiddle[1] not in banList:
                maxCoordinateLeft = newMiddle[0]
                maxLeft = newMiddle[1]

        print(f"Left max: {maxCoordinateLeft}. Count: {maxLeft}")

        #find 5 points on right
        botListRight = []
        for index in range(1, countNumber):

            #point = (((maxCoordinates[0] - middleRight[0]) //countNumber ) * index , ((maxCoordinates[1] - middleRight[1] ) //countNumber ) * index , ((maxCoordinates[2] - middleRight[2]) //countNumber) * index )
            point = (middleRight[0] + abs(middleRight[0] - maxCoordinates[0]) // countNumber * index,
                     middleRight[1] + abs(middleRight[1] - maxCoordinates[1]) // countNumber * index,
                     middleRight[2] + abs(middleRight[2] - maxCoordinates[2]) // countNumber * index)
            #print(point)
            count = 0
            for key,value in positionDictinary.items():
                if (abs(key[0]  - point[0]  )  + abs(key[1]  - point[0] )  + abs(key[2]  - point[0] )  ) <= value :
                        count += 1

            botListRight.append((point, count))

        print("End of iteration")
        #print(botListRight)

        maxRight = 0
        maxCoordinateRight = (0, 0, 0)
        for newMiddle in botListRight:
            if newMiddle[1] > maxRight and newMiddle[1] not in banList:
                maxCoordinateRight = newMiddle[0]
                maxRight = newMiddle[1]

        print(f"Right max: {maxCoordinateRight}. Count: {maxRight}")
        print(f"minCoordinates: {minCoordinates}. maxCoordinates: {maxCoordinates}")
        print(f"middleLeft: {middleLeft}. middleRight: {middleRight}")

        if maxRight > maxLeft:

            minCoordinates = middleRight
            middleRight = maxCoordinateRight
            middleLeft = middleRight
        else:
            maxCoordinates = middleLeft
            middleLeft = maxCoordinateLeft
            middleRight = middleLeft

        print("")
        print("")



if __name__ == '__main__':

    inputList = readInput("input.txt")

    print(inputList)
    print(len(inputList))

    positionDictinary = parseInput(inputList)

    print(positionDictinary)

    #largestNonobot(positionDictinary)

    mostNonobots(positionDictinary)

