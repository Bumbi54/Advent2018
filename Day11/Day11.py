import re
import time
import numpy


def findBestPowerCell():
    """
    
    :return: 
    """
    bestPowerLevel = 0
    coordinatesOfBestPowerCell = ''

    powerDictionary = {}

    for x in range(1,301):
        for y in range(1, 301):

            #calculate power level
            rackID = x + 10
            powerLevel = rackID * y
            powerLevel += 8772
            powerLevel = powerLevel * rackID

            if len(str(powerLevel)) > 2:
                powerLevel = int(str(powerLevel)[-3])
            else:
                powerLevel = 0

            powerLevel = powerLevel - 5

            powerDictionary[(x,y)] = powerLevel

    for x in range(1, 301):
        for y in range(1, 301):

            sum = 0

            if (x + 2) <= 300 and (y + 2) <= 300:
                for x_3_cell in range(3):
                    for y_3_cell in range(3):
                        sum = sum + powerDictionary[(x + x_3_cell , y + y_3_cell)]

                if sum > bestPowerLevel:
                    bestPowerLevel = sum
                    coordinatesOfBestPowerCell = (x,y)


    print(f"Best power level: {bestPowerLevel} on coordiantes: {coordinatesOfBestPowerCell}")


def secondFindBestPowerCell():
    """

    :return: 
    """
    bestPowerLevel = 0
    coordinatesOfBestPowerCell = ''

    powerDictionary = {}

    for x in range(1, 301):
        for y in range(1, 301):

            # calculate power level
            rackID = x + 10
            powerLevel = rackID * y
            powerLevel += 18
            powerLevel = powerLevel * rackID

            if len(str(powerLevel)) > 2:
                powerLevel = int(str(powerLevel)[-3])
            else:
                powerLevel = 0

            powerLevel = powerLevel - 5

            powerDictionary[(x, y)] = powerLevel

    for x in range(1, 301):
        for y in range(1, 301):

            sum = 0
            print(f"Curent coordiantes: {x} {y}")
            for x_size in range (1, 301):
                #print(f"Curent size: {x_size}")
                if (x + x_size - 1) <= 300 and (y + x_size - 1) <= 300:
                    for x_cell in range(x_size):
                        for y_cell in range(x_size):
                            sum = sum + powerDictionary[(x + x_cell, y + y_cell)]

                            if sum > bestPowerLevel:
                                bestPowerLevel = sum
                                coordinatesOfBestPowerCell = (x, y)

    print(f"Best power level: {bestPowerLevel} on coordiantes: {coordinatesOfBestPowerCell}")


def secondFindBestPowerCell2():
    """

    :return: 
    """
    bestPowerLevel = 0
    coordinatesOfBestPowerCell = ''
    size = 0

    powerDictionary = {}

    for x in range(1, 301):
        for y in range(1, 301):

            # calculate power level
            rackID = x + 10
            powerLevel = rackID * y
            powerLevel += 8772
            powerLevel = powerLevel * rackID

            if len(str(powerLevel)) > 2:

                powerLevel = int(str(powerLevel)[-3])
            else:
                powerLevel = 0

            powerLevel = powerLevel - 5

            powerDictionary[(x, y)] = powerLevel

    powerArray = numpy.array(list(powerDictionary.values()))
    powerArray = powerArray.reshape(300, 300)

    print(powerArray)
    for x in range(0, 300):
        for y in range(0, 300):

            for x_size in range (1, 301):
                if (x + x_size - 1) <= 300 and (y + x_size - 1) <= 300:

                    subArray = powerArray[x : x + x_size,
                                    y : y + x_size]
                    sum = numpy.sum(subArray)

                    if sum > bestPowerLevel:
                        bestPowerLevel = sum
                        coordinatesOfBestPowerCell = (x, y)
                        size = x_size

    print(f"Best power level: {bestPowerLevel} on coordiantes: {coordinatesOfBestPowerCell}, size {size}")

if __name__ == '__main__':
    result = secondFindBestPowerCell2()

    #result = findBestPowerCell()