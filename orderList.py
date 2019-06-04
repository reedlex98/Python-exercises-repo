from random import randint
def createList(size,randint):
    newList = []
    for i in range(0,size):
        newList.append(randint(0,size))
    return newList
def orderList(userList):
    return sorted(userList)

print(orderList(createList(3,randint)))