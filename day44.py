# https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        maxL = 1
        l = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            if nums[i] == nums[i - 1]+1:
                l += 1
                maxL = max(maxL, l)
            else:
                l = 1
        return maxL

# https://leetcode.com/problems/trapping-rain-water/description/

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = len(height)
        lm = [0]*l
        lmax = height[0]
        for i in range(1, l):
            lm[i] = lmax
            lmax = max(lmax, height[i])
        rm = [0]*l
        rmax = height[-1]
        for i in range(l-2, -1, -1):
            rm[i] = rmax
            rmax = max(rmax, height[i])
        ans = 0
        for i in range(l-1):
            cap = max(0, (min(lm[i], rm[i]) - height[i]))
            ans += cap
        return ans

        
# https://leetcode.com/problems/search-in-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        dum = root

        while dum:
            if dum.val == val:
                return dum
            elif dum.val > val:
                dum = dum.left
            else:
                dum = dum.right 
        

# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)
        s = 0
        e = l - 1
        while s <= e:
            m = (s + e)//2
            if nums[m] == target:
                return m
            elif nums[s] <= nums[m]:
                if target >= nums[s] and target < nums[m]:
                    e = m - 1
                else:
                    s = m + 1
            else:
                if target > nums[m] and target <= nums[e]:
                    s = m + 1
                else:
                    e = m - 1
        return -1
 

