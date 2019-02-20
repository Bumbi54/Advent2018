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

def parsGuardShift(sortedSchedule):
    """
    Parse Guards Shifts into dictionary
    :param sortedCchedule: sorted list of all of the guards Schedules
    :return: dictionary, key is Guard ID, value is list of guards sleep times. List of tuples "(BEGIN, END)"
    """

    guardDict = {}
    guardID = ''
    sleepStart = -1

    #iterate over every entry
    for entry in sortedSchedule:

        m = re.search('\[\d{4}-\d{2}-\d{2} \d{2}:(\d{2})\] (.+)', entry)

        #if regular expresion was found continue, else input file is not correct and exit function
        if m:

            #if entry is about guard save its ID and if it doesn't exist add it to dictinary
            if "Guard" in m.group(2):

                guardRe = re.search('Guard #(\d+) begins shift', m.group(2))
                guardID = guardRe.group(1)

                if guardID not in guardDict.keys():
                    guardDict[guardID] = []

            elif "falls asleep" == m.group(2):
                sleepStart = m.group(1)

            elif "wakes up" == m.group(2) and sleepStart != -1:
                guardDict[guardID].append( (int(sleepStart), int(m.group(1)) ))
                sleepStart = -1

            else:
                print("Order is not correct!!")
                break

        else:
            print("Input not correct!!")
            break

    return guardDict

def strategyOne(guardDict):
    """
    Calculate according to first strategy which guard is most likely to be asleep. Find the guard that has the most minutes asleep. What minute does that guard spend asleep the most?
    ID of the guard you chose multiplied by the minute you chose
    :param guardDict: dictionary with a list of sleep times for each guard
    :return: integer result
    """

    minutesAsleep = 0
    chosenGuard = ''


    #iterate over guard dict and find that is asleep the most minutes
    for guard, sleepList in guardDict.items():

        totalSleepTime = 0
        minutesInHour = [0] * 59
        #for each sleep time
        for sleepInterval in sleepList:
            totalSleepTime += sleepInterval[1] - sleepInterval[0]
            for  minute in range(sleepInterval[0], sleepInterval[1]):
                minutesInHour[minute] += 1

        #if guard has sleept the most so far set him as current chosen
        if totalSleepTime > minutesAsleep:
            minutesAsleep = totalSleepTime
            chosenGuard = (guard, minutesInHour)



    print(f"Guard: {chosenGuard[0]} was {minutesAsleep} minutes asleep. Minutes sleep in a hour: {chosenGuard[1].index(max(chosenGuard[1]))}")


def strategyOne(guardDict):
    """
    Calculate according to first strategy which guard is most likely to be asleep. Find the guard that has the most minutes asleep. What minute does that guard spend asleep the most?
    ID of the guard you chose multiplied by the minute you chose
    :param guardDict: dictionary with a list of sleep times for each guard
    :return: integer result
    """

    minutesAsleep = 0
    chosenGuard = ''

    # iterate over guard dict and find that is asleep the most minutes
    for guard, sleepList in guardDict.items():

        totalSleepTime = 0
        minutesInHour = [0] * 59
        # for each sleep time
        for sleepInterval in sleepList:
            totalSleepTime += sleepInterval[1] - sleepInterval[0]
            for minute in range(sleepInterval[0], sleepInterval[1]):
                minutesInHour[minute] += 1

        # if guard has sleept the most so far set him as current chosen
        if totalSleepTime > minutesAsleep:
            minutesAsleep = totalSleepTime
            chosenGuard = (guard, minutesInHour)

    print(f"Guard: {chosenGuard[0]} was {minutesAsleep} minutes asleep. Minutes sleep in a hour: {chosenGuard[1].index(max(chosenGuard[1]))}")

    return int(chosenGuard[0]) * int(chosenGuard[1].index(max(chosenGuard[1])) )


def strategyTwo(guardDict):
    """
    Calculate according to second strategy which guard is most likely to be asleep. Of all guards, which guard is most frequently asleep on the same minute?
    ID of the guard you chose multiplied by the minute you chose
    :param guardDict: dictionary with a list of sleep times for each guard
    :return: integer result
    """

    maxMinuteSleep = 0
    chosenGuard = ''

    # iterate over guard dict and find that is asleep the most minutes
    for guard, sleepList in guardDict.items():

        totalSleepTime = 0
        minutesInHour = [0] * 59
        # for each sleep time
        for sleepInterval in sleepList:
            for minute in range(sleepInterval[0], sleepInterval[1]):
                minutesInHour[minute] += 1

        # if guard has sleept the most so far set him as current chosen
        if max(minutesInHour)  > maxMinuteSleep:
            maxMinuteSleep = max(minutesInHour)
            chosenGuard = (guard, minutesInHour)

    print(f"Guard: {chosenGuard[0]}. Minutes sleep in a hour: {chosenGuard[1].index(max(chosenGuard[1]))} count: {max(chosenGuard[1])}")

    return int(chosenGuard[0]) * int(chosenGuard[1].index(max(chosenGuard[1])) )

def parseInput(inputFile):
    """
    Parse input from file into dictinary. Each dictionary entry is one guard
    :param inputFile: input file where each row is one element in a list
    :return: dictionary that represents guards and their sleep time
    """


if __name__ == "__main__":

    inputFile = readInput("input.txt")

    dict = parsGuardShift(sorted(inputFile))

    print(dict)

    strategyOne = strategyOne(dict)

    print(strategyOne)

    strategyTwo = strategyTwo(dict)

    print(strategyTwo)
