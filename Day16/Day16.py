import re
import time

class Operations:

    def addr(self, customRegisters, A, B, C):
        customRegisters[C] = customRegisters[A] + customRegisters[B]

    def addi(self, customRegisters, A, B, C):
        customRegisters[C] = customRegisters[A] + B

    def mulr(self, customRegisters, A, B, C):
        customRegisters[C] = customRegisters[A] * customRegisters[B]

    def muli(self, customRegisters, A, B, C):
        customRegisters[C] = customRegisters[A] * B

    def banr(self, customRegisters, A, B, C):
        customRegisters[C] = customRegisters[A] & customRegisters[B]

    def bani(self, customRegisters, A, B, C):
        customRegisters[C] = customRegisters[A] & B

    def borr(self, customRegisters, A, B, C):
        customRegisters[C] = customRegisters[A] | customRegisters[B]

    def bori(self, customRegisters, A, B, C):
        customRegisters[C] = customRegisters[A] | B

    def setr(self, customRegisters, A, B, C):
        customRegisters[C] = customRegisters[A]

    def seti(self, customRegisters, A, B, C):
        customRegisters[C] = A

    def gtir(self, customRegisters, A, B, C):
        if A > customRegisters[B]:
            customRegisters[C] =  1
        else:
            customRegisters[C] = 0

    def gtri(self, customRegisters, A, B, C):
        if customRegisters[A] > B:
            customRegisters[C] =  1
        else:
            customRegisters[C] = 0

    def gtrr(self, customRegisters, A, B, C):
        if customRegisters[A] > customRegisters[B]:
            customRegisters[C] =  1
        else:
            customRegisters[C] = 0

    def eqir(self, customRegisters, A, B, C):
        if A == customRegisters[B]:
            customRegisters[C] =  1
        else:
            customRegisters[C] = 0

    def eqri(self, customRegisters, A, B, C):
        if customRegisters[A] == B:
            customRegisters[C] =  1
        else:
            customRegisters[C] = 0

    def eqrr(self, customRegisters, A, B, C):
        if customRegisters[A] == customRegisters[B]:
            customRegisters[C] =  1
        else:
            customRegisters[C] = 0



def readInput(fileName):
    """
    Read input file and parse it into a string
    :param fileName: name of input file
    :return: list of input file content (each line is new element)
    """
    with open(fileName, 'r') as file:

        fileContent = file.read()

        return fileContent.split("\n")

def parseInstruction(inputList):
    '''
    
    :param inputList: 
    :return: 
    '''

    operationDict = {}
    operationsObject = Operations()

    operationList = [operationsObject.addr, operationsObject.addi,
                     operationsObject.mulr, operationsObject.muli,
                     operationsObject.banr, operationsObject.bani,
                     operationsObject.borr, operationsObject.bori,
                     operationsObject.setr, operationsObject.seti,
                     operationsObject.gtir, operationsObject.gtri,operationsObject.gtrr,
                     operationsObject.eqir, operationsObject.eqri, operationsObject.eqrr,
                     ]

    i = 0
    while('Before' in inputList[i]):

        m = re.match(r'Before: \[(.*)\]', inputList[i])
        before = list(map(int, m.group(1).split(", ")))

        instruction = list(map(int, inputList[i + 1].split(" ")))

        m = re.match(r'After:  \[(.*)\]', inputList[i + 2])
        after = list(map(int, m.group(1).split(", ")))

        if instruction[0] not in operationDict.keys():
            operationDict[instruction[0]] = [0] * 16

        for index in range(len(operationList)):

            action = operationList[index]
            tmpBefore = before[:]
            action(tmpBefore, instruction[1], instruction[2], instruction[3])

            if tmpBefore == after:
                operationDict[instruction[0]][index] += 1

        i += 4

    opcodeDict = {}
    print(operationDict)
    while(list(operationDict.keys()) ):
        for key in list(operationDict.keys()):

            value = operationDict[key]

            maximumValue = max(value)

            if value.count(maximumValue) == 1:
                opcodeIndex = value.index(maximumValue)
                opcodeDict[key] = operationList[opcodeIndex]
                for key_temp in operationDict.keys():
                    operationDict[key_temp][opcodeIndex] = 0
                del operationDict[key]


    print(opcodeDict)

    registers = [0, 0, 0, 0]
    for command in inputList[i + 2 :]:

        parseCommand = command.split(" ")
        parseCommand = list(map(int, parseCommand))

        opcodeDict[parseCommand[0]](registers, parseCommand[1], parseCommand[2], parseCommand[3])

    print(registers)
    return registers


def parseInstructionDowngrade(inputList):
    '''

    :param inputList: 
    :return: 
    '''

    operationDict = {}
    operationsObject = Operations()

    operationList = [operationsObject.addr, operationsObject.addi,
                     operationsObject.mulr, operationsObject.muli,
                     operationsObject.banr, operationsObject.bani,
                     operationsObject.borr, operationsObject.bori,
                     operationsObject.setr, operationsObject.seti,
                     operationsObject.gtir, operationsObject.gtri, operationsObject.gtrr,
                     operationsObject.eqir, operationsObject.eqri, operationsObject.eqrr,
                     ]

    countOpcode = 0
    i = 0
    while ('Before' in inputList[i]):

        m = re.match(r'Before: \[(.*)\]', inputList[i])
        before = list(map(int, m.group(1).split(", ")))

        instruction = list(map(int, inputList[i + 1].split(" ")))

        m = re.match(r'After:  \[(.*)\]', inputList[i + 2])
        after = list(map(int, m.group(1).split(", ")))

        operationDict[instruction[0]] = 0

        for index in range(len(operationList)):

            action = operationList[index]
            tmpBefore = before[:]
            action(tmpBefore, instruction[1], instruction[2], instruction[3])

            if tmpBefore == after:
                operationDict[instruction[0]] += 1

        if operationDict[instruction[0]] > 2:
            countOpcode += 1

        i += 4

    print(countOpcode)
    return operationDict

if __name__ == '__main__':
    inputList = readInput("input.txt")

    operationDict = parseInstructionDowngrade(inputList)

    print(operationDict)

    print(inputList)
    operationDict = parseInstruction(inputList)

    print(operationDict)


