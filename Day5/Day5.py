import re

def readInput(fileName):
    """
    Read input file and parse it into a string
    :param fileName: name of input file
    :return: list of input file content (each line is new element)
    """
    with open(fileName, 'r') as file:

        fileContent = file.read()

        return fileContent

def resolveUnits(inputString):
    '''
    Resolve units. From string resolve identical units with opposite polarities (remove such units)
    :param inputString: input string which will be iterated and resolved
    :return: size of resolved string 
    '''

    index = 0
    #iterate over input string by index
    while(True):

        #print(f"Curent index: {index}. Curent string: , curnet len of string: {len(inputString)}")
        #if we are at the end of the inputString leave loop
        if len(inputString) <= index + 1:
            break;

        #if current and next character are the same regardless of case check if they are of opposite polarities
        if inputString[index].lower() == inputString[index + 1].lower():

            if (inputString[index].isupper() and inputString[index + 1].islower() ) or (inputString[index].islower() and inputString[index + 1].isupper() ):
                inputString = inputString[:index] + inputString[index + 2:]
                if index > 0:
                    index -= 1
            else:
                index += 1
        #otherwise go to next character
        else:
            index += 1

        #print(f"Input string: {inputString}" )

    return inputString

def optimize(inputString):
    '''
    Calculate which unit is best to remove to get optimal result (minimal strin len)
    :param inputString: input string which will be iterated and resolved
    :return: size of resolved optimized string 
    '''

    bestOptimizedString = ''

    #iterate over all unique characters in input string
    for unit in ''.join(set(inputString.lower())):

        print(f"Curent unit: {unit}")
        stringWithoutUnit = re.sub(f'[{unit.upper()}{unit.lower()}]', '' , inputString)
        print(f"Bare unit: {stringWithoutUnit}")
        optimizedString = resolveUnits(stringWithoutUnit)
        print(f"Optimized unit: {optimizedString}")

        #if it is first optimization put its value as best
        if not bestOptimizedString:
            bestOptimizedString = optimizedString
        #if new optimized string is better than last but it as best
        elif len(optimizedString) < len(bestOptimizedString):
            bestOptimizedString = optimizedString

    return bestOptimizedString

if __name__ == '__main__':
    inputString = readInput("input.txt")
    print(inputString)

    resolvedString = resolveUnits(inputString)

    print(resolvedString)

    optimizedString = optimize(inputString)

    print(optimizedString)
    print("I am here")
    print(len(optimizedString))



