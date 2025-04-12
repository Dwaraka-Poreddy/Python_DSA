# https://leetcode.com/problems/array-partition/description/

def arrayPairSum(nums):
    nums.sort()
    ans = 0
    for i in range(0, len(nums), 2):
        ans+=nums[i]
    return ans
    
print(arrayPairSum([1,4,3,2]))
#4
print(arrayPairSum([6,2,6,5,1,2]))
#9



# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/description/
def minimumCost(cost):
    length = len(cost)
    cost.sort()
    took = 0
    ans = 0
    for i in range(length-1, -1, -1):
        if(took == 2):
           took = 0
        else:
            ans += cost[i]
            took+=1
    return ans
    
print(minimumCost([1,2,3]))
#5
print(minimumCost([6,5,7,9,2,2]))
#23
print(minimumCost([3, 3, 3, 1]))
#7
print(minimumCost([5, 5]))
#10
print(minimumCost([6]))
#6