def printKondaMugguPattern(m):
    for i in range(m):
        for j in range(m-i-1):
            print(" ", end="")
        for j in range(2*i+1):
             print("*", end="")
        print() 
printKondaMugguPattern(6)
#      *
#     ***
#    *****
#   *******
#  *********
# ***********

def printReverseKondaMugguPattern(m):
    for i in range(m):
        for j in range(i):
            print(" ", end="")
        for j in range(2*(m-i-1)+1):
            print("*", end="")
        print() 
printReverseKondaMugguPattern(6)
# ***********
#  *********
#   *******
#    *****
#     ***
#      *

def printRhombusPattern(m):
    printKondaMugguPattern(m//2)
    printReverseKondaMugguPattern(m//2)
printRhombusPattern(6)
#   *
#  ***
# *****
# *****
#  ***
#   *