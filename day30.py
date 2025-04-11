#Find the highest sum of subarray of length 3 in below array. (Worst O(n^3))

li = [5, 9, 1, 8, 7]
maxi_sub_arr_sum = 0
sub_arr_len = 3
for i in range(len(li)):
    for j in range(i, len(li)):
        temp = []
        tempSum = 0
        for k in range(i, j+1):
            tempSum += li[k]
            temp.append(li[k])
        if(len(temp) == sub_arr_len):
            maxi_sub_arr_sum = max(maxi_sub_arr_sum, tempSum)
print(maxi_sub_arr_sum)
#18

#Using sliding window main approach (BEST O(n))
li = [5, 9, 1, 8, 7]
sub_arr_len = 3
l = 0
ans = 0
temp = 0
for r in range(len(li)):
    temp += li[r]
    if r-l == sub_arr_len:
        temp-=li[l]
        l+=1
    if r-l+1 == sub_arr_len:
        ans = max(ans, temp)

print(ans)
#18


#Using sliding window another approach (O(n*m))
li = [5, 9, 1, 8, 7]
max_sum = 0
sub_arr_len = 3
for i in range(0, len(li)-sub_arr_len+1):
    temp_sum = 0
    for j in range(sub_arr_len):
        temp_sum += li[i+j]
    max_sum = max(max_sum, temp_sum)

print(max_sum)
#18