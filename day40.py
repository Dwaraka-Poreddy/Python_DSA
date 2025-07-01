# https://leetcode.com/problems/clumsy-factorial/

import math
class Solution(object):
    def clumsy(self, n):
        """
        :type n: int
        :rtype: int
        """
        stack = [n]
        n -= 1
        index = 0

        while n > 0:
            if index % 4 == 0:
                stack[-1] = stack[-1] * n
            elif index % 4 == 1:
                stack[-1] = int(stack[-1] / float(n))
            elif index % 4 == 2:
                stack.append(n)
            else:
                stack.append(-n)

            index += 1
            n -= 1
        return sum(stack)
        

# https://leetcode.com/problems/two-sum/description/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dt = {}
        for i, num in enumerate(nums):
            c = target - num
            if c in dt:
                return [dt[c], i]
            else:
                dt[num] = i
        
# https://leetcode.com/problems/alternating-digit-sum/description/

class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = []
        while n > 0:
            a.append(n % 10)
            n//=10
        a.reverse()
        ans = 0
        c = True
        for num in a:
            if c:
                ans += num
            else:
                ans -= num
            c = not c
        return ans

class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n:
            res = n % 10 - res
            n //= 10
        return res

# https://leetcode.com/problems/count-the-digits-that-divide-a-number/description/

class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        ans = 0
        z = num
        while num:
            k = num % 10
            if z % k == 0:
                ans += 1
            num = num//10
        return ans

# https://leetcode.com/problems/running-sum-of-1d-array/description/

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        sum = 0
        for i in range(len(nums)):
            sum = sum + nums[i]
            ans.append(sum)
        return ans

# https://leetcode.com/problems/get-maximum-in-generated-array/description/

#iterative approach
class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        nums = [0] * (n + 1)
        nums[0]=0
        nums[1]=1
        ans = 1
        for i in range(2, n+1):
            if i % 2 == 0:
                nums[i]= nums[i//2]
            else:
                nums[i] = nums[i //2] + nums[i//2 + 1]
            ans = max(ans, nums[i])
        return ans
        

#recursive approach
class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        memo = {}
        def get(i):
            if i in memo:
                return memo[i]
            if i == 0:
                memo[0] = 0
            elif i == 1:
                memo[1] = 1
            elif i % 2 == 0:
                memo[i]= get(i/2)
            else:
                memo[i]=get(i//2) + get(i//2 + 1)
            return memo[i]
        ans = 0
        for i in range(n + 1):
            ans = max(ans, get(i))
        return ans
        
# https://leetcode.com/problems/add-digits/description/

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        def addd(n):
            s = 0
            while(n > 0):
                s += n % 10
                n //= 10
            return s

        while(num // 10 != 0):
            num = addd(num)
        return num

# Base Case Check:
# If the input number num is 0, the result is 0 because the digital root of 0 is 0.
# Divisibility Check:
# If num is divisible by 9, return 9. This is because any number that is a multiple of 9 has a digital root of 9 (except for 0).
# General Case:
# For all other numbers, return num % 9. This remainder gives the digital root directly. This is based on the properties of numbers and modulo arithmetic, which simplifies the process to a constant-time solution.

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0: return 0
        if num % 9 == 0: return 9
        else: return num % 9

# https://leetcode.com/problems/rotate-array/description/

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def reverse(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        n = len(nums)
        k %=n
        reverse(nums, 0, n-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, n-1)
        
        return nums

