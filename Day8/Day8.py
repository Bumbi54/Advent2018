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

        return list(map(int, fileContent.split(" ")))


def recursiveFunction(index, nodeList, sum):
    #this is recursive that is call for every node

    orignalIndex = index
    #if node doesn't have childrens
    if nodeList[index] == 0:

        numberOfMetadata = nodeList[index + 1]
        #return sum of metaData for currnet node
        tmpSum = 0
        for metaData in nodeList[index + 2: index + numberOfMetadata + 2]:
            tmpSum += metaData

        return (numberOfMetadata, tmpSum)

    for i in range(nodeList[index]):

        resultTuple = recursiveFunction(index + 2, nodeList, 0)

        index += resultTuple[0] + 2
        sum += resultTuple[1]

    numberOfMetadata = nodeList[orignalIndex + 1]
    # return sum of metaData for currnet node
    for metaData in nodeList[index + 2: index + 2 + numberOfMetadata]:
        sum += metaData

    return (index - orignalIndex + numberOfMetadata, sum)


def recursiveFunctionSecondPart(index, nodeList, sum):
    #this is recursive that is call for every node

    orignalIndex = index
    #if node doesn't have childrens
    if nodeList[index] == 0:

        numberOfMetadata = nodeList[index + 1]
        #return sum of metaData for currnet node
        tmpSum = 0
        for metaData in nodeList[index + 2: index + numberOfMetadata + 2]:
            tmpSum += metaData

        return (numberOfMetadata, tmpSum)

    listOfChildsMetaData = []
    for i in range(nodeList[index]):

        resultTuple = recursiveFunctionSecondPart(index + 2, nodeList, 0)

        index += resultTuple[0] + 2
        #sum += resultTuple[1]
        listOfChildsMetaData.append(resultTuple[1])

    numberOfMetadata = nodeList[orignalIndex + 1]
    # return sum of metaData for currnet node
    for metaData in nodeList[index + 2: index + 2 + numberOfMetadata]:

        if metaData - 1 > (len(listOfChildsMetaData)) - 1:
            sum += 0
        else:
            sum += listOfChildsMetaData[metaData - 1]

    return (index - orignalIndex + numberOfMetadata, sum)

if __name__ == '__main__':
    inputString = readInput("input.txt")
    print(inputString)

    #sum = recursiveFunction(0, inputString, 0)

    #print(sum)

    sum = recursiveFunctionSecondPart(0, inputString, 0)

    print(sum)



