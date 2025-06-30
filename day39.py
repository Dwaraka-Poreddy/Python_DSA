# https://leetcode.com/problems/contains-duplicate/description/

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dt = {}
        for num in nums:
            if num in dt:
                return True
            else:
                dt[num] = 1
        return False

# https://leetcode.com/problems/contains-duplicate-ii/description/

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dt = {}
        lp = 0
        for i in range(len(nums)):
            if nums[i] in dt:
                dt[nums[i]] += 1
                return True
            else:
                dt[nums[i]] = 1
            if i - lp == k:
                dt[nums[lp]] -= 1
                if dt[nums[lp]] == 0:
                    dt.pop(nums[lp])
                lp += 1
        return False

# https://leetcode.com/problems/maximum-average-subarray-i/description/

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        lp = 0
        tempSum = 0
        ans = float('-inf')
        for i in range(len(nums)):
            tempSum+= nums[i]
            if i - lp == k - 1:
                ans = max(ans, float(tempSum)/k)
                tempSum -= nums[lp]
                lp += 1
        return ans

# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dt = {}
        ans = 0
        tempLen = 0
        for i in range(len(s)):
            if s[i] not in dt:
                dt[s[i]] = 1
                tempLen += 1
            else:
                ans = max(ans, tempLen)
                while(s[i] in dt):
                    dt.pop(s[i - tempLen])
                    tempLen -= 1
                dt[s[i]] = 1
                tempLen += 1
        return max(ans, tempLen)
            

# https://leetcode.com/problems/fibonacci-number/

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)
        
# https://leetcode.com/problems/power-of-two/description/

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (n & (n - 1)) == 0


# https://leetcode.com/problems/reverse-linked-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head

# https://leetcode.com/problems/single-number/description/

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for num in nums:
            ans^=num
        return ans

# https://leetcode.com/problems/missing-number/description/


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        n = len(nums)
        for i in range(1, n+1):
            ans ^= i
        for num in nums:
            ans ^= num
        return ans