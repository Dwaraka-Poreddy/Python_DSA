# https://leetcode.com/problems/valid-parentheses/description/

# using deque for stack implementation
from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()
    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]
    def is_empty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = Stack()
        for char in s:
            if (stack.peek() == '{' and char == '}') or  (stack.peek() == '[' and char == ']') or  (stack.peek() == '(' and char == ')'):
                stack.pop()
            else:
                stack.push(char)
        return stack.is_empty()
        
        


# using list for stack implementation

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {')':'(', '}':'{', ']':'['}
        for char in s:
            if char in dict:
                if stack and stack[-1] == dict[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack


# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/

class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for char in s:
            if stack and stack[-1]==char:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)

# https://leetcode.com/problems/reverse-vowels-of-a-string/submissions/1677474043/

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')
        s = list(s)
        lp = 0
        rp = len(s) - 1
        while lp < rp:
            while lp < rp and s[lp] not in vowels:
                lp += 1
            while lp < rp and s[rp] not in vowels:
                rp -= 1
            s[lp], s[rp] = s[rp], s[lp]
            lp += 1
            rp -= 1
        return ''.join(s)