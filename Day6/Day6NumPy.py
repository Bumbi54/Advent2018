import numpy as np


def readInput(fileName):
    """
    Read input file with numpy
    :param fileName: name of input file
    :return: numpy object that is 2D array with coordinates from input file
    """
    return np.loadtxt(fileName, delimiter=", ")






if __name__ == '__main__':

    list_Points = readInput("input.txt")
    print(type(list_Points))
    print(list_Points)

    print(list_Points.min(axis=0) )

    print(list_Points.shape)
