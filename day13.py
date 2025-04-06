def printBokkaPadinaKondaMugguPattern(m):
    for i in range(m):
        for j in range(m-i-1):
            print(" ", end="")
        for j in range(2*i+1):
            if i == m-1:
                print("*", end="")
            elif j == 0 or j == 2*i:
                print("*", end="")
            else:
                print(" ", end="")
        print() 
printBokkaPadinaKondaMugguPattern(5)
#     *
#    * *
#   *   *
#  *     *
# *********


def printBokkaPadinaReverseKondaMugguPattern(m):
    for i in range(m):
        for j in range(i):
            print(" ", end="")
        for j in range(2*(m-i-1)+1):
            if i == 0:
                print("*", end="")
            elif j == 0 or j == 2*(m-i-1):
                print("*", end="")
            else:
                print(" ", end="")
        print() 
printBokkaPadinaReverseKondaMugguPattern(5)
# *********
#  *     *
#   *   *
#    * *
#     *

def printHallowRhombusPattern(m):
    printBokkaPadinaKondaMugguPattern(m//2)
    printBokkaPadinaReverseKondaMugguPattern(m//2)

printHallowRhombusPattern(10)
#     *
#    * *
#   *   *
#  *     *
# *********
# *********
#  *     *
#   *   *
#    * *
#     *



def printNumTriangle(m):
    for i in range(m):
        for j in range(i+1):
            print(j+1, end="")
        print()
printNumTriangle(6)
# 1
# 12
# 123
# 1234
# 12345
# 123456

def printNumTriangleReverse(m):
    for i in range(m):
        for j in range(m-i-1):
            print(" ", end="")
        for j in range(i+1):
            print(j+1, end="")
        print()
printNumTriangleReverse(6)
#      1
#     12
#    123
#   1234
#  12345
# 123456

def printNumTriangleFull(m):
    for i in range(m):
        for j in range(m-i-1):
            print(" ", end="")
        for j in range(i + 1, 0, -1):
            print(j, end ="")
        for j in range(2, i+2):
            print(j, end ="")
        print()
printNumTriangleFull(6)
#      1
#     212
#    32123
#   4321234
#  543212345
# 65432123456