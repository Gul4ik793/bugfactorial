def getSum(x, y):
    return x + y
def getDiff(x, y):
    return x - y
def getMult(x, y):
    return x * y
def getDiv(x, y):
    if y == 0:
        return None
    return x / y
    
def calc(a, b):
   print ("результат сложения", getSum(a, b))
   print ("результат вычитания", getDiff(a, b))
   print ("результат умножения", getMult(a, b))
   print ("результат деления", getDiv(a, b))

calc(1, 10)
