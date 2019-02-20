import re
from collections import deque
from copy import copy, deepcopy
import time

import math
class Group:


    def __init__(self, units, hitpoints, dmgDone, dmgType, initiative, type):

        self.units = units
        self.hitpoints = hitpoints
        self.dmgDone = dmgDone
        self.dmgType = dmgType
        self.initiative = initiative
        self.type = type
        self.immunities = []
        self.weakness = []

    def resolveWeaknessImmunities(self, unParsedString):
        if ";" in unParsedString:
            m = re.search("immune to (.+); weak to (.+)", unParsedString)
            if not m:
                m = re.search("weak to (.+); immune to (.+)", unParsedString)
                self.weakness = m.group(1).split(", ")
                self.immunities = m.group(2).split(", ")
            else:
                self.weakness = m.group(2).split(", ")
                self.immunities = m.group(1).split(", ")
        else:
            m = re.search("weak to (.+)", unParsedString)
            if m:
                self.weakness = m.group(1).split(", ")
            m = re.search("immune to (.+)", unParsedString)
            if m:
                self.immunities = m.group(1).split(", ")

        #print(self.weakness, self.immunities)

    def effectivePower(self):

        return self.units * self.dmgDone


def readInput(fileName):
    """
    Read input file and parse it into a string
    :param fileName: name of input file
    :return: list of input file content (each line is new element)
    """
    with open(fileName, 'r') as file:

        fileContent = file.read()

        return fileContent.split("\n")

def parseGroups(inputList):
    '''
    
    :param inputList: 
    :return: 
    '''

    groupList = []

    currentType = 0

    for line in inputList[1:]:

        if line == '':
            currentType = 1
        elif ("Immune" not in line) and ("Infection" not in line):
            if "(" in line:
                m = re.search("(\d+) units each with (\d+) hit points \((.+)\) with an attack that does (\d+) (.+) damage at initiative (\d+)", line)

                newGroup = Group(int(m.group(1)), int(m.group(2)), int(m.group(4)), m.group(5), int(m.group(6)), currentType)
                newGroup.resolveWeaknessImmunities(m.group(3))

                groupList.append(newGroup)

            else:
                    m = re.search("(\d+) units each with (\d+) hit points with an attack that does (\d+) (.+) damage at initiative (\d+)", line)

                    newGroup = Group(int(m.group(1)), int(m.group(2)), int(m.group(3)), m.group(4), int(m.group(5)), currentType)

                    groupList.append(newGroup)

    return groupList

def combat(groupList):
    '''

    :param groupList:
    :return:
    '''

    #print([(group.units, group.weakness) for group in groupList])

    while(True):
        #targeting
        groupsSorted =  sorted(groupList, key=lambda group: (group.effectivePower(), group.initiative), reverse=True)
        combatGroup = []

        #print([group.effectivePower() for group in groupsSorted])
        #print([group.initiative for group in groupsSorted])
        for group in groupsSorted[:]:
            dmgToGroup = []
            index = 0
            for target in groupsSorted:
                if group.dmgType in target.immunities or group.type == target.type:
                    index += 1
                    continue
                else:
                    potentialDmg = group.effectivePower()

                    if group.dmgType in target.weakness:
                        potentialDmg *= 2

                    dmgToGroup.append((index, potentialDmg))

                index += 1

            if dmgToGroup:
                chosenTarget = max(dmgToGroup, key= lambda  x: x[1])
                combatGroup.append( (group, groupsSorted[chosenTarget[0]] ))
                groupsSorted.pop(chosenTarget[0])


        combatGroup = sorted(combatGroup, key=lambda group: group[0].initiative, reverse=True)

        #resolve combat
        for attacker, target in combatGroup:

            if attacker.units > 0:
                if attacker.dmgType in target.immunities or attacker.type == target.type:
                    dmg = 0
                else:
                    dmg = attacker.effectivePower()

                    if attacker.dmgType in target.weakness:
                        dmg *= 2

                target.units = math.ceil((target.units * target.hitpoints - dmg) / target.hitpoints)

                if target.units <= 0:
                    groupList.remove(target)

        noImmune = True
        noInfection  = True

        for group in groupList:
            if group.type == 0:
                noImmune = False
            elif group.type == 1:
                noInfection = False
        if noImmune or noInfection:
            break

    print([group.units for group in groupList])
    print(sum([group.units for group in groupList]))


def boostedCombat(groupList):
    '''

    :param groupList:
    :return:
    '''

    #print([(group.units, group.weakness) for group in groupList])

    while(True):
        #targeting
        groupsSorted =  sorted(groupList, key=lambda group: (group.effectivePower(), group.initiative), reverse=True)
        combatGroup = []

        #print([group.effectivePower() for group in groupsSorted])
        #print([group.initiative for group in groupsSorted])
        for group in groupsSorted[:]:
            dmgToGroup = []
            index = 0
            for target in groupsSorted:
                if group.dmgType in target.immunities or group.type == target.type:
                    index += 1
                    continue
                else:
                    potentialDmg = group.effectivePower()

                    if group.dmgType in target.weakness:
                        potentialDmg *= 2

                    dmgToGroup.append((index, potentialDmg))

                index += 1

            if dmgToGroup:
                chosenTarget = max(dmgToGroup, key= lambda  x: x[1])
                combatGroup.append( (group, groupsSorted[chosenTarget[0]] ))
                groupsSorted.pop(chosenTarget[0])


        combatGroup = sorted(combatGroup, key=lambda group: group[0].initiative, reverse=True)

        #resolve combat
        flagHurt = False
        for attacker, target in combatGroup:

            if attacker.units > 0:
                if attacker.dmgType in target.immunities or attacker.type == target.type:
                    dmg = 0
                else:
                    dmg = attacker.effectivePower()

                    if attacker.dmgType in target.weakness:
                        dmg *= 2

                beforeDmg = target.units
                target.units = math.ceil((target.units * target.hitpoints - dmg) / target.hitpoints)

                if target.units < beforeDmg:
                    flagHurt = True

                if target.units <= 0:
                    groupList.remove(target)

        if not flagHurt:
            break

        noImmune = True
        noInfection  = True

        for group in groupList:
            if group.type == 0:
                noImmune = False
            elif group.type == 1:
                noInfection = False
        if noImmune or noInfection:
            break

    #if len([group.type for group in groupList if group.type == 0]) == len(groupList) :
    print([(group.units, group.type) for group in groupList])
    print(sum([group.units for group in groupList]))

if __name__ == "__main__":


    for boost in range(0,60000):
        inputList = readInput("input.txt")
        print(boost)

        groupList = parseGroups(inputList)

        for group in groupList:

            if group.type == 0:
                group.dmgDone += boost

        boostedCombat(groupList)

