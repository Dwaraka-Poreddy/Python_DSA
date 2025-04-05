mat = [[3, 4, 5], [6, 7, 8], [9, 10, 11]]


print(mat)


for arr in mat:
    for i in arr:
        print(i)


for l in range(len(mat)):
    for m in range(len(mat[l])):
        print(mat[l][m])