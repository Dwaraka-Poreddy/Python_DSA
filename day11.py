def printSquareBokkaPattern(m,n):
    for i in range(m):
        for j in range(n):
            if(i == 0 or i == m-1 or j == 0 or j == n-1):
                print("*", end="")
            else:
                print(" ", end="")
        print()
printSquareBokkaPattern(5, 5)
# *****
# *   *
# *   *
# *   *
# *****

def printBikeStandPattern(m, p):
    for i in range(m):
        for j in range(m-i-1):
             print(" ", end="")
        for k in range(p):
             print("-", end="")
        print()
printBikeStandPattern(6, 5)
#      ****
#     ****
#    ****
#   ****
#  ****
# ****


def printReverseBikeStandPattern(m, p):
    for i in range(m):
        for j in range(i):
             print(" ", end="")
        for k in range(p):
             print("*", end="")
        print()
printReverseBikeStandPattern(6, 4)
# ****
#  ****
#   ****
#    ****
#     ****
#      ****