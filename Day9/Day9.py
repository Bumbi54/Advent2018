import re
import time
import collections



def marbleMeThis(players, marbleCount):
    '''
    
    :param players: 
    :param marbleCount: 
    :return: 
    '''

    marbleList = collections.deque()
    marbleList.append(0)
    playersScore = {}

    for marble in range(1, marbleCount + 1):


        if marble % 23 == 0:
            #print(f"Before: {marbleList}")
            result = marble
            result = result + marbleList[-2 - 7]
            del marbleList[-2 - 7]
            marbleList.rotate(6)

            if not playersScore.get(marble % players):
                playersScore[marble % players] = result
            else:
                playersScore[marble % players] += result

            #print(f"Step: {marble}")
            #print(f"After: {marbleList}")
        else:
            #print(f"Before: {marbleList}")

            marbleList.append(marble)
            marbleList.rotate(-1)

            #print(f"Step: {marble}")
            #print(f"After: {marbleList}")

    print(playersScore)
    print(max(playersScore.values()))

if __name__ == '__main__':

    marbleMeThis(447, 7151000)


