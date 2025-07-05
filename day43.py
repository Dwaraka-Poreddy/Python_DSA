# https://leetcode.com/problems/sort-colors/description/

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        start = 0
        mid = 0
        end = l - 1
        while mid <= end:
            if nums[mid] == 0:
                nums[start], nums[mid] = nums[mid], nums[start]
                start += 1
                mid += 1
            elif nums[mid] == 2:
                nums[end], nums[mid] = nums[mid], nums[end]
                end -= 1
            else:
                mid += 1

# https://www.geeksforgeeks.org/problems/equilibrium-point-1587115620/1

class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        ts = sum(arr)
        cs = 0
        for i,num in enumerate(arr):
            ts -= num
            if cs == ts:
                return i
            cs += num
        return -1


# https://leetcode.com/problems/most-frequent-even-element/description/

class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dt = {}
        for num in nums:
            if num % 2 == 0:
                if num in dt:
                    dt[num] += 1
                else:
                    dt[num] = 1
        if not dt:
            return -1
        maxCt = 1
        maxEl = float('+inf')
        for i in dt:
            if dt[i] == maxCt:
                maxEl = min(i, maxEl)
            if dt[i] > maxCt:
                maxCt = dt[i]
                maxEl = i
        return maxEl

# single pass
class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dt = {}
        maxCt = 0
        maxEl = float('+inf')
        for num in nums:
            if num % 2 == 0:
                if num in dt:
                    dt[num] += 1
                else:
                    dt[num] = 1
                if dt[num] > maxCt or dt[num] == maxCt and  num < maxEl:
                    maxEl = num
                    maxCt = dt[num]
        return -1 if maxCt == 0 else maxEl

# https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos = []
        neg = []
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        for i in range(len(pos)):
            nums[2*i] = pos[i]
        for i in range(len(neg)):
            nums[2*i + 1] = neg[i]
        return nums

        
class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0] * len(nums)
        pos = 0
        neg = 1
        for num in nums:
            if num > 0:
                res[pos] = num
                pos += 2
            else:
                res[neg] = num
                neg += 2
        return res

# https://leetcode.com/problems/factorial-trailing-zeroes/description/

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        i = 5
        while n/i >= 1:
            ans += n/i
            i = i * 5
        return ans
        