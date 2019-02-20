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
        for x in range(minX - 1, maxX + 9):
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

                if x in xDictinary.keys():

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

    #caveSystem[20][166] = '#'

    extra = True
    while True:
        #print("Iteration")
        #print(queue)
        if queue:
            nextStep = queue.pop()
        elif extra:
            extra = False
            caveSystem[103][155] = '~'
            nextStep = (103, 154)
        else:
            break
        #print(nextStep)

        #time.sleep(1)
        if nextStep[0] <= (len(caveSystem)) and nextStep[1] <= (len(caveSystem[0])):
            listNextSteps = analizeNeighbours(caveSystem, nextStep, maxX)

        if listNextSteps:
            for step in listNextSteps:

                if caveSystem[step[0]][step[1]] == '.' or caveSystem[step[0]][step[1]] == '|':
                    queue.append(step)
        '''
        with open("output.txt", "w") as file:
            for row in caveSystem:
                file.write(' '.join(row))
                file.write("\n")
        '''
    #for row in caveSystem:
    #    print(row)

    #(104, 165)
    with open("output.txt", "w") as file:
            for row in caveSystem:
                file.write(''.join(row))
                file.write("\n")
    print("End")
    return  caveSystem

def analizeNeighbours(caveSystem, point, maxX):
    print(f"My point is: {point}")
    if point[0] + 1 > maxX:
        caveSystem[point[0]][point[1]] = '|'
        return

    left = (point[0], point[1] - 1)
    right = (point[0], point[1] + 1)
    down = (point[0] + 1, point[1])
    up =  (point[0] - 1, point[1])


    if (caveSystem[up[0]][up[1]] == '+' or caveSystem[up[0]][up[1]] == '|') and caveSystem[down[0]][down[1]] == '.':
        caveSystem[point[0]][point[1]] = '|'

        return [down]

    elif caveSystem[up[0]][up[1]] == '|'  and (caveSystem[down[0]][down[1]] == '#' or caveSystem[down[0]][down[1]] == '~' ):

        leftWall = False
        rightWall = False
        for y in range(point[1], len(caveSystem[0])):

            if caveSystem[point[0] + 1][y] == '.':
                break

            if caveSystem[point[0]][y] == '#':
                rightWall = True
                wallCoordianteRight =  y
                break

        for y in reversed(range(0, point[1])):

            if caveSystem[point[0] + 1][y] == '.':
                break

            if caveSystem[point[0]][y ] == '#' :
                leftWall = True
                wallCoordianteLeft =  y
                break

        if leftWall and rightWall:
            for y in range(wallCoordianteLeft + 1, wallCoordianteRight):

                caveSystem[point[0]][y] = '~'

            return [up]
        elif not leftWall and rightWall:

            for y in reversed(range(0, point[1])):

                if caveSystem[point[0] + 1][y] == '.':
                    fallCoordiante = y
                    break

            for y in range(fallCoordiante, wallCoordianteRight):
                caveSystem[point[0]][y] = '|'

            return [(point[0] + 1, fallCoordiante)]

        elif  leftWall and not rightWall:

            for y in range(point[1], len(caveSystem[0])):

                if caveSystem[point[0] + 1][y] == '.':
                    fallCoordiante = y
                    break

            for y in range(wallCoordianteLeft + 1 ,fallCoordiante + 1):
                caveSystem[point[0]][y] = '|'

            return [(point[0] + 1, fallCoordiante)]

        elif not leftWall and not rightWall:
            print("Al last")
            for y in range(point[1], len(caveSystem[0])):

                if caveSystem[point[0] + 1][y] == '.':
                    fallCoordianteRight = y
                    break

            for y in reversed(range(0, point[1])):

                if caveSystem[point[0] + 1][y] == '.':
                    fallCoordianteLeft = y
                    break

            print(fallCoordianteLeft, fallCoordianteRight)
            for y in range(fallCoordianteLeft, fallCoordianteRight + 1):
                caveSystem[point[0]][y] = '|'

            return [(point[0] + 1, fallCoordianteRight), (point[0] + 1, fallCoordianteLeft)]

        return []

    elif caveSystem[down[0]][down[1]] == '~':

        print(point)
        waterFall = False
        for y in range(point[1], len(caveSystem[0])):

            if caveSystem[point[0] + 1][y] == '.':
                break

            if caveSystem[point[0]][y] == '|':
                waterFall = True
                break

        for y in reversed(range(0, point[1])):

            if caveSystem[point[0] + 1][y] == '.':
                break

            if caveSystem[point[0]][y] == '|':
                waterFall = True
                break

        if waterFall:

            leftWall = False
            rightWall = False
            for y in range(point[1], len(caveSystem[0])):

                if caveSystem[point[0] + 1][y] == '.':
                    break

                if caveSystem[point[0]][y] == '#':
                    rightWall = True
                    wallCoordianteRight = y
                    break

            for y in reversed(range(0, point[1])):

                if caveSystem[point[0] + 1][y] == '.':
                    break

                if caveSystem[point[0]][y] == '#':
                    leftWall = True
                    wallCoordianteLeft = y
                    break
            print(leftWall, rightWall)
            if leftWall and rightWall:

                for y in range(wallCoordianteLeft + 1, wallCoordianteRight):
                    caveSystem[point[0]][y] = '~'

                return [up]
            elif not leftWall and rightWall:

                for y in reversed(range(0, point[1])):

                    if caveSystem[point[0] + 1][y] == '.':
                        fallCoordiante = y
                        break

                for y in range(fallCoordiante, wallCoordianteRight):
                    caveSystem[point[0]][y] = '|'

                return [(point[0] + 1, fallCoordiante)]

            elif leftWall and not rightWall:

                for y in range(point[1], len(caveSystem[0])):

                    if caveSystem[point[0] + 1][y] == '.':
                        fallCoordiante = y
                        break

                for y in range(wallCoordianteLeft + 1, fallCoordiante + 1):
                    caveSystem[point[0]][y] = '|'

                return [(point[0] + 1, fallCoordiante)]

            elif not leftWall and not rightWall:
                print("Al last222")
                for y in range(point[1], len(caveSystem[0])):

                    if caveSystem[point[0] + 1][y] == '.':
                        fallCoordianteRight = y
                        break

                for y in reversed(range(0, point[1])):

                    if caveSystem[point[0] + 1][y] == '.':
                        fallCoordianteLeft = y
                        break

                print(fallCoordianteLeft, fallCoordianteRight)
                for y in range(fallCoordianteLeft, fallCoordianteRight + 1):
                    caveSystem[point[0]][y] = '|'

                return [(point[0] + 1, fallCoordianteRight), (point[0] + 1, fallCoordianteLeft)]

        return []

    elif caveSystem[down[0]][down[1]] == '|' and caveSystem[up[0]][up[1]] == '|':
        caveSystem[point[0]][point[1]] = '|'
    else:
        print("End is here")
        print(point)


    '''
    elif caveSystem[left[0]][left[1]] == '~' and caveSystem[right[0]][right[1]] == '.' and caveSystem[down[0]][down[1]] == '#':
        caveSystem[point[0]][point[1]] = '~'

        return [right]


    elif caveSystem[left[0]][left[1]] == '~' and caveSystem[right[0]][right[1]] == '#'  and caveSystem[down[0]][down[1]] == '#':
        caveSystem[point[0]][point[1]] = '~'

        return [up]

    elif caveSystem[right[0]][right[1]] == '~' and caveSystem[left[0]][left[1]] == '.' and caveSystem[down[0]][down[1]] == '#':
        caveSystem[point[0]][point[1]] = '~'

        return [left]

    elif caveSystem[right[0]][right[1]] == '~' and  caveSystem[left[0]][left[1]] == '#' and caveSystem[down[0]][down[1]] == '#':
        caveSystem[point[0]][point[1]] = '~'

        return [up]
    




    elif caveSystem[up[0]][up[1]] == '|' and caveSystem[down[0]][down[1]] == '~' and  (caveSystem[left[0]][left[1]] == '|' or caveSystem[left[0]][left[1]] == '|'):
        caveSystem[point[0]][point[1]] = '|'

        return []

    elif caveSystem[up[0]][up[1]] == '|'  and caveSystem[down[0]][down[1]] == '~':
        print(f"joj bojim se: {point}")
        waterFall = False
        #check for wall on right
        for y in range(point[1], len(caveSystem[0]) ):

            if caveSystem[point[0] + 1][y] != '~' or (caveSystem[point[0]][y + 1] == '#' and not waterFall) :
                wallCoordianteLeft =  (point[0], y)
                break
            elif caveSystem[point[0]][y + 1] == '|':
                    waterFall = True

        for y in reversed(range(0, point[1])):

            if caveSystem[point[0] + 1][y] != '~' or (caveSystem[point[0]][y - 1] == '#' and not waterFall) :
                wallCoordianteRight = (point[0], y)
                break
            elif caveSystem[point[0]][y - 1] == '|':
                    waterFall = True
        print(f"waterFall,{waterFall}")
        print(waterFall, wallCoordianteLeft, wallCoordianteRight)
        if not waterFall:
            for y in range(point[1], wallCoordianteLeft[1] + 1):
                caveSystem[point[0]][y] = '~'

            for y in reversed(range(wallCoordianteRight[1], point[1] + 1)):
                caveSystem[point[0]][y] = '~'

            list = []

            if caveSystem[wallCoordianteRight[0]][y - 1] != '#':
                list.append((wallCoordianteRight[0], wallCoordianteRight[1] - 1))

            if caveSystem[wallCoordianteLeft[0]][y + 1] != '#':
                list.append((wallCoordianteLeft[0], wallCoordianteLeft[1] + 1))

            return list

        else:
            caveSystem[point[0]][point[1]] = '|'
            return [left]



    elif caveSystem[left[0]][left[1]] == '#' and caveSystem[down[0]][down[1]] == '~' :

        closed = False
        #check for wall on right
        for y in range(point[1], len(caveSystem[0]) ):

            if caveSystem[point[0] + 1][y] != '~':
                break
            elif caveSystem[point[0]][y + 1] == '#':
                    closed = True
                    wallCoordiante = (point[0], y)
        print(f"Var: {closed}")
        if closed:
            for y in range(point[1], wallCoordiante[1] + 1):
                caveSystem[point[0]][y] = '~'

        return [up]

    elif caveSystem[right[0]][right[1]] == '#' and caveSystem[down[0]][down[1]] == '~' :
        print(f"Yes yes: {point}")
        closed = False
        #check for wall on right
        for y in reversed(range(0, point[1])):
            if caveSystem[point[0] + 1][y] != '~':
                break
            elif caveSystem[point[0]][y - 1] == '#':
                    closed = True
                    wallCoordiante = (point[0], y)

        if closed:
            print(f"Var: {closed}, {wallCoordiante}")
            for y in reversed(range(wallCoordiante[1], point[1] + 1)):
                caveSystem[point[0]][y] = '~'
        print(f"up: {up}")
        print(f"closed: {closed}")
        return [up]

    elif caveSystem[left[0]][left[1]] == '.' and caveSystem[down[0]][down[1]] == '~' and caveSystem[left[0] + 1][left[1]] == '#':
        print(f"Why here: {point}")
        waterFall = False
        #check for wall on right
        for y in range(point[1], len(caveSystem[0]) ):


            if caveSystem[point[0] + 1][y] != '~' or (caveSystem[point[0]][y + 1] == '#' and not waterFall) :
                break
            elif caveSystem[point[0]][y + 1] == '|':
                    waterFall = True
            if (caveSystem[point[0]][y + 1] == '#' or caveSystem[point[0] + 1][y + 1] == '#') and waterFall:
                wallCoordiante = (point[0], y)
                break

        if waterFall:
            for y in range(point[1], wallCoordiante[1] + 1):
                caveSystem[point[0]][y] = '~'

            if caveSystem[wallCoordiante[0]][y + 1] != '#':
                print(f"I was here sfdsdgfsdgdsfkgbsdjk: {wallCoordiante}")
                return  [(wallCoordiante[0], wallCoordiante[1] + 1), left]

            return [left]

    elif caveSystem[right[0]][right[1]] == '.' and caveSystem[down[0]][down[1]] == '~' and caveSystem[right[0] + 1][right[1]] == '#':
        print(f"Why here right: {point}")
        waterFall = False
        wallCoordiante = False
        #check for wall on right
        for y in reversed(range(0, point[1])):


            if caveSystem[point[0] + 1][y] != '~' or (caveSystem[point[0]][y - 1] == '#' and not waterFall) :
                break
            elif caveSystem[point[0]][y - 1] == '|':
                    waterFall = True
            if (caveSystem[point[0]][y - 1] == '#' or caveSystem[point[0] + 1][y - 1] == '#') and waterFall:
                wallCoordiante = (point[0], y)
                break

        if waterFall and wallCoordiante:
            for y in reversed(range(wallCoordiante[1], point[1] + 1)):
                caveSystem[point[0]][y] = '~'

            if caveSystem[wallCoordiante[0]][y - 1] != '#':
                print(f"I was here sfdsdgfsdgdsfkgbsdjk: {wallCoordiante}")
                return  [(wallCoordiante[0], wallCoordiante[1] - 1), right]

            return [right]

    elif caveSystem[down[0]][down[1]] == '|' and caveSystem[up[0]][up[1]] == '|':
        caveSystem[point[0]][point[1]] = '|'

    '''

if __name__ == '__main__':

    inputList = readInput("input.txt")
    print(inputList)
    print(len(inputList))

    caveSystem = parseInput(inputList)

    caveSystem = calculateWater(caveSystem)

