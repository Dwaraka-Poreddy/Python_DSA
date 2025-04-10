# https://leetcode.com/problems/set-mismatch/description/

def findErrorNums(nums):
    s = set()
    rep = nums[0]
    mis = nums[0]
    for i in range(len(nums)):
        if nums[i] not in s:
            s.add(nums[i])
        else:
            rep = nums[i]
    for i in range(len(nums)):
        if i+1 not in s:
            mis = i+1
            break
    return [rep, mis]
            
    
print(findErrorNums([1,2,2,4]))
# [2, 3]
print(findErrorNums([1,1]))
# [1, 2]
print(findErrorNums([3,2,2]))
# [2, 1]
print(findErrorNums([3,3,1]))
# [3, 2]