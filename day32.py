# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/description/

def minimumDifference(nums, k):
    nums.sort()
    l = 0
    ans = float("inf")
    temp = []
    for r in range(len(nums)):
        temp.append(nums[r])
        if r+1-l == k:
            tempMaxi = temp[k-1]
            tempMini = temp[0]
            temp.remove(nums[l])
            l+=1
            ans = min(ans, tempMaxi - tempMini)
    return ans
    
print(minimumDifference([90], 1))
#0
print(minimumDifference([9,4,1,7], 2))
#2
