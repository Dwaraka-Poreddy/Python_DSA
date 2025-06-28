# https://leetcode.com/problems/baseball-game/description/

class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []
        ans = 0
        for op in operations:
            if op == "C":
                if stack:
                    stack.pop()
            elif op == "D":
                if stack:
                    lastScore = stack[-1]
                    stack.append(2*lastScore)
            elif op == "+":
                if len(stack) > 1:
                    lastScore = stack[-1]
                    lastButOneScore = stack[-2]
                    stack.append(lastScore + lastButOneScore)
            else:
                stack.append(int(op))
        return sum(stack)

# https://leetcode.com/problems/minimize-string-length/description/

class Solution(object):
    def minimizedStringLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        se = set(s)
        return len(se)


# https://leetcode.com/problems/min-stack/submissions/1678025794/

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if self.minStack:
            val = min(val,self.minStack[-1])
        self.minStack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue(object):

    def __init__(self):
        self.s1=[]
        self.s2=[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())
        

    def pop(self):
        """
        :rtype: int
        """
        return self.s1.pop()

        

    def peek(self):
        """
        :rtype: int
        """
        return self.s1[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return not self.s1
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


# https://leetcode.com/problems/remove-outermost-parentheses/description/
class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        tempStr = ""
        depth = 0
        for char in s:
            if char == '(':
                if depth == 0:
                    depth += 1
                else:
                    depth += 1
                    tempStr += '('
            elif char == ')':
                if depth == 1:
                    depth -= 1
                    ans += tempStr
                    tempStr = ""
                else:
                    depth -= 1
                    tempStr += ")"

        return ans


# using stacks
def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        tempStr = ""
        stack = []
        for char in s:
            stack.append(char)
            tempStr += char
            if char ==')':
                stack.pop()
                stack.pop()
                if not stack:
                    ans += tempStr[1:-1]
                    tempStr = ""

        return ans


# https://leetcode.com/problems/make-the-string-great/

class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for char in s:
            if stack and abs(ord(char) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
        
# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(float(x) / y),
        }
        stack = []
        for token in tokens:
            if token in operations:
                b = stack.pop()
                a = stack.pop() 
                stack.append(operations[token](a, b))
            else:
                stack.append(int(token))
        return stack[0]
                
# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        ans = []
        stack = []
        for p in reversed(prices):

            while stack and stack[-1] > p:
                stack.pop()
            if not stack:
                stack.append(p)
                ans.append(p)
                continue
            else:
                ans.append(p - stack[-1])
                stack.append(p)
        ans.reverse()
        return ans
        

# https://leetcode.com/problems/daily-temperatures/description/

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        ans = []

        for i in range(len(temperatures)-1, -1, -1):
            t = temperatures[i]
            while stack and list(stack[-1].keys())[0] <= t:
                stack.pop()
            if not stack:
                stack.append({t:i})
                ans.append(0)
            else:
                ans.append(list(stack[-1].values())[0] - i)
                stack.append({t:i})
        ans.reverse()
        return ans
