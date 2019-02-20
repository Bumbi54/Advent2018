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
    Parses a list input strings,
    :param inputList: list where each entry is a line from input file
    :return: list of parsed inputs strings - [[x, y, x_change, y_change],.... [x, y, x_change, y_change]]
    '''

    parsedList = []
    for line in inputList:
        m = re.search(r'position=<\s*([-]?\d+), \s*([-]?\d+)> velocity=<\s*([-]?\d+), \s*([-]?\d+)>', line)
        parsedList.append([int(m.group(1)),int(m.group(2)),int(m.group(3)),int(m.group(4))])

    return parsedList

def findText(parsedList):
    """
    
    :param parsedList: 
    :return: 
    """

    for step in range(1000000):

        #make a set just from current coordinates
        coordinates = set((x,y) for x,y,x_change,y_change in parsedList)

        minX = (min(coordinates, key=lambda x: x[0]))[0]
        maxX = (max(coordinates, key=lambda x: x[0]))[0]
        minY = (min(coordinates, key=lambda x: x[1]))[1]
        maxY = (max(coordinates, key=lambda x: x[1]))[1]

        #print(f"minX:{minX}, maxX: {maxX}, minY:{minY}, maxY:{maxY}")

        #print(coordinates)

        if (maxX - minX) < 300 and (maxY - minY) < 15:
            print(f"Writing in file in step: {step}")
            print(f"minX:{minX}, maxX: {maxX}, minY:{minY}, maxY:{maxY}")
            print(coordinates)
            with open("output.txt", 'a') as file:
                for y in range(minY, maxY  + 1):
                    for x in range(minX, maxX + 1):
                        #print(f"x {x}, y {y}")
                        if (x,y) in coordinates:
                            #print("#", end = '')
                            file.write("#")
                        else:
                            #print(".", end='')
                            file.write(".")

                    #print("")
                    file.write("\n")
                file.write("\nEND!!!\n\n")

        parsedList = [[x + x_change,y + y_change,x_change,y_change] for x,y,x_change,y_change in parsedList]

        #print("", end='\n\n')

if __name__ == '__main__':
    inputList = readInput("input.txt")

    print(inputList)

    parsedList = parseInput(inputList)
    print(parsedList)

    findText(parsedList)
