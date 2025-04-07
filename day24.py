# https://leetcode.com/problems/number-of-good-pairs/description/

def numIdenticalPairs(nums):
    dic = {}
    for num in nums:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
    ans = 0
    for i in dic:
        ans += dic[i]*(dic[i]-1)/2
    return ans

numIdenticalPairs([1,2,3,1,1,3])
# 4