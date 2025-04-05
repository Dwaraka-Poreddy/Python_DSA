# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

def finalValueAfterOperations(operations):
    """
    :type operations: List[str]
    :rtype: int
    """
    ans = 0
    for operation in operations:
        if(operation == "--X" or operation == "X--"):
            ans -= 1
        else:
            ans += 1 
    return ans


# https://leetcode.com/problems/defanging-an-ip-address/
class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        ans = ""
        for char in address:
            if char == ".":
                ans += "[.]"
            else:
                ans += char
        return ans

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return "[.]".join(address.split("."))


# https://leetcode.com/problems/jewels-and-stones/submissions/1597603238/
def numJewelsInStones(jewels, stones):
    ans = 0
    for stone in stones:
        if stone in jewels:
            ans +=1
    return ans