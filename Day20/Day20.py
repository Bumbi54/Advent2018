import re
import time
import networkx as nx


def readInput(fileName):
    """
    Read input file and parse it into a string
    :param fileName: name of input file
    :return: list of input file content (each line is new element)
    """
    with open(fileName, 'r') as file:

        fileContent = file.read()

        return fileContent

def pathToRoom(inputString):
    '''
    
    :param inputString: 
    :return: 
    '''

    roomGraph = nx.Graph()
    currentCoordinate = (0, 0)
    stackQue = []

    directionOperation = {
        "N" : lambda x : (x[0] - 1, x[1]),
        "S": lambda x: (x[0] + 1, x[1]),
        "E": lambda x: (x[0], x[1] + 1),
        "W": lambda x: (x[0], x[1] - 1),
    }

    for direction in inputString[1:-1]:
        #print(direction)

        if direction in 'NSWE':

            newPosition = directionOperation[direction](currentCoordinate)
            roomGraph.add_edge(currentCoordinate, newPosition)
            #print(f"Current coordiante: {currentCoordinate}. New cooridante: {newPosition}")
            currentCoordinate = newPosition

        elif direction == '(':
            stackQue.append(currentCoordinate)
        elif direction == ')':
            currentCoordinate = stackQue.pop()
        elif direction == '|':
            currentCoordinate = stackQue[-1]

    print(f"Graph: {roomGraph.nodes}")
    distances = nx.algorithms.shortest_path_length(roomGraph, (0, 0))
    print(distances)
    print(f"Max distance from start (0, 0) to a room is:{max(distances.values())}")

    print(f"Rooms with  distance from start (0, 0) more than 1000: {len([value for value in distances.values() if value > 999])}")


if __name__ == '__main__':


    inputString = readInput("input.txt")

    print(inputString)

    pathToRoom(inputString)

