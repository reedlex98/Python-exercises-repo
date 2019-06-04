from random import randint

def createList(size):
    newList = []
    for i in range(0,size):
        newList.append(randint(0,size))
    return newList
    