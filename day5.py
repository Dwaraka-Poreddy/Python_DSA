def printNameNTimes(name, n):
    for i in range(n):
        print(name)
    
printNameNTimes("Dwaraka", 3)

def addTwoNumbers(a, b):
    return a+b

res = addTwoNumbers(12, 18)
print(res)


def printMathTable(n):
    for i in range(1, 11):
        print(n, "*", i, "=", n*i)
        print(str(n)+" * "+str(i)+" = "+str(n*i))
        print(f"{n} * {i} = {n*i}")

printMathTable(3)