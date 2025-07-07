# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if not nums:
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root.val > max(p.val,q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < min(p.val,q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

# https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        arr = []
        def _inord(r):
            if not r:
                return
            _inord(r.left)
            arr.append(r.val)
            _inord(r.right)
        _inord(root)
        maxDiff = float("+inf")
        print(arr)
        for i in range(1, len(arr)):
            maxDiff = min(maxDiff, abs(arr[i]-arr[i-1]))
        return maxDiff

#Without using extra array space

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.prev_val = None
        self.minDiff = float("inf")
        def _inord(r):
            if not r:
                return
            _inord(r.left)
            if self.prev_val is not None:
                self.minDiff = min(self.minDiff, r.val - self.prev_val)
            self.prev_val = r.val
            _inord(r.right)
        _inord(root)
        return self.minDiff