import re
import time
import pickle
from collections import deque


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
    xDictinary = {}
    yDictinary = {}
    maxX = 0
    maxY = 0
    minX = 500

    for line in inputList:

        m = re.search("x=(\d+), y=(\d+)..(\d+)", line)

        if m:
            if int(m.group(1)) not in xDictinary.keys():
                xDictinary[int(m.group(1))] = [(int(m.group(2)), int(m.group(3)))]
            else:
                xDictinary[int(m.group(1))].append((int(m.group(2)), int(m.group(3))))

            if int(m.group(1)) > maxX:
                maxX = int(m.group(1))
            if int(m.group(1)) < minX:
                minX = int(m.group(1))
            if int(m.group(3)) > maxY:
                maxY = int(m.group(3))

        else:
            m = re.search("y=(\d+), x=(\d+)..(\d+)", line)

            if int(m.group(1)) not in yDictinary.keys():
                yDictinary[int(m.group(1))] = [(int(m.group(2)), int(m.group(3)))]
            else:
                yDictinary[int(m.group(1))].append((int(m.group(2)), int(m.group(3))))

            if int(m.group(1)) > maxY:
                maxY = int(m.group(1))
            if int(m.group(3)) > maxX:
                maxX = int(m.group(3))
            if int(m.group(3)) < minX:
                minX = int(m.group(3))


    print(xDictinary)
    print(yDictinary)
    print(maxX, maxY,minX)
        #positionDictinary[(int(m.group(1)), int(m.group(2)), int(m.group(3)))] = int(m.group(4))

    caveSystem = []
    for y in range(maxY + 8):
        row = []
        for x in range(minX, maxX + 9):
            rowSet = False
            if x == 500 and y == 0:
                row.append('+')
                rowSet = True
            else:
                if y in yDictinary.keys():

                    for interval in yDictinary[y]:
                        if interval[0] <= x <= interval[1] and not rowSet:
                            row.append('#')
                            rowSet = True

                elif x in xDictinary.keys():

                        for interval in xDictinary[x]:
                            if interval[0] <= y <= interval[1] and not rowSet:
                                row.append('#')
                                rowSet = True


            if not rowSet:
                row.append('.')
        caveSystem.append(row)

    #for row in caveSystem:
     #   print(row)

    return (caveSystem)

def calculateWater(caveSystem):

    sourceCoordinate = (0, 0)
    maxX = 0

    for x in range(len(caveSystem)):
        for y in range(len(caveSystem[0])):

            if  caveSystem[x][y] == '+':
                sourceCoordinate = (x,y)

        if x > maxX:
            maxX = x

    print(sourceCoordinate)

    queue = deque([])
    queue.append((sourceCoordinate[0] + 1, sourceCoordinate[1]))
    while True:
        print("Iteration")
        if queue:
            nextStep = queue.pop()
        else:
            break
        print(nextStep)

        #$time.sleep(1)
        if nextStep[0] <= (len(caveSystem) - 7) and nextStep[1] <= (len(caveSystem[0]) - 7):
            listNextSteps = analizeNeighbours(caveSystem, nextStep, maxX)

        print(listNextSteps)

        if listNextSteps:
            for step in listNextSteps:

                if caveSystem[step[0]][step[1]] == '.':
                    queue.append(step)
                elif caveSystem[step[0]][step[1]] == '|' and (caveSystem[step[0]][step[1] - 1]  == '~' or caveSystem[step[0]][step[1] + 1] == '~'):
                    print("alooooo????")
                    print(step)
                    if caveSystem[step[0]][step[1] - 1] == '.':
                        queue.append((step[0], step[1] - 1))
                    if caveSystem[step[0]][step[1] + 1] == '.':
                        queue.append((step[0], step[1] + 1))

                    caveSystem[step[0]][step[1]] = '~'


        #for row in caveSystem:
            #print(row)
    print()
    with open("output.txt", "w") as file:
        for row in caveSystem:
            file.write(' '.join(row))
            file.write("\n")
    #for row in caveSystem:
    #    print(row)
    print("Endc")

