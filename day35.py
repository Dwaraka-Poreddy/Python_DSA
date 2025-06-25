# https://leetcode.com/problems/valid-palindrome/description/

def isPalindrome(s):
        s1 = ""
        for i in range(len(s)):
            if (ord(s[i]) >= 97 and ord(s[i]) <=122) or (ord(s[i]) >= 48 and ord(s[i]) <=57):
                s1 += s[i]
            elif (ord(s[i]) >= 65 and ord(s[i]) <=90):
                s1 += chr(ord(s[i]) + 32)
            
        for i in range(len(s1)):
            if s1[i] != s1[len(s1)-1-i]:
                return False
        return True
        

print(isPalindrome("A man, a plan, a canal: Panama")) # True
print(isPalindrome("0P")) #False


# https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1676325325/

def removeDuplicates(nums):
        ans = 1
        prevEle = nums[0]
        for i in range(1, len(nums), 1):
            if nums[i] == '_':
                break
            elif nums[i] == prevEle:
                nums.pop(i)
                nums.insert(0,'_')
            else:
                ans += 1
                prevEle = nums[i]
        i = 0
        while nums[i] == "_":
            nums.pop(i)
        return ans

# using 2 pointer approach
def removeDuplicates(nums):
        ans = 1
        j = 1
        prevEle = nums[0]
        for i in range(1, len(nums), 1):
            if nums[i] != prevEle:
                nums[j] = nums[i]
                prevEle = nums[i]
                j += 1
        return j
        

# https://leetcode.com/problems/move-zeroes/submissions/1676355687/
# using 2 pointer approach
def moveZeroes(nums):
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums

# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# using dictionaries

def intersect(nums1, nums2):
        d1 = {}
        d2 = {}
        ans = []
        for num in nums1:
            if num not in d1:
                d1[num] = 1
            else:
                d1[num] += 1
        for num in nums2:
            if num not in d2:
                d2[num] = 1
            else:
                d2[num] += 1
        for num in d1:
            if num in d2:
                count = min(d1[num], d2[num])
                for i in range(count):
                    ans.append(num)
        return ans

# https://leetcode.com/problems/reverse-string/description/

def reverseString(s):
        for i in range(len(s)//2):
            s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]

# using 2 pointer approach
def reverseString(s):
        l = 0
        r = len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1