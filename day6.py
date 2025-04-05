# https://leetcode.com/problems/score-of-a-string/submissions/1597573481/

def scoreOfString(self, s):
    score = 0
    for i in range(0, len(s)-1):
        score += abs(ord(s[i]) - ord(s[i+1]))
    return score