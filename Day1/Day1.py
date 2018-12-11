


def readInput(fileName):
    """
    Read input file and parse it into a list
    :param fileName: name of input file
    :return: list of input file content (each line is new element)
    """
    with open(fileName, 'r') as file:

        fileContent = []
        for line in file:
            fileContent.append(int(line.strip()))

        return fileContent

def calculateFrequency(sequenceList, startFrequency = 0):
    """
    Calculate frequency by sequence list
    :param sequenceList: list of sequence (+/-integer)
    :param startFrequency: starting frequency
    :return: Final frequency - integer
    """

    for sequence in sequenceList:
        startFrequency += sequence

    return  startFrequency

def calculateFrequencyDuplicate(sequenceList, startFrequency = 0):
    """
    Calculate frequency by sequence list until same frequency is found twice
    :param sequenceList: list of sequence (+/-integer)
    :param startFrequency: starting frequency
    :return: Final frequency - integer
    """

    alreadyFound = []
    result = False
    while not result:

        #print(alreadyFound)
        for sequence in sequenceList:

            newFrequency =  startFrequency + sequence

            if newFrequency in alreadyFound:
                print(f"Found duplicated frequency {newFrequency}")
                result =  True
                return newFrequency
            else:
                startFrequency = newFrequency
                alreadyFound.append(newFrequency)




if __name__ == '__main__':

    sequenceList = readInput("input.txt")
    print(sequenceList)

    finalFrequency = calculateFrequency(sequenceList, 0)

    print(finalFrequency)

    result = calculateFrequencyDuplicate(sequenceList,0)

    print(f"Duplicate found: {result}")