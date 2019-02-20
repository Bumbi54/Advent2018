import re
from collections import deque


def createRecipe(puzzleInput):
    '''

    :return:
    '''

    firstElf = (0,3)
    secondElf = (1,7)

    recipeList = [3, 7]

    for step in range(puzzleInput + 10):

        newRecipes = firstElf[1] + secondElf[1]
        recipeList = recipeList + list(map(int,str(newRecipes)))

        firstElfPostion = (firstElf[1] + firstElf[0] + 1) % len(recipeList)
        firstElf = (firstElfPostion ,recipeList[firstElfPostion])

        secondElfPostion = (secondElf[1] + secondElf[0] + 1) % len(recipeList)
        secondElf = (secondElfPostion ,recipeList[secondElfPostion])

        if step % 10000 == 0:
            print(f"Recipe list: {recipeList}. First elf: {firstElf}. Second elf: {secondElf}")

    print(f"Solution: {recipeList[puzzleInput:puzzleInput+10]}")

def createRecipeSecond(puzzleInput):
    '''

    :return:
    '''

    firstElf = (0,3)
    secondElf = (1,7)

    recipeList = [3, 7]
    recipeString = '0' * (len(puzzleInput) - 2) + '37'

    while(True):

        newRecipes = firstElf[1] + secondElf[1]
        recipeList = recipeList + list(map(int,str(newRecipes)))

        firstElfPostion = (firstElf[1] + firstElf[0] + 1) % len(recipeList)
        firstElf = (firstElfPostion ,recipeList[firstElfPostion])

        secondElfPostion = (secondElf[1] + secondElf[0] + 1) % len(recipeList)
        secondElf = (secondElfPostion ,recipeList[secondElfPostion])

        recipeString = recipeString[len(str(newRecipes)):] + str(newRecipes)
        #print(recipeString,puzzleInput)

        if puzzleInput == recipeString:
            print(recipeString)

            print(f" {puzzleInput} first appears after {len(recipeList) - len(puzzleInput)} recipes. +-1 ")
            break



    #print(f"Solution: {recipeList[puzzle
    # Input:puzzleInput+10]}")

if __name__ == "__main__":

    #createRecipe(puzzleInput = 540561)

    createRecipeSecond(puzzleInput='540561')



