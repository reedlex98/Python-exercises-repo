import math
def secondGrade(a, b, c, math):
    delta = b**2 + (-4)*(a)*(c)
    if delta < 0:
        return 'non exist in Real'
    elif delta == 0:
        return (-b)/(2*a)
    else:
        return [ ((-b)+math.sqrt(delta))/(2*a), ((-b)-math.sqrt(delta))/(2*a)]

print('Equation format: a.x^2 + b.x + c = 0')
a = int(input('Type a value: '))
b = int(input('Type b value: '))
c = int(input('Type c value: '))

print('X value is ', secondGrade(a, b, c, math))
