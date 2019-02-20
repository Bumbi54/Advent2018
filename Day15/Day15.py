import re
import time
import networkx
import collections
from collections import  deque


def readInput(fileName):
    """
    Read input file and parse it into a string
    :param fileName: name of input file
    :return: list of input file content (each line is new element)
    """
    with open(fileName, 'r') as file:
        fileContent = []
        for line in file.readlines():
            fileContent.append(list(line.strip()))

        return fileContent


# finds nodes in targets that have the same shortest path distance from start
# without visiting a node in excluded_nodes
def find_closest(graph, excluded_nodes, start, targets):
    if start not in graph:
        return [], 0

    seen = set()
    q = deque([(start, 0)])
    found_dist = None
    closest = []
    while q:
        cell, dist = q.popleft()
        if found_dist is not None and dist > found_dist:
            if found_dist is None:
                found_dist = 0
            return closest, found_dist

        if cell in seen or (cell in excluded_nodes):
            continue
        seen.add(cell)
        #print(f"In search: {cell},{dist}")
        #print(f"In search: {q},{seen}")
        if cell in targets:
            found_dist = dist
            closest.append(cell)

        for n in graph.neighbors(cell):
            if n not in seen and n not in excluded_nodes:
                q.append((n, dist + 1))
    if found_dist is None:
        found_dist = 0

    return closest, found_dist


def ofElfsAndGloblins(inputList):
    '''
    
    :param inputList: 
    :return: 
    '''
    elfList = []
    globlinsList = []
    maze = networkx.Graph()

    unitDict = {}

    for x in range(1, len(inputList) ):
        for y in range(1, len(inputList[0])):

            if inputList[x][y] == 'G':
                globlinsList.append((x,y))
                unitDict[(x,y)] = (200, 'G')
            elif inputList[x][y] == 'E':
                elfList.append((x,y))
                unitDict[(x, y)] = (200, 'E')
            if inputList[x][y] != '#':
                maze.add_node((x,y))
                if inputList[x - 1][y] != '#':
                    maze.add_edge((x,y), (x-1, y))
                if inputList[x ][y-1] != '#':
                    maze.add_edge((x,y), (x, y - 1))

    print(maze.edges)
    print(elfList)
    print(globlinsList)

    #move
    i = 1
    while(True):

        print(f"i: {i}")
        for unit in sorted(elfList + globlinsList):
            if unit not in unitDict.keys():
                continue
            #print(f"unit: {unit}")
            if unit in elfList:
                excluded = elfList[:]
                excluded.remove(unit)
                closestEnemy, distance = find_closest(maze, excluded, unit, globlinsList)
                #print(f"Just a test: {closestEnemy}, distance:{distance}")

            else:
                #print(globlinsList)
                excluded = globlinsList[:]
                excluded.remove(unit)
                #print(excluded)
                closestEnemy, distance = find_closest(maze, excluded, unit, elfList)
                #print(f"Just a test: {closestEnemy}, distance:{distance}")

            if closestEnemy:
                # choose the closest by reading order
                choice = min(closestEnemy, key= lambda x : (x[0] , x[1]) )

                neighbours = []
                if (unit[0], unit[1] + 1) in maze.nodes:
                    neighbours.append((unit[0], unit[1] + 1))
                if (unit[0] + 1, unit[1]) in maze.nodes:
                    neighbours.append((unit[0] + 1, unit[1]))
                if (unit[0] - 1, unit[1]) in maze.nodes:
                    neighbours.append((unit[0] - 1, unit[1]))
                if (unit[0], unit[1] - 1) in maze.nodes:
                    neighbours.append((unit[0], unit[1] - 1))

                # find next cell which has a shortest path of the same distance
                for s in sorted(neighbours, key=lambda x : (x[0] , x[1])):
                    #print(f"s: {s}")
                    #excluded = globlinsList[:] + elfList[:]
                    #excluded.remove(s)
                    _, d = find_closest(maze, excluded, s, [choice])
                    #print(f"d: {d}")
                    if d == distance - 1:
                        nextStep = s
                        break

                #print(f"Nexthop: {nextStep}")

            if distance > 1:
                temp = unitDict[unit]
                del unitDict[unit]
                #print(f"Here: {temp}, nextStep:{nextStep}")
                unitDict[nextStep] = temp

                if unit in elfList:
                    elfList.remove(unit)
                    elfList.append(nextStep)
                else:
                    globlinsList.remove(unit)
                    globlinsList.append(nextStep)

            # combat
            attackList = []
            #print(f"unitDict: {unitDict}")
            #print(f"unit: {unit}")
            if unit not in unitDict.keys():
                #time.sleep(1)
                #print(f"minShortest_pathList {minShortest_pathList}")
                unitTmp = nextStep
            else:
                unitTmp = unit
            if (unitTmp[0] - 1, unitTmp[1]) in unitDict.keys():
                if unitDict[(unitTmp[0] - 1, unitTmp[1])][1] != unitDict[unitTmp][1]:
                    attackList.append((unitTmp[0] - 1, unitTmp[1], unitDict[unitTmp[0] - 1, unitTmp[1]][0], unitDict[unitTmp[0] - 1, unitTmp[1]][1]))
            if (unitTmp[0] + 1, unitTmp[1]) in unitDict.keys():
                if unitDict[(unitTmp[0] + 1, unitTmp[1])][1] != unitDict[unitTmp][1]:
                    attackList.append((unitTmp[0] + 1, unitTmp[1], unitDict[unitTmp[0] + 1, unitTmp[1]][0], unitDict[unitTmp[0] + 1, unitTmp[1]][1]))

            if (unitTmp[0], unitTmp[1] - 1) in unitDict.keys():
                if unitDict[(unitTmp[0], unitTmp[1] - 1)][1] != unitDict[unitTmp][1]:
                    attackList.append((unitTmp[0], unitTmp[1] - 1, unitDict[unitTmp[0], unitTmp[1] - 1][0], unitDict[unitTmp[0], unitTmp[1] - 1][1]))

            if (unitTmp[0], unitTmp[1] + 1) in unitDict.keys():
                if unitDict[(unitTmp[0], unitTmp[1] + 1)][1] != unitDict[unitTmp][1]:
                    attackList.append((unitTmp[0], unitTmp[1] + 1, unitDict[unitTmp[0], unitTmp[1] + 1][0], unitDict[unitTmp[0], unitTmp[1] + 1][1]))

            #print(f"attackList: {attackList}")

            if attackList:
                #print(f"before: {attackList}")
                attackList = sorted(attackList, key = lambda x: (x[2], x[0],  x[1]))
                #print(f"after: {attackList}")
                chosenTarget = (attackList[0][0], attackList[0][1])
                if unitDict[chosenTarget][1] == 'G':
                    unitDict[chosenTarget] =  (unitDict[chosenTarget][0] - 3, unitDict[chosenTarget][1])
                else:
                    unitDict[chosenTarget] = (unitDict[chosenTarget][0] - 3, unitDict[chosenTarget][1])

                if unitDict[chosenTarget][0] <= 0:

                    del unitDict[chosenTarget]
                    #print(maze.nodes)
                    if chosenTarget in globlinsList:
                        globlinsList.remove(chosenTarget)
                    elif chosenTarget in elfList:
                        elfList.remove(chosenTarget)

                    maze.add_node(chosenTarget)
                    if (chosenTarget[0] + 1, chosenTarget[1]) in maze.nodes:
                        maze.add_edge(chosenTarget, (chosenTarget[0] + 1, chosenTarget[1]))
                    if (chosenTarget[0], chosenTarget[1] + 1) in maze.nodes:
                        maze.add_edge(chosenTarget, (chosenTarget[0], chosenTarget[1] + 1))
                    if (chosenTarget[0] - 1, chosenTarget[1]) in maze.nodes:
                        maze.add_edge(chosenTarget, (chosenTarget[0] - 1, chosenTarget[1]))
                    if (chosenTarget[0], chosenTarget[1] - 1) in maze.nodes:
                        maze.add_edge(chosenTarget, (chosenTarget[0], chosenTarget[1] - 1))


        #print(f"elfList: {elfList}, globlinsList:{globlinsList}")
        #print(f"unitDict: {unitDict}")
        #print(f"maze: {maze.nodes}")
        #time.sleep(1)
        if not elfList:
            break
        if not globlinsList:
            break
        i += 1

    print(i)
    print(f"Sum: {sum(hitpoints[0] for hitpoints in unitDict.values())}")



def ofElfsAndGloblins2(inputList, elfsAttack):
    '''

    :param inputList: 
    :return: 
    '''
    elfList = []
    globlinsList = []
    maze = networkx.Graph()

    unitDict = {}

    for x in range(1, len(inputList)):
        for y in range(1, len(inputList[0])):

            if inputList[x][y] == 'G':
                globlinsList.append((x, y))
                unitDict[(x, y)] = (200, 'G')
            elif inputList[x][y] == 'E':
                elfList.append((x, y))
                unitDict[(x, y)] = (200, 'E')
            if inputList[x][y] != '#':
                maze.add_node((x, y))
                if inputList[x - 1][y] != '#':
                    maze.add_edge((x, y), (x - 1, y))
                if inputList[x][y - 1] != '#':
                    maze.add_edge((x, y), (x, y - 1))

    print(maze.edges)
    print(elfList)
    print(globlinsList)

    # move
    i = 1
    while (True):

        print(f"i: {i}")
        for unit in sorted(elfList + globlinsList):
            if unit not in unitDict.keys():
                continue
            # print(f"unit: {unit}")
            if unit in elfList:
                excluded = elfList[:]
                excluded.remove(unit)
                closestEnemy, distance = find_closest(maze, excluded, unit, globlinsList)
                # print(f"Just a test: {closestEnemy}, distance:{distance}")

            else:
                # print(globlinsList)
                excluded = globlinsList[:]
                excluded.remove(unit)
                # print(excluded)
                closestEnemy, distance = find_closest(maze, excluded, unit, elfList)
                # print(f"Just a test: {closestEnemy}, distance:{distance}")

            if closestEnemy:
                # choose the closest by reading order
                choice = min(closestEnemy, key=lambda x: (x[0], x[1]))

                neighbours = []
                if (unit[0], unit[1] + 1) in maze.nodes:
                    neighbours.append((unit[0], unit[1] + 1))
                if (unit[0] + 1, unit[1]) in maze.nodes:
                    neighbours.append((unit[0] + 1, unit[1]))
                if (unit[0] - 1, unit[1]) in maze.nodes:
                    neighbours.append((unit[0] - 1, unit[1]))
                if (unit[0], unit[1] - 1) in maze.nodes:
                    neighbours.append((unit[0], unit[1] - 1))

                # find next cell which has a shortest path of the same distance
                for s in sorted(neighbours, key=lambda x: (x[0], x[1])):
                    # print(f"s: {s}")
                    # excluded = globlinsList[:] + elfList[:]
                    # excluded.remove(s)
                    _, d = find_closest(maze, excluded, s, [choice])
                    # print(f"d: {d}")
                    if d == distance - 1:
                        nextStep = s
                        break

                        # print(f"Nexthop: {nextStep}")

            if distance > 1:
                temp = unitDict[unit]
                del unitDict[unit]
                # print(f"Here: {temp}, nextStep:{nextStep}")
                unitDict[nextStep] = temp

                if unit in elfList:
                    elfList.remove(unit)
                    elfList.append(nextStep)
                else:
                    globlinsList.remove(unit)
                    globlinsList.append(nextStep)

            # combat
            attackList = []
            # print(f"unitDict: {unitDict}")
            # print(f"unit: {unit}")
            if unit not in unitDict.keys():
                # time.sleep(1)
                # print(f"minShortest_pathList {minShortest_pathList}")
                unitTmp = nextStep
            else:
                unitTmp = unit
            if (unitTmp[0] - 1, unitTmp[1]) in unitDict.keys():
                if unitDict[(unitTmp[0] - 1, unitTmp[1])][1] != unitDict[unitTmp][1]:
                    attackList.append((unitTmp[0] - 1, unitTmp[1], unitDict[unitTmp[0] - 1, unitTmp[1]][0],
                                       unitDict[unitTmp[0] - 1, unitTmp[1]][1]))
            if (unitTmp[0] + 1, unitTmp[1]) in unitDict.keys():
                if unitDict[(unitTmp[0] + 1, unitTmp[1])][1] != unitDict[unitTmp][1]:
                    attackList.append((unitTmp[0] + 1, unitTmp[1], unitDict[unitTmp[0] + 1, unitTmp[1]][0],
                                       unitDict[unitTmp[0] + 1, unitTmp[1]][1]))

            if (unitTmp[0], unitTmp[1] - 1) in unitDict.keys():
                if unitDict[(unitTmp[0], unitTmp[1] - 1)][1] != unitDict[unitTmp][1]:
                    attackList.append((unitTmp[0], unitTmp[1] - 1, unitDict[unitTmp[0], unitTmp[1] - 1][0],
                                       unitDict[unitTmp[0], unitTmp[1] - 1][1]))

            if (unitTmp[0], unitTmp[1] + 1) in unitDict.keys():
                if unitDict[(unitTmp[0], unitTmp[1] + 1)][1] != unitDict[unitTmp][1]:
                    attackList.append((unitTmp[0], unitTmp[1] + 1, unitDict[unitTmp[0], unitTmp[1] + 1][0],
                                       unitDict[unitTmp[0], unitTmp[1] + 1][1]))

            # print(f"attackList: {attackList}")

            if attackList:
                # print(f"before: {attackList}")
                attackList = sorted(attackList, key=lambda x: (x[2], x[0], x[1]))
                # print(f"after: {attackList}")
                chosenTarget = (attackList[0][0], attackList[0][1])
                if unitDict[chosenTarget][1] == 'G':
                    unitDict[chosenTarget] = (unitDict[chosenTarget][0] - elfsAttack, unitDict[chosenTarget][1])
                else:
                    unitDict[chosenTarget] = (unitDict[chosenTarget][0] - 3, unitDict[chosenTarget][1])

                if unitDict[chosenTarget][0] <= 0:
                    if unitDict[chosenTarget][1] == 'E':
                        print(f"Elf has died")
                        return 0

                    del unitDict[chosenTarget]
                    # print(maze.nodes)
                    if chosenTarget in globlinsList:
                        globlinsList.remove(chosenTarget)
                    elif chosenTarget in elfList:
                        elfList.remove(chosenTarget)

                    maze.add_node(chosenTarget)
                    if (chosenTarget[0] + 1, chosenTarget[1]) in maze.nodes:
                        maze.add_edge(chosenTarget, (chosenTarget[0] + 1, chosenTarget[1]))
                    if (chosenTarget[0], chosenTarget[1] + 1) in maze.nodes:
                        maze.add_edge(chosenTarget, (chosenTarget[0], chosenTarget[1] + 1))
                    if (chosenTarget[0] - 1, chosenTarget[1]) in maze.nodes:
                        maze.add_edge(chosenTarget, (chosenTarget[0] - 1, chosenTarget[1]))
                    if (chosenTarget[0], chosenTarget[1] - 1) in maze.nodes:
                        maze.add_edge(chosenTarget, (chosenTarget[0], chosenTarget[1] - 1))

        # print(f"elfList: {elfList}, globlinsList:{globlinsList}")
        # print(f"unitDict: {unitDict}")
        # print(f"maze: {maze.nodes}")
        # time.sleep(1)
        if not elfList:
            break
        if not globlinsList:
            break
        i += 1

    print(i)
    print(f"Sum: {sum(hitpoints[0] for hitpoints in unitDict.values())}")

if __name__ == '__main__':
    inputList = readInput("input.txt")

    print(inputList)

    ofElfsAndGloblins(inputList)
    time.sleep(1)
    for attack in range(3, 1000):

        output = ofElfsAndGloblins2(inputList, attack)
        print(f"New attack: {attack}")

        if output!= 0:
            break