def analizeNeighbours(caveSystem, point, maxX):

    if point[0] + 1 > maxX:
        caveSystem[point[0]][point[1]] = '|'
        return

    left = (point[0], point[1] - 1)
    right = (point[0], point[1] + 1)
    down = (point[0] + 1, point[1])
    up =  (point[0] - 1, point[1])

    print(caveSystem[left[0]][left[1]], caveSystem[right[0]][right[1]], caveSystem[down[0]][down[1]], caveSystem[up[0]][up[1]] )

    if caveSystem[left[0]][left[1]] == '.' and caveSystem[right[0]][right[1]] == '.' and caveSystem[down[0]][down[1]] == '.' and (caveSystem[up[0]][up[1]] == '+' or caveSystem[up[0]][up[1]] == '|'):
        caveSystem[point[0]][point[1]] = '|'
        if caveSystem[left[0] + 1][left[1]] == '#':
            return [down, left]
        if caveSystem[right[0] + 1][right[1]] == '#':
            return [down, right]

        return [down]


    elif (caveSystem[left[0]][left[1]] == '#' or caveSystem[right[0]][right[1]] == '#') and (caveSystem[left[0]][left[1]] == '~' or caveSystem[right[0]][right[1]] == '~'):
        print("must be here")
        waterFallFound = False
        waterFallCoordiante = (0, 0)
        #check for waterfall
        for y in range(up[1], len(caveSystem[0]) ):
            print(f"y in right: {y}")
            if caveSystem[up[0]][y] == '#':
                break
            elif caveSystem[up[0]][y] == '|':
                waterFallFound = True
                waterFallCoordiante = (up[0], y)

        for y in reversed(range(0, up[1] + 1)):
            print(f"y in left: {y}")
            if caveSystem[up[0]][y] == '#':
                break
            elif caveSystem[up[0]][y] == '|':
                waterFallFound = True
                waterFallCoordiante = (up[0], y)

        if (caveSystem[up[0]][up[1] + 1] == '#' or caveSystem[up[0]][up[1] - 1] == '#') and waterFallFound:
            caveSystem[point[0]][point[1]] = '~'
            caveSystem[up[0]][up[1]] = '~'
            return [left, right, down, up, (up[0], up[1] - 1), (up[0], up[1] + 1)]
        elif waterFallFound:
            #return [left, right, down, up, (up[0], up[1] - 1), (up[0], up[1] + 1)]
            print(f"heheheheh: {waterFallCoordiante}")
            caveSystem[point[0]][point[1]] = '~'
            return [(waterFallCoordiante[0], waterFallCoordiante[1] - 1), (waterFallCoordiante[0], waterFallCoordiante[1] + 1)]

            #waterFallCoordiante

        else:
            caveSystem[point[0]][point[1]] = '~'
            return [left, right, down]


    elif (caveSystem[left[0]][left[1]] == '|' or caveSystem[right[0]][right[1]] == '|') and (
            caveSystem[left[0]][left[1]] == '#' or caveSystem[right[0]][right[1]] == '#') and caveSystem[down[0]][
        down[1]] == '~':
        caveSystem[point[0]][point[1]] = '~'

        if (caveSystem[point[0]][point[1] + 1] == '|' and caveSystem[point[0]][point[1] + 2] == '|') or (
                caveSystem[point[0]][point[1] - 1] == '|' and caveSystem[point[0]][point[1] - 2] == '|'):
            return []
        return [up]


    elif caveSystem[down[0]][down[1]] == '.' and caveSystem[up[0]][up[1]] == '|':
        caveSystem[point[0]][point[1]] = '|'
        return [down]
    elif caveSystem[down[0]][down[1]] == '#' and caveSystem[up[0]][up[1]] == '|':
        caveSystem[point[0]][point[1]] = '~'
        return [left, right, up]
    elif (caveSystem[left[0]][left[1]] == '#' or caveSystem[right[0]][right[1]] == '#') and caveSystem[up[0]][up[1]] == '|':
        caveSystem[point[0]][point[1]] = '~'
        return [left, right, down]
    elif (caveSystem[left[0]][left[1]]== '~' or caveSystem[right[0]][right[1]] == '~'):
        caveSystem[point[0]][point[1]] = '~'
        return [left, right, down]

    elif (caveSystem[left[0]][left[1]]== '|' or caveSystem[right[0]][right[1]] == '|') and caveSystem[down[0]][down[1]] == '#':
        caveSystem[point[0]][point[1]] = '|'
        return [left, right]
    elif (caveSystem[left[0]][left[1]] == '|' or caveSystem[right[0]][right[1]] == '|') and caveSystem[down[0]][down[1]] == '.' and  caveSystem[up[0]][up[1]] == '.':
        caveSystem[point[0]][point[1]] = '|'
        return [down]
    elif (caveSystem[left[0]][left[1]] == '|' or caveSystem[right[0]][right[1]] == '|') and caveSystem[down[0]][down[1]] == '~' :
        caveSystem[point[0]][point[1]] = '|'
        return [left, right]





    elif (caveSystem[down[0]][down[1]] == '#' or caveSystem[down[0]][down[1]] == '~') and caveSystem[up[0]][up[1]] == '~':
        caveSystem[point[0]][point[1]] = '~'
        return [left, right, down]



if __name__ == '__main__':

    inputList = readInput("input.txt")
    print(inputList)
    print(len(inputList))

    caveSystem = parseInput(inputList)

    calculateWater(caveSystem)

