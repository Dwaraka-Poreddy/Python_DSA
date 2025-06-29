# https://leetcode.com/problems/next-greater-element-ii/description/

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        dict1 = {}
        ans = []
        for num in reversed(nums):
            while stack and num >= stack[-1]:
                stack.pop()
            stack.append(num)
        for i in reversed(range(len(nums))):
            num = nums[i]
            while stack and num >= stack[-1]:
                stack.pop()
            if not stack:
                dict1[i] = -1
            else:
                dict1[i] = stack[-1]
            stack.append(num)
        ans = [-1]*len(nums)
        for i in dict1:
            ans[i] = dict1[i]
        return ans     

# https://leetcode.com/problems/binary-search/
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
        
# https://leetcode.com/problems/search-insert-position/

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while(left <= right):
            middle = (right + left)//2

            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
        return   left
# https://leetcode.com/problems/first-bad-version/description/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n

        while start <= end:
            middle = (start + end) // 2
            if not isBadVersion(middle):
                start = middle + 1
            else:
                end = middle - 1
        return end + 1

# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def search(x):
            start = 0 
            end = len(nums) - 1
        
            while(start <= end):
                middle = (start + end) // 2
                if nums[middle] > x:
                    end = middle - 1
                    
                else:
                    start = middle + 1
            return end
        lo = search(target-1)+1
        hi = search(target)
        if lo <= hi:
            return [lo, hi]
        return [-1, -1]

# OR

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def search(x):
            start = 0 
            end = len(nums) - 1
        
            while(start <= end):
                middle = (start + end) // 2
                if nums[middle] < x:
                    start = middle + 1
                else:
                    end = middle - 1
            return start
        lo = search(target)
        hi = search(target+1)-1
        if lo <= hi:
            return [lo, hi]
        return [-1, -1]

# https://leetcode.com/problems/valid-perfect-square/submissions/1679038014/

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        start = 1
        end = num // 2
        found = False

        while(start <= end):
            middle = (start + end) // 2
            ms = middle * middle
            if ms == num:
                found = True
                break
            elif ms > num:
                end = middle - 1
            else:
                start = middle + 1
        return found

# https://leetcode.com/problems/sqrtx/description/

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        start = 1
        end = x//2
        while(start <= end):
            middle = (start + end) // 2
            ms = middle * middle
            if ms == x:
                return middle
            elif ms > x:
                end = middle - 1
            else:
                start = middle + 1
        return end
        

# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if (target) >= (letters[-1]) or (target) < (letters[0]):
            return letters[0]
        start = 0
        end = len(letters) - 1
        while start <= end:
            mid = (start + end) // 2
            if target >= letters[mid]:
                start = mid + 1
            elif target < letters[mid]:
                end = mid - 1
        return letters[start]

# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/

class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        s = 0
        e = len(arr) - 1
        while (s < e):
            m = (s + e) // 2
            if arr[m] < arr[m+1]:
                s = m + 1
            elif arr[m] > arr[m+1]:
                e = m
        return s

# https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 1
        e = n
        while (s <= e):
            m = (s + e) // 2
            if guess(m) == 0:
                return m
            elif guess(m) == -1:
                e = m - 1
            else:
                s = m + 1
        
# https://leetcode.com/problems/arranging-coins/description/

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 1
        e = n
        c = 0
        while s <= e:
            m = (s + e) // 2
            k = m*(m+1)//2
            if k <= n:
                c = m
                s = m+1
            else:
                e = m - 1
        return c
        
        