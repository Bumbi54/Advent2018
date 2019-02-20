import re
from collections import deque
from copy import copy, deepcopy

def readInput(fileName):
    """
    Read input file and parse it into a list
    :param fileName: name of input file
    :return: list of input file content (each line is new element)
    """
    with open(fileName, 'r') as file:

        plotArray = []
        for line in file:
            plotArray.append(list(line.strip()))

        return plotArray

def drvosjecaUMladosti(plotArray):
    '''

    :param plotArray:
    :return:
    '''

    for _ in range(10):
        plotArrayPrevious = deepcopy(plotArray)

        for x in range(len(plotArrayPrevious)):
            for y in range(len(plotArrayPrevious[0])):

                #countAdjacentAcres =[., #, |]
                countAdjacentAcres = [0, 0, 0]

                #check eight adjacent acres
                for x_offset in [-1,0, 1]:
                    for y_offset in [-1,0, 1]:

                        #print(f"In loop. Acre {x,y}. Previous value: {plotArrayPrevious[x][y]} Adjacent acres: {x + x_offset},{y+y_offset}. ")

                        #if adjacent acres is out of range
                        if (x + x_offset >= 0 and y + y_offset >= 0 and x + x_offset < len(plotArrayPrevious) and y + y_offset < len(plotArrayPrevious[0])) and not (y_offset == 0 and x_offset == 0):

                            #print(f"More In loop. Acre {x,y}. Previous value: {plotArrayPrevious[x][y]} Adjacent acres: {x + x_offset},{y+y_offset}. {plotArrayPrevious[x + x_offset][y+y_offset]}")

                            adjacentAcre = plotArrayPrevious[x + x_offset][y + y_offset]

                            if adjacentAcre =='.':
                                countAdjacentAcres[0] += 1
                            elif adjacentAcre =='#':
                                countAdjacentAcres[1] += 1
                            elif adjacentAcre =='|':
                                countAdjacentAcres[2] += 1

                #print(f"Acre {x,y}. Previous value: {plotArrayPrevious[x][y]} Adjacent acres: {countAdjacentAcres}")

                if plotArrayPrevious[x][y] == '.' and countAdjacentAcres[2] > 2:
                    plotArray[x][y] = '|'
                elif plotArrayPrevious[x][y] == '|' and countAdjacentAcres[1] > 2:
                    plotArray[x][y] = '#'
                elif plotArrayPrevious[x][y] == '#' and (countAdjacentAcres[1] == 0 or countAdjacentAcres[2] == 0):
                    plotArray[x][y] = '.'

    stringPlotArray = ''.join(acre for innerlist in plotArray for acre in innerlist)
    print(stringPlotArray.count("|"))
    print(stringPlotArray.count("#"))

    print(f"Result is: {stringPlotArray.count('|') * stringPlotArray.count('#') }")


def drvosjecaUStarosti(plotArray):
    '''

    :param plotArray:
    :return:
    '''

    flag = True
    for index in range(1000000000):
        plotArrayPrevious = deepcopy(plotArray)

        for x in range(len(plotArrayPrevious)):
            for y in range(len(plotArrayPrevious[0])):

                #countAdjacentAcres =[., #, |]
                countAdjacentAcres = [0, 0, 0]

                #check eight adjacent acres
                for x_offset in [-1,0, 1]:
                    for y_offset in [-1,0, 1]:

                        #print(f"In loop. Acre {x,y}. Previous value: {plotArrayPrevious[x][y]} Adjacent acres: {x + x_offset},{y+y_offset}. ")

                        #if adjacent acres is out of range
                        if (x + x_offset >= 0 and y + y_offset >= 0 and x + x_offset < len(plotArrayPrevious) and y + y_offset < len(plotArrayPrevious[0])) and not (y_offset == 0 and x_offset == 0):

                            #print(f"More In loop. Acre {x,y}. Previous value: {plotArrayPrevious[x][y]} Adjacent acres: {x + x_offset},{y+y_offset}. {plotArrayPrevious[x + x_offset][y+y_offset]}")

                            adjacentAcre = plotArrayPrevious[x + x_offset][y + y_offset]

                            if adjacentAcre =='.':
                                countAdjacentAcres[0] += 1
                            elif adjacentAcre =='#':
                                countAdjacentAcres[1] += 1
                            elif adjacentAcre =='|':
                                countAdjacentAcres[2] += 1

                #print(f"Acre {x,y}. Previous value: {plotArrayPrevious[x][y]} Adjacent acres: {countAdjacentAcres}")

                if plotArrayPrevious[x][y] == '.' and countAdjacentAcres[2] > 2:
                    plotArray[x][y] = '|'
                elif plotArrayPrevious[x][y] == '|' and countAdjacentAcres[1] > 2:
                    plotArray[x][y] = '#'
                elif plotArrayPrevious[x][y] == '#' and (countAdjacentAcres[1] == 0 or countAdjacentAcres[2] == 0):
                    plotArray[x][y] = '.'

        stringPlotArray = ''.join(acre for innerlist in plotArray for acre in innerlist)
        stringPlotArrayPrevious = ''.join(acre for innerlist in plotArrayPrevious for acre in innerlist)

        #print(f'Wood: {stringPlotArray.count("|")}. Index: {index}.')
        print(f'Lumbermill: {stringPlotArray.count("#")}. Index: {index}')

    print(f"Result is: {stringPlotArray.count('|') * stringPlotArray.count('#') }")

if __name__ == "__main__":

    plotArray = readInput("input.txt")

    #drvosjecaUMladosti(plotArray)

    drvosjecaUStarosti(plotArray)
