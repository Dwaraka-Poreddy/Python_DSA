# https://leetcode.com/problems/decode-the-message/description/

def decodeMessage(key, message):
    dic = {}
    tracker = 97
    for k in key:
        if k == " ":
            continue
        elif k in dic:
            continue
        else:
            dic[k] = tracker
            tracker += 1
    ans = ""
    for m in message:
        if m == " ":
            ans += " "
        else:
            ans += chr(dic[m])
    return ans
    
print(decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"))
#this is a secret
print(decodeMessage("eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb"))
#the five boxing wizards jump quickly