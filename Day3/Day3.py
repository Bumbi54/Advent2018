import re

def readInput(fileName):
    """
    Read input file and parse it into a list
    :param fileName: name of input file
    :return: list of input file content (each line is new element)
    """
    with open(fileName, 'r') as file:

        fileContent = []
        for line in file:
            fileContent.append(line.strip())

        return fileContent


def parseInputToGrid(inputFile):
    """
    Make a dictionary that represent a grid
    :param input: content of input file
    :return: dictionary that represent a grid
    """

    dictinary = {}

    for command in inputFile:

        m = re.search('#\d+ @ (\d+),(\d+): (\d+)x(\d+)', command)

        if m:
            #print(f"Start postition x: {m.group(1)}, Start postion y: {m.group(2)}. Grid: {m.group(3)} x {m.group(4)}")

            for x in range(int(m.group(1)), (int(m.group(1)) + int(m.group(3))) ) :

                for y in range(int(m.group(2)), (int(m.group(2)) + int(m.group(4)) )):

                    #print(x,y)
                    if (x,y) in dictinary.keys():
                        dictinary[(x,y)] += 1
                    else:
                        dictinary[(x, y)] = 1



        else:
            print("Regular expresion not found")
            return 0

    return dictinary

def findFreeID(inputFile, parsedGrids):
    """
    Find ID that is free
    :param input: content of input file
    :parsedGrids input: parsed grid with data about all of the ID
    :return: ID that is not in conflict
    """

    for command in inputFile:

        m = re.search('#\d+ @ (\d+),(\d+): (\d+)x(\d+)', command)
        print(command)

        inConflict = False

        if m:

            for x in range(int(m.group(1)), (int(m.group(1)) + int(m.group(3))) ) :

                for y in range(int(m.group(2)), (int(m.group(2)) + int(m.group(4)) )):

                    #print(x,y)
                    if parsedGrids[(x, y)] > 1:
                        inConflict = True
                        break
                        dictinary[(x,y)] += 1

        else:
            print("Regular expresion not found")
            return 0

        if not inConflict:
            return command



if __name__ == '__main__':

    list_of_ID = readInput("input.txt")
    print(list_of_ID)

    resultDictionary = parseInputToGrid(list_of_ID)

    print(resultDictionary)

    conflict = 0
    for value in resultDictionary.values():

        if value > 1:
            conflict += 1

    print(f"Conflict numbers: {conflict}")

    notInCOnflictID = findFreeID(list_of_ID, resultDictionary)

    print(f"ID not in conflict: {notInCOnflictID}")