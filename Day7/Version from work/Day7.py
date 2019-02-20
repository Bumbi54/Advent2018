import re
from collections import deque
import string

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


def parseInput(fileContent):
    '''
    Parse file content into dictionary
    :param fileContent: list of steps that will bea parsed
    :return: dictionary that represent steps (key) and and to which steps they are prerequisites (values)
    '''

    stepsDict = {}

    for line in fileContent:

        m = re.search('Step (\w) must be finished before step (\w) can begin.', line)

        if m.group(1) in stepsDict.keys():

            stepsDict[m.group(1)].append(m.group(2))
        else:
            stepsDict[m.group(1)] = [m.group(2) ]

    return stepsDict

def resolveSteps(stepsDict):
    '''
    Find order of steps. Go from steps that don't have prerequisites in alphabetical order
    :param stepsDict: dictionary that represent steps (key) and and to which steps they are prerequisites (values)
    :return: string that represents order of steps that was processed
    '''

    queue = deque([])
    stepOrder = ''


    dictValues = [value for values in stepsDict.values() for value in values]

    #find steps without prerequisites
    for step in stepsDict.keys():

        #check if step have prerequisites, if not add it to queue
        if step not in dictValues:
            queue.append(step)

    queue = deque(sorted(queue))

    while (True):

        if not queue:
            print(f"All steps in queue are resolved: {stepOrder}")
            break

        step = queue.popleft()

        #add step to step order
        stepOrder = stepOrder + step

        #go over steps for which current step is prerequisit and add it to queue if it is not in queue
        if step in stepsDict.keys():
            for nextStep in stepsDict[step]:

                flagPrerequisitesNotResolved = True
                for key,value in stepsDict.items():

                    if nextStep in value and key not in stepOrder:
                        flagPrerequisitesNotResolved = False

                if nextStep not in queue and flagPrerequisitesNotResolved:
                    queue.append(nextStep)

        queue = deque(sorted(queue))

    return stepOrder

def resolveSteps2(stepsDict):
    '''
    :param stepsDict: dictionary that represent steps (key) and and to which steps they are prerequisites (values)
    :return: string that represents order of steps that was processed
    '''

    dictTime = {char: counter + 1 for counter, char in enumerate(string.ascii_uppercase)}
    print(dictTime)
    seconds = 0
    valuesList = [value for values in stepsDict.values() for value in values]
    print(valuesList)
    workDict = {}

    visisted = set()
    while(True):


        for step in workDict.keys():

            if step not in visisted and step not in workDict.keys():

                workDict[step] = 60 + dictTime[step]

        seconds += 1

        if not workDict:
            break

        print(workDict)
        print(visisted)
        for key in list(workDict.keys()):

         newValue = workDict[key] - 1

        if newValue == 0:
            del workDict[key]
            visisted.add(step)
        elif key not in visisted:
            workDict[key] = newValue

    return seconds

if __name__ == "__main__":

    inputFile = readInput("input.txt")
    print(inputFile)

    stepsDict = parseInput(inputFile)

    print(stepsDict)

    stepOrder = resolveSteps(stepsDict)


    print(stepOrder)

    stepOrder = resolveSteps2(stepsDict)


    print(stepOrder)

