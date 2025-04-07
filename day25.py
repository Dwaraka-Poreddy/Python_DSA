# https://leetcode.com/problems/jewels-and-stones/description/

def numJewelsInStones(jewels, stones):
    ans = 0
    dic = {}
    for stone in stones:
        if stone in dic:
            dic[stone] +=1
        else:
            dic[stone] = 1
    
    for jewel in jewels:
        if jewel in dic:
            ans += dic[jewel]
    return ans

numJewelsInStones("aA", "aAAbbbb")
# 3