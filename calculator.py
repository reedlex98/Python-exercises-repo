def summ(a, b):
    return a+b


def sub(a, b):
    return a-b


def div(a, b):
    return a/b


def mult(a, b):
    return a*b


a = int(input('Type first number: '))
b = int(input('Type second number: '))
op = input('Type operation you want to perform: ')
if(op == '+'):
    print(summ(a, b))
elif(op == '-'):
    print(sub(a, b))
elif(op == '/'):
    print(div(a, b))
elif(op == '*'):
    print(mult(a, b))
