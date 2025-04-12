# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/description/

def countGoodSubstrings(s):
    ans = 0
    l = 0
    dic = {}
    for r in range(len(s)):
        if s[r] in dic:
            dic[s[r]] += 1
        else:
            dic[s[r]] = 1
        if r-l == 3:
            dic[s[l]]-=1
            if dic[s[l]] == 0:
                dic.pop(s[l])
            l+=1
        if r-l+1 == 3:
            if len(dic)==3:
                ans+= 1
    return ans
    
print(countGoodSubstrings("xyzzaz"))
#1
print(countGoodSubstrings("aababcabc"))
#4
            