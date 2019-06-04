def moda(userList):
    recurrencyList = []
    for value in userList:
        cont = 0
        for valueComparative in userList:
            if value == valueComparative:
                cont+=1
        recurrencyList.append(cont)
    return userList[recurrencyList.index(max(recurrencyList))]

def media(userList):
    return sum(userList)/len(userList)

def mediana(userList):
    return sorted(userList)[int(len(sorted(userList))/2)]