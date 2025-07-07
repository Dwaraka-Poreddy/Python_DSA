# https://leetcode.com/problems/increasing-order-search-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        arr = []
        def _in_ord(node):
            if node is None:
                return
            _in_ord(node.left)
            arr.append(node.val)
            _in_ord(node.right)
        _in_ord(root)
        print(arr)
        p = TreeNode(val =arr[0])
        k = p
        for i in range(1, len(arr)):
            k.right = TreeNode(val=arr[i])
            k = k.right
        return p

#without using extra array space


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        dummy = TreeNode(-1)
        self.cur = dummy
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            new_node = TreeNode(node.val)
            self.cur.right = new_node
            self.cur = new_node
            
            inorder(node.right)
        inorder(root)
        return dummy.right

# https://leetcode.com/problems/range-sum-of-bst/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        self.ans = 0
        def inord(node):
            if node is None:
                return 
            inord(node.left)
            if node.val >=low and node.val <=high:
                self.ans += node.val
            inord(node.right)
        inord(root)
        return self.ans

#Optimization by skipping unnecessary subtrees,
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        self.ans = 0
        def inord(node):
            if node is None:
                return 
            if not node.val < low:
                inord(node.left)
            if node.val >=low and node.val <=high:
                self.ans += node.val
            if not node.val > high:
                inord(node.right)
        inord(root)
        return self.ans

#Recursive approach
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        if not root:
            return 0
        
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        
        return (
            root.val +
            self.rangeSumBST(root.left, low, high) + 
            self.rangeSumBST(root.right, low, high)
        )

# https://leetcode.com/problems/insert-into-a-binary-search-tree/description/

#Recursive approach

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        def _insert(node, val):
            if node is None:
                return TreeNode(val)
            if val < node.val:
                node.left = _insert(node.left, val)
            else:
                node.right = _insert(node.right, val)
            return node
        return _insert(root, val)
        
#Iterative approach
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return TreeNode(val)
        
        curr = root
        while True:
            if val < curr.val:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = TreeNode(val)
                    break
            else:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = TreeNode(val)
                    break
            
        return root

# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        if head is None:
            return None
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        def arrToBST(arr):
            if not arr:
                return None
            mid = len(arr)//2
            root = TreeNode(arr[mid])
            root.right = arrToBST(arr[mid+1:])
            root.left = arrToBST(arr[:mid])
            return root
        return arrToBST(arr)
        
# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dt = {}
        for char in s:
            if char in dt:
                dt[char]+=1
            else:
                dt[char] = 1
        for i,char in enumerate(s):
            if dt[char] == 1:
                return i
        return -1        


# https://leetcode.com/problems/palindrome-number/description/

#By converting num into string
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        for i in range(len(s)):
            if s[i] != s[len(s)-i-1]:
                return False
        return True
#By reversing the number
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        rev = 0
        num = x
        while num != 0:
            rev = rev * 10 + num % 10
            num = num // 10
        return rev == x
#optimized
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rev = 0
        while rev < x:
            rev = rev * 10 + x % 10
            x = x // 10
        return rev == x or x == rev // 10

# https://leetcode.com/problems/roman-to-integer/description/

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dt = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        ans = 0
        for i in range(len(s)-1):
            if dt[s[i]] < dt[s[i+1]]:
                ans -= dt[s[i]]
            else:
                ans += dt[s[i]]
        ans += dt[s[-1]]
        return ans

# https://leetcode.com/problems/longest-common-prefix/description/

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        prefix = strs[0]
        for string in strs[1:]:
            while string.find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

        
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        ln = len(needle)
        s = ""
        for i in range(len(haystack)):
            s+=(haystack[i])
            if s == needle:
                return i-ln+1
            if len(s) == ln:
                s = s[1:]
        return -1

# https://leetcode.com/problems/plus-one/description/

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sum = digits[-1] + 1
        digits[-1] = sum % 10
        carry = sum // 10
        
        for i in range(len(digits)-2, -1, -1):
            sum = carry + digits[i]
            carry = sum // 10
            digits[i] = sum % 10
        if carry != 0:
            ans = [carry]
            ans.extend(digits)
            return ans
        else:
            return digits
        

# https://leetcode.com/problems/add-binary/description/

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        ans = ""
        while a or b:
            an = a[-1] if a else 0
            bn = b[-1] if b else 0
            if int(an)+int(bn) + carry == 2:
                carry = 1
                ans="0"+ans
            elif int(an)+int(bn) + carry == 3:
                carry = 1
                ans = "1"+ans
            else:
                ans = str(int(an)+int(bn) + carry) + ans
                carry = 0
            a = a[:-1]
            b = b[:-1]
        if carry:
            ans = str(carry) + ans
        return ans
        
        
# Optimized appraoch
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0

            total = digit_a + digit_b + carry
            result.append(str(total % 2))
            carry = total // 2

            i -= 1
            j -= 1
        return ''.join(reversed(result))
        
 #Using inbuilt function       
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a,2) + int(b,2))[2:]