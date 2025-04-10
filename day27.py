# https://leetcode.com/problems/isomorphic-strings/description/

def isIsomorphic(s, t):
    dic = {}
    rev = {}
    
    for i in range(len(s)):
        if s[i] not in dic and t[i] not in rev:
            dic[s[i]] = t[i]
            rev[t[i]] = s[i]
        elif s[i] in dic and dic[s[i]] != t[i]:
            return False
        elif t[i] in rev and rev[t[i]] != s[i]:
            return False
    return True
        
            
    
print(isIsomorphic("egg", "add"))
#True
print(isIsomorphic("badc", "baba"))
#False