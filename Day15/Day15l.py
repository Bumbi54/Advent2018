import re
import time
import networkx
import collections


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


def ofElfsAndGloblins(inputList):
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
            elif inputList[x][y] == '.':
                maze.add_node((x, y))
                if inputList[x - 1][y] == '.':
                    maze.add_edge((x, y), (x - 1, y))
                if inputList[x][y - 1] == '.':
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
            print(f"unit: {unit}")
            # print(f"unit: {unit} unitDict :{unitDict}:")
            minShortest_pathList = []
            if unit in elfList:

                for target in globlinsList:
                    maze.add_node(unit)
                    if (unit[0], unit[1] + 1) in maze.nodes:
                        maze.add_edge(unit, (unit[0], unit[1] + 1))
                    if (unit[0] + 1, unit[1]) in maze.nodes:
                        maze.add_edge(unit, (unit[0] + 1, unit[1]))
                    if (unit[0] - 1, unit[1]) in maze.nodes:
                        maze.add_edge(unit, (unit[0] - 1, unit[1]))
                    if (unit[0], unit[1] - 1) in maze.nodes:
                        maze.add_edge(unit, (unit[0], unit[1] - 1))

                    maze.add_node(target)
                    if (target[0] + 1, target[1]) in maze.nodes:
                        maze.add_edge(target, (target[0] + 1, target[1]))
                    if (target[0], target[1] + 1) in maze.nodes:
                        maze.add_edge(target, (target[0], target[1] + 1))
                    if (target[0] - 1, target[1]) in maze.nodes:
                        maze.add_edge(target, (target[0] - 1, target[1]))
                    if (target[0], target[1] - 1) in maze.nodes:
                        maze.add_edge(target, (target[0], target[1] - 1))

                    minCoordinate = (-1, -1)
                    shortest_path = []
                    # print(f"unit {unit}, target: {target}")
                    if networkx.has_path(maze, unit, target):
                        shortest_paths = networkx.all_shortest_paths(maze, unit, target)
                        print("before")
                        for path in shortest_paths:
                            if path[1] < minCoordinate or minCoordinate == (-1, -1):
                                shortest_path = path
                                minCoordinate = path[1]
                        print("after")

                        # shortest_path = networkx.shortest_path(maze, unit, target)
                        # print(f"shortest_path: {shortest_path}, unit: {unit}, target:{target}")

                        if len(shortest_path) < len(minShortest_pathList) or len(minShortest_pathList) == 0:
                            minShortest_pathList = shortest_path
                    maze.remove_node(target)


            else:
                for target in elfList:
                    maze.add_node(unit)
                    if (unit[0], unit[1] + 1) in maze.nodes:
                        maze.add_edge(unit, (unit[0], unit[1] + 1))
                    if (unit[0] + 1, unit[1]) in maze.nodes:
                        maze.add_edge(unit, (unit[0] + 1, unit[1]))
                    if (unit[0] - 1, unit[1]) in maze.nodes:
                        maze.add_edge(unit, (unit[0] - 1, unit[1]))
                    if (unit[0], unit[1] - 1) in maze.nodes:
                        maze.add_edge(unit, (unit[0], unit[1] - 1))

                    maze.add_node(target)
                    # print(maze.edges)
                    if (target[0] + 1, target[1]) in maze.nodes:
                        maze.add_edge(target, (target[0] + 1, target[1]))
                    if (target[0], target[1] + 1) in maze.nodes:
                        maze.add_edge(target, (target[0], target[1] + 1))
                    if (target[0] - 1, target[1]) in maze.nodes:
                        maze.add_edge(target, (target[0] - 1, target[1]))
                    if (target[0], target[1] - 1) in maze.nodes:
                        maze.add_edge(target, (target[0], target[1] - 1))

                    minCoordinate = (-1, -1)
                    shortest_path = []
                    if networkx.has_path(maze, unit, target):
                        shortest_paths = networkx.all_shortest_paths(maze, unit, target)
                        print("before")
                        for path in shortest_paths:
                            if path[1] < minCoordinate or minCoordinate == (-1, -1):
                                shortest_path = path
                                minCoordinate = path[1]
                        print("after")

                        # shortest_path = networkx.shortest_path(maze, unit, target)
                        # print(f"shortest_path: {shortest_path}, unit: {unit}, target:{target}")

                        if len(shortest_path) < len(minShortest_pathList) or len(minShortest_pathList) == 0:
                            minShortest_pathList = shortest_path
                    # print(f"unit: {unit} minShortest_pathList: {minShortest_pathList}, maze.nodes {maze.nodes}")
                    maze.remove_node(target)

            # print("out")
            if len(minShortest_pathList) == 2:
                maze.remove_node(unit)

            elif len(minShortest_pathList) > 2:
                maze.remove_node(minShortest_pathList[1])
                temp = unitDict[unit]
                del unitDict[unit]
                unitDict[minShortest_pathList[1]] = temp
                # maze.remove_node(target)

                if unit in elfList:
                    elfList.remove(unit)
                    elfList.append(minShortest_pathList[1])
                else:
                    globlinsList.remove(unit)
                    globlinsList.append(minShortest_pathList[1])

                    # else:
                    # maze.remove_node(unit)
                    # print("A probelm")
            # print(f"edges, {maze.edges}")

            # combat
            attackList = []
            # print(f"unitDict: {unitDict}")
            # print(f"unit: {unit}")
            if unit not in unitDict.keys():
                # time.sleep(1)
                # print(f"minShortest_pathList {minShortest_pathList}")
                unitTmp = minShortest_pathList[1]
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
                unitDict[chosenTarget] = (unitDict[chosenTarget][0] - 3, unitDict[chosenTarget][1])

                if unitDict[chosenTarget][0] <= 0:
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


