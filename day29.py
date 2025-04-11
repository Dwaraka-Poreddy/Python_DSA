#Sub Arrays, Sub Strings

li = [1, 8, 9]
ans = []
for i in range(len(li)):
    for j in range(i, len(li)):
        temp = []
        for k in range(i, j+1):
            temp.append(li[k])
        ans.append(temp)
print(ans)
# [[1], [1, 8], [1, 8, 9], [8], [8, 9], [9]]
