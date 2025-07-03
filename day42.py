# https://leetcode.com/problems/palindrome-linked-list/submissions/1684788154/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head or not head.next:
            return True
        h1 = head
        slow = head
        fast = head
        p = head
        while fast and fast.next:
            fast = fast.next.next
            p = slow
            slow = slow.next
        if fast:
            slow = slow.next
        p.next = None
        h2 = slow
        prev = None
        current = slow
        while current:
            nn = current.next
            current.next = prev
            prev = current
            current = nn
        h2 = prev
        while h1 and h2:
            if h1.val != h2.val:
                return False
            else:
                h1 = h1.next
                h2 = h2.next
        if h1 or h2:
            return False
        else:
            return True

# Using Stack (extra space)

class Solution(object):
    def isPalindrome(self, head):
        stack = []
        slow = fast = head

        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next

        while slow:
            if stack.pop() != slow.val:
                return False
            slow = slow.next

        return True


# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        sum = 0
        current = head
        while current:
          sum = sum << 1
          sum += current.val
          current = current.next
        return sum
        

# https://leetcode.com/problems/delete-node-in-a-linked-list/description/

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev = None
        while node.next:
            prev = node
            node.val = node.next.val
            node = node.next  
        prev.next = None    

# Optimal O(1)
class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next  

# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return 
        len = 0
        curr = head
        while curr:
            len += 1
            curr = curr.next
        if n > len:
            return head
        k = len - n
        if k == 0:
            head = head.next
            return head
        curr = head
        prev = None
        for i in range(0, k-1):
            prev = curr
            curr = curr.next
        if curr.next:
            curr.next = curr.next.next
        return head

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        first, second = dummy, dummy
        for _ in range(n + 1):
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next

# https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = l1
        rem = 0
        curr = None
        while l1 and l2:
            sum = l1.val + l2.val + rem
            rem = sum/10
            l1.val = sum % 10
            curr = l1
            l1 = l1.next
            l2 = l2.next
        while l1:
            sum = l1.val + rem
            rem = sum/10
            l1.val = sum % 10
            curr = l1
            l1 = l1.next
        while l2:
            sum = l2.val + rem
            rem = sum/10
            l2.val = sum % 10
            curr.next = l2
            curr = curr.next
            l2 = l2.next
        if rem:
            new_node = ListNode(rem)
            curr.next = new_node
        
        return head
        
# Simple method
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = x + y + carry
            carry = total//10
            curr.next = ListNode(total%10)
            curr = curr.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next
    
        return dummy.next