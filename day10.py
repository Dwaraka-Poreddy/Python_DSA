def printBoxStarPattern(m,n):
    for i in range(m):
        for j in range(n):
            print("*", end=" ")
        print()
printBoxStarPattern(3, 4)
# * * * * 
# * * * * 
# * * * * 


def printBoxStarDashPattern(m,n):
    for i in range(m):
        for j in range(n):
            if(j == n-1):
                print("*")
            else:
                print("*", end="-")
printBoxStarDashPattern(3, 4)
# *-*-*-*
# *-*-*-*
# *-*-*-*