import re
from collections import deque
from copy import copy, deepcopy
import time
import networkx as nx


def calculateCave(depth, targetPosition):
    '''

    :param depth:
    :param targetPosition:
    :return:
    '''

    caveSystem = {}

    for x in range(depth):
        for y in range(depth):

            if (x,y) in [(0, 0), targetPosition]:
                geologicIndex = 0
            elif y == 0:
                geologicIndex = x * 16807
            elif x == 0:
                geologicIndex = y * 48271
            else:
                geologicIndex = caveSystem[(x-1, y)][1] * caveSystem[(x, y-1)][1]

            erosionLevel = (depth + geologicIndex) % 20183
            caveSystem[(x,y)] = (erosionLevel % 3, erosionLevel)

    riskLevelArea(caveSystem, targetPosition)

def riskLevelArea(caveSystem, targetPosition):
    '''

    :param caveSystem:
    :param targetPosition:
    :return:
    '''

    totalRisklevel = 0
    for x in range(targetPosition[0] + 1):
        for y in range(targetPosition[1] + 1):

            totalRisklevel = totalRisklevel + caveSystem[(x,y)][0]

    print(totalRisklevel)


def calculateCave2(depth, targetPosition):
    '''

    :param depth:
    :param targetPosition:
    :return:
    '''

    caveGraph = nx.Graph()
    caveSystem = []
    currentTool = 0
    #torch = 0
    #climbing gear = 1
    #neither = 2
    toolDict = {
        0 : [0],
        1 : [1, 2],
        2 : [0, 2],
    }

    for x in range(depth):
        currentCaveLevel = []
        for y in range(depth):

            if (x,y) in [(0, 0), targetPosition]:
                geologicIndex = 0
            elif y == 0:
                geologicIndex = x * 16807
            elif x == 0:
                geologicIndex = y * 48271
            else:
                geologicIndex = caveSystem[x-1][y][1] * currentCaveLevel[y-1][1]

            erosionLevel = (depth + geologicIndex) % 20183
            currentCaveLevel.append((erosionLevel % 3, erosionLevel))

        caveSystem.append(currentCaveLevel)

    print("Calculate graph!")

    for x in range(depth - 3000):
        for y in range(depth - 3000):
            for tool in toolDict[caveSystem[x][y][0]]:
                if x < depth -1:
                    for nextTool in toolDict[caveSystem[x + 1][y][0]]:
                        if tool == nextTool:
                            caveGraph.add_edge((x,y,tool), (x + 1,y,nextTool), weight = 1)
                        elif nextTool in toolDict[caveSystem[x][y][0]]:
                            caveGraph.add_edge((x,y,tool), (x + 1,y,nextTool), weight = 8)
                
                if y <  depth -1:
                    for nextTool in toolDict[caveSystem[x][y + 1][0]]:
                        if tool == nextTool:
                            caveGraph.add_edge((x,y,tool), (x,y + 1,nextTool), weight = 1)
                        elif nextTool in toolDict[caveSystem[x][y][0]]:
                            caveGraph.add_edge((x,y,tool), (x,y + 1,nextTool), weight = 8)
            if x == 0 and y == 0:
                toolDict[0] =[0, 1]

    print(nx.dijkstra_path_length(caveGraph, (0,0,0), (targetPosition[0],targetPosition[1], 0) ))
    print(nx.dijkstra_path_length(caveGraph, (0,0,0), (targetPosition[0],targetPosition[1], 1) ))


def riskLevelArea2(caveSystem, targetPosition):
    '''

    :param caveSystem:
    :param targetPosition:
    :return:
    '''

    totalRisklevel = 0
    for x in range(targetPosition[0] + 1):
        for y in range(targetPosition[1] + 1):

            totalRisklevel = totalRisklevel + caveSystem[x][y][0]

    print(totalRisklevel)

if __name__ == "__main__":

    calculateCave2(4080, (14, 785))
