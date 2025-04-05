arr = [5, 6, 2, 3, 8]
ans = 0

for i in range(len(arr)):
    if arr[i]%3==0:
     ans +=1
     print(arr[i], "is divisible by 3")
    
print(ans)



arr1 = [5, 6 , 23, 46, 36, 98, 180]
ans1 = 0
 
for i in range(len(arr1)):
    if arr1[i]%3 == 0 and arr1[i]%2 == 0:
        ans += 1
        print(arr1[i], "is divisible by 6")

for i in arr1:
    if i%3 == 0 and i%2 == 0:
        ans1 += 1
        print(i, "is divisible by 6")