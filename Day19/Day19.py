import re
import time


class Operations:


    def __init__(self):
        self.operationDict = {
                            "addr": self.addr,
                            "addi": self.addi,
                            "mulr": self.mulr,
                            "muli": self.muli,
                            "banr": self.banr,
                            "bani": self.bani,
                            "borr": self.borr,
                            "bori": self.bori,
                            "setr": self.setr,
                            "seti": self.seti,
                            "gtir": self.gtir,
                            "gtri": self.gtri,
                            "gtrr": self.gtrr,
                            "eqir": self.eqir,
                            "eqri": self.eqri,
                            "eqrr": self.eqrr,
                            }

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
            customRegisters[C] = 1
        else:
            customRegisters[C] = 0

    def gtri(self, customRegisters, A, B, C):
        if customRegisters[A] > B:
            customRegisters[C] = 1
        else:
            customRegisters[C] = 0

    def gtrr(self, customRegisters, A, B, C):
        if customRegisters[A] > customRegisters[B]:
            customRegisters[C] = 1
        else:
            customRegisters[C] = 0

    def eqir(self, customRegisters, A, B, C):
        if A == customRegisters[B]:
            customRegisters[C] = 1
        else:
            customRegisters[C] = 0

    def eqri(self, customRegisters, A, B, C):
        if customRegisters[A] == B:
            customRegisters[C] = 1
        else:
            customRegisters[C] = 0

    def eqrr(self, customRegisters, A, B, C):
        if customRegisters[A] == customRegisters[B]:
            customRegisters[C] = 1
        else:
            customRegisters[C] = 0


class Instruction:

    def __init__(self, command, A, B, C):
        self.command = command
        self.A = A
        self.B = B
        self.C = C

def readInput(fileName):
    """
    Read input file and parse it into a string
    :param fileName: name of input file
    :return: list of input file content (each line is new element)
    """
    with open(fileName, 'r') as file:

        instructionPointer = file.readline().replace("#ip ", "")

        instructionList = []
        for line in file:
            m = re.search(r"(.*) (\d+) (\d+) (\d+)", line)

            instructionList.append(Instruction(m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4))))


        return (int(instructionPointer), instructionList)

def executeCommands(instructionPointer, instructionList):
    '''

    :param instructionPointer:
    :param instructionList:
    :return:
    '''

    registers = [0, 0, 0, 0, 0, 0]
    operationsObject = Operations()


    while(True):

        #print(f"Before: {registers}")
        if registers[instructionPointer] > (len(instructionList) - 1) or registers[instructionPointer] < 0:
            break

        commandTOExecute = instructionList[registers[instructionPointer]]

        print(f"commandTOExecute. command: {commandTOExecute.command}, A:{commandTOExecute.A}, B:{commandTOExecute.B}, C:{commandTOExecute.C}")
        print(f"registers: {registers}")
        operationsObject.operationDict[commandTOExecute.command](registers, commandTOExecute.A, commandTOExecute.B, commandTOExecute.C)

        registers[instructionPointer] += 1

        #print(f"After: {registers}, InstructionPointer: {registers[instructionPointer]}")


    print(registers)

'''
def executeCommandsSecond(instructionPointer, instructionList):


    :param instructionPointer:
    :param instructionList:
    :return:


    count = 0

    #[1, 10551309, 3, 219409, 0, 2]
    #registers = [0, 10551309, 9, 5275654, 0, register5]
    registers = [1, 0, 0, 0, 0, 0]
    flag = True
    while(True):

            if count > 30 and registers[5]:
                #register5 += 1

                if registers[1]  % registers[5]  == 0 and flag:
                    #print("I am here")
                    registers[3] = int(registers[1] / registers[5])
                    flag = False
                else:
                    registers[3] = 10551308
                    flag = True
                registers[2] = 3
                registers[4] = 0

                count = 0

            operationsObject = Operations()

            #print(f"Before: {registers}")
            if registers[instructionPointer] > (len(instructionList) - 1) or registers[instructionPointer] < 0:
                break

            commandTOExecute = instructionList[registers[instructionPointer]]

            #print(f"commandTOExecute. command: {commandTOExecute.command}, A:{commandTOExecute.A}, B:{commandTOExecute.B}, C:{commandTOExecute.C}")
            #print(f"registers: {registers}")
            operationsObject.operationDict[commandTOExecute.command](registers, commandTOExecute.A, commandTOExecute.B, commandTOExecute.C)

            registers[instructionPointer] += 1

            #print(f"After: {registers}, InstructionPointer: {registers[instructionPointer]}")

            #print("")
            #time.sleep(1)

            count += 1

    print(registers)

'''

if __name__ == '__main__':


    inputTuple = readInput("input.txt")

    executeCommands(inputTuple[0], inputTuple[1])

