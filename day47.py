# https://leetcode.com/problems/climbing-stairs/description/

#Using Fibonacci logic
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}
        def climb(n):
            if n in memo:
                return memo[n]
            if n == 1 or n == 2:
                memo[n] = n
                return n
            k = climb(n-1) + climb(n-2)
            memo[n] = k
            return  k
        return climb(n)

# https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ans = []
        def preOrdTrav(root):
            if root is None:
                return
            ans.append(root.val)
            preOrdTrav(root.left)
            preOrdTrav(root.right)
        preOrdTrav(root)
        return ans
        

# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ans = []
        def postOrdTrav(node):
            if node is None:
                return
            postOrdTrav(node.left)
            postOrdTrav(node.right)
            ans.append(node.val)
        postOrdTrav(root)
        return ans
        
        