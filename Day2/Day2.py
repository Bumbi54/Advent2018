



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

def countLetterOccurrence(list_of_ID):
    """
    Coutn number of IDs that have exactly two of any letter and exactly three of any letter
    :param list_of_ID: list of all of the IDs taht will be tested
    :return: checksum (multiple of those two counts)
    """
    twoCount = 0
    threeCount = 0

    #for each ID
    for ID in list_of_ID:
        flagTwo = False
        flagThree = False

        #for each letter in ID count its occurrence number
        for letter in ID:

            if ID.count(letter) == 2 and not flagTwo:
                twoCount += 1
                flagTwo = True
                print(f"For ID: {ID} count two is found")
            if ID.count(letter) == 3 and not flagThree:
                threeCount += 1
                flagThree = True
                print(f"For ID: {ID} count three is found")

    print(f"Two count: {twoCount}. Three count: {threeCount}")

    return twoCount * threeCount

def differenceByOneCharacter(list_of_ID):
    """
    FInd two ID that have difference in only on character
    :param list_of_ID: list of all of the IDs taht will be tested
    :return: string with character that are the same
    """

    resultString = ""

    for ID in list_of_ID:

        for compareID in list_of_ID:

            differenceCount = 0

            for i in range(len(ID)):

                if ID[i] != compareID[i]:
                    differenceCount += 1

                if differenceCount > 1:
                    break

            if differenceCount == 1:
                print(f"Two ID that are different in only one letter: First: {ID}, Second: {compareID}")

                for i in range(len(ID)):

                    if ID[i] == compareID[i]:
                        resultString += ID[i]

                return resultString

    return resultString

if __name__ == '__main__':

    list_of_ID = readInput("input.txt")
    print(list_of_ID)

    checksum = countLetterOccurrence(list_of_ID)

    print(checksum)

    resultString = differenceByOneCharacter(list_of_ID)

    print(resultString)