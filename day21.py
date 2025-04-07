#Python inbuilt Sort
print("Using 'sorted'")
lis = [4, 5, 7, 1, 3, 2]
print(lis)
temp = sorted(lis)
print(temp)
print(lis)

print("Using '.sort()'")
listy = [4, 5, 7, 1, 3, 2]
print(listy)
listy.sort()
print(listy)

print("Using '.sort(reverse = True)'")
listy1 = [4, 5, 7, 1, 3, 2]
print(listy)
listy.sort(reverse = True)
print(listy)



#Bubble Sort
# li = [7, 1, 2, 3, 4, 5, 6]
li = [10, 1, 2, 6, 4]
print("Using 'Bubble Sort Algo'")
print(li)

for i in range(len(li)-1, 0, -1):
    for j in range(i):
        didSwap = False
        if li[j]>li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]
            didSwap = True
    print(li)
    if didSwap == False:
        break


# Dry run
# j = 0
# if(li[j]>li[j+1]):
#     li[j], li[j+1] = li[j+1], li[j]
# print(li)
# j = 1
# if(li[j]>li[j+1]):
#     li[j], li[j+1] = li[j+1], li[j]
# print(li)
# j = 2
# if(li[j]>li[j+1]):
#     li[j], li[j+1] = li[j+1], li[j]
# print(li)
# j = 3
# if(li[j]>li[j+1]):
#     li[j], li[j+1] = li[j+1], li[j]
# print(li)

# j = 0
# if(li[j]>li[j+1]):
#     li[j], li[j+1] = li[j+1], li[j]
# print(li)
# j = 1
# if(li[j]>li[j+1]):
#     li[j], li[j+1] = li[j+1], li[j]
# print(li)
# j = 2
# if(li[j]>li[j+1]):
#     li[j], li[j+1] = li[j+1], li[j]
# print(li)

# j = 0
# if(li[j]>li[j+1]):
#     li[j], li[j+1] = li[j+1], li[j]
# print(li)
# j = 1
# if(li[j]>li[j+1]):
#     li[j], li[j+1] = li[j+1], li[j]
# print(li)

# j = 0
# if(li[j]>li[j+1]):
#     li[j], li[j+1] = li[j+1], li[j]
# print(li)
