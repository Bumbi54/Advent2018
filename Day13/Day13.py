import re
import time

def readInput(fileName):
    """
    Read input file and parse it into a string
    :param fileName: name of input file
    :return: list of input file content (each line is new element)
    """
    with open(fileName, 'r') as file:

        fileContent = file.read().split("\n")

        grid = []
        for line in fileContent:
            grid.append(list(line))

        return grid

def findCarts(grid):
    '''
    
    :param grid: 
    :return: 
    '''

    cartLocation = {}

    i = 0
    for row in grid:
        j = 0
        for location in row:

            if location in ['v', '^','<', '>']:
                print(location)
                cartLocation[(i,j)] = (location,0)

                if location in ['v', '^']:
                    grid[i][j] = '|'
                elif  location in ['<', '>']:
                    grid[i][j] = '-'
            j += 1
        i += 1

    print(cartLocation)
    print(grid)
    #moveCarts(cartLocation, grid)
    moveCartsSecond(cartLocation, grid)



def moveCarts(cartLocation, grid):
    '''
    
    :param cartLocation: 
    :param grid: 
    :return: 
    '''

    noCollision = True
    while(noCollision):
        #time.sleep(1)
        #print(cartLocation)
        sortedCarts = sorted(list(cartLocation.keys()))
        for x,y in sortedCarts:
            #print(x,y)

            newX = x
            newY = y
            if cartLocation[(x,y)][0] == '>':
                newY = y + 1
            elif cartLocation[(x,y)][0] == '<':
                newY = y - 1
            elif cartLocation[(x,y)][0] == '^':
                newX = x - 1
            elif cartLocation[(x,y)][0] == 'v':
                newX = x + 1

            #print(f"New coo at: ({newX},{newY}, {x}{y} cartLocation {cartLocation})")
            if (newX, newY) in cartLocation.keys():
                print(f"Collision at: ({newX},{newY}, cartLocation {cartLocation})")
                return

            else:
                cartValue = cartLocation[(x,y)]
                del cartLocation[(x,y)]
                nextHop = grid[newX][newY]
                #print(f"nextHop {nextHop}")

                if nextHop == '\\' and cartValue[0] == '^':
                    cartLocation[(newX, newY)] = ('<', cartValue[1])
                elif nextHop == '\\' and cartValue[0] == '>':
                    cartLocation[(newX, newY)] = ('v', cartValue[1])
                elif nextHop == '\\' and cartValue[0] == 'v':
                    cartLocation[(newX, newY)] = ('>', cartValue[1])
                elif nextHop == '\\' and cartValue[0] == '<':
                    cartLocation[(newX, newY)] = ('^', cartValue[1])
                elif nextHop == '-' and cartValue[0] == '<':
                    cartLocation[(newX, newY)] = ('<', cartValue[1])
                elif nextHop == '-' and cartValue[0] == '>':
                    cartLocation[(newX, newY)] = ('>', cartValue[1])
                elif nextHop == '/' and cartValue[0] == 'v':
                    cartLocation[(newX, newY)] = ('<', cartValue[1])
                elif nextHop == '/' and cartValue[0] == '>':
                    cartLocation[(newX, newY)] = ('^', cartValue[1])
                elif nextHop == '/' and cartValue[0] == '^':
                    cartLocation[(newX, newY)] = ('>', cartValue[1])
                elif nextHop == '/' and cartValue[0] == '<':
                    cartLocation[(newX, newY)] = ('v', cartValue[1])
                elif nextHop == '|' and cartValue[0] == 'v':
                    cartLocation[(newX, newY)] = ('v', cartValue[1])
                elif nextHop == '|' and cartValue[0] == '^':
                    cartLocation[(newX, newY)] = ('^', cartValue[1])
                elif nextHop == '+':

                    if cartValue[1] == 0:
                        if cartValue[0] == '<':
                            cartLocation[(newX, newY)] = ('v', 1)
                        elif cartValue[0] == 'v':
                            cartLocation[(newX, newY)] = ('>', 1)
                        elif cartValue[0] == '>':
                            cartLocation[(newX, newY)] = ('^', 1)
                        if cartValue[0] == '^':
                            cartLocation[(newX, newY)] = ('<', 1)

                    elif cartValue[1] == 1:
                            cartLocation[(newX, newY)] = (cartValue[0], 2)

                    if cartValue[1] == 2:
                        if cartValue[0] == '<':
                            cartLocation[(newX, newY)] = ('^', 0)
                        elif cartValue[0] == 'v':
                            cartLocation[(newX, newY)] = ('<', 0)
                        elif cartValue[0] == '>':
                            cartLocation[(newX, newY)] = ('v', 0)
                        elif cartValue[0] == '^':
                            cartLocation[(newX, newY)] = ('>', 0)

        #noCollision = False


def moveCartsSecond(cartLocation, grid):
    '''

    :param cartLocation: 
    :param grid: 
    :return: 
    '''

    noCollision = True
    while (noCollision):
        # time.sleep(1)
        # print(cartLocation)
        if len(cartLocation.keys()) == 1:
            print(f"Last cart: {cartLocation}")
            return

        sortedCarts = sorted(list(cartLocation.keys()))
        for x, y in sortedCarts:
            # print(x,y)

            if cartLocation.get((x, y)):
                newX = x
                newY = y
                if cartLocation[(x, y)][0] == '>':
                    newY = y + 1
                elif cartLocation[(x, y)][0] == '<':
                    newY = y - 1
                elif cartLocation[(x, y)][0] == '^':
                    newX = x - 1
                elif cartLocation[(x, y)][0] == 'v':
                    newX = x + 1

                # print(f"New coo at: ({newX},{newY}, {x}{y} cartLocation {cartLocation})")
                if (newX, newY) in cartLocation.keys():
                    print(f"Collision at: ({newX},{newY}, cartLocation {cartLocation})")
                    del cartLocation[(newX, newY)]
                    del cartLocation[(x, y)]

                else:
                    cartValue = cartLocation[(x, y)]
                    del cartLocation[(x, y)]
                    nextHop = grid[newX][newY]
                    # print(f"nextHop {nextHop}")

                    if nextHop == '\\' and cartValue[0] == '^':
                        cartLocation[(newX, newY)] = ('<', cartValue[1])
                    elif nextHop == '\\' and cartValue[0] == '>':
                        cartLocation[(newX, newY)] = ('v', cartValue[1])
                    elif nextHop == '\\' and cartValue[0] == 'v':
                        cartLocation[(newX, newY)] = ('>', cartValue[1])
                    elif nextHop == '\\' and cartValue[0] == '<':
                        cartLocation[(newX, newY)] = ('^', cartValue[1])
                    elif nextHop == '-' and cartValue[0] == '<':
                        cartLocation[(newX, newY)] = ('<', cartValue[1])
                    elif nextHop == '-' and cartValue[0] == '>':
                        cartLocation[(newX, newY)] = ('>', cartValue[1])
                    elif nextHop == '/' and cartValue[0] == 'v':
                        cartLocation[(newX, newY)] = ('<', cartValue[1])
                    elif nextHop == '/' and cartValue[0] == '>':
                        cartLocation[(newX, newY)] = ('^', cartValue[1])
                    elif nextHop == '/' and cartValue[0] == '^':
                        cartLocation[(newX, newY)] = ('>', cartValue[1])
                    elif nextHop == '/' and cartValue[0] == '<':
                        cartLocation[(newX, newY)] = ('v', cartValue[1])
                    elif nextHop == '|' and cartValue[0] == 'v':
                        cartLocation[(newX, newY)] = ('v', cartValue[1])
                    elif nextHop == '|' and cartValue[0] == '^':
                        cartLocation[(newX, newY)] = ('^', cartValue[1])
                    elif nextHop == '+':

                        if cartValue[1] == 0:
                            if cartValue[0] == '<':
                                cartLocation[(newX, newY)] = ('v', 1)
                            elif cartValue[0] == 'v':
                                cartLocation[(newX, newY)] = ('>', 1)
                            elif cartValue[0] == '>':
                                cartLocation[(newX, newY)] = ('^', 1)
                            if cartValue[0] == '^':
                                cartLocation[(newX, newY)] = ('<', 1)

                        elif cartValue[1] == 1:
                            cartLocation[(newX, newY)] = (cartValue[0], 2)

                        if cartValue[1] == 2:
                            if cartValue[0] == '<':
                                cartLocation[(newX, newY)] = ('^', 0)
                            elif cartValue[0] == 'v':
                                cartLocation[(newX, newY)] = ('<', 0)
                            elif cartValue[0] == '>':
                                cartLocation[(newX, newY)] = ('v', 0)
                            elif cartValue[0] == '^':
                                cartLocation[(newX, newY)] = ('>', 0)

                                # noCollision = False


if __name__ == '__main__':
    grid = readInput("input.txt")

    print(grid)


    findCarts(grid)

