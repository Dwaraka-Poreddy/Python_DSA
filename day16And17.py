# https://leetcode.com/problems/maximum-difference-between-increasing-elements/description/

def maximumDifference(nums):
        lowestTillNow = nums[0]
        ans = 0
        for num in nums:
            ans = max(ans, num - lowestTillNow)
            lowestTillNow = min(lowestTillNow, num)
        return ans
 

print(maximumDifference([7,1,4,4]))
