
import time




def findRegister():

    b = 0
    e = b | 65536
    b = 12772194

    while True:
        d = e & 255
        b = b + d
        b = b & 16777215
        b = b * 65899
        b = b & 16777215

        if e < 256:
            print(f"Uspijeh d:{d}")
            print(f"Uspijeh e:{e}")
            print(f"Uspijeh b:{b}")
            return
        e = e // 256


def findRegister2():

    listOfPossibleValuies =[]
    b = 0
    while True:
        e = b | 65536
        b = 12772194

        while True:
            d = e & 255
            b = b + d
            b = b & 16777215
            b = b * 65899
            b = b & 16777215

            if e < 256:
                if b in listOfPossibleValuies:
                    #listOfPossibleValuies.append(b)
                    print(listOfPossibleValuies)
                    return
                listOfPossibleValuies.append(b)
                break

            e = e // 256

if __name__ == '__main__':
    findRegister()
    findRegister2()