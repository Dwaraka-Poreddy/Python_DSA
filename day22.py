# dic = { }
# print(dic)

# dic[5]=3
# dic[1]="Dwaraka"
# dic[9]="Siri"
# print(dic)
# print(dic[1])
# # print(dic[4]) #throws error as dic[5] doesn't exist

# if 6 in dic:
#     print("YES")
# else:
#     print("NO")

# print("Using for loop")
# for i in dic:
#     print(i, ":", dic[i])

#make a frequency count dictionary of the array
arr = [1, 5, 8, 0, 1, 8, 1, 5, 1]
dic = {}
for i in range(len(arr)):
    if arr[i] in dic:
        dic[arr[i]]+=1
    else:
        dic[arr[i]]=1

print(dic)