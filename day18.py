# https://leetcode.com/problems/two-furthest-houses-with-different-colors/description/

def maxDistance(colors):
    ans = 0
    for i in range(0, len(colors)):
        currentColIndex = i
        for j in range(i+1, len(colors)):
            if colors[j] != colors[currentColIndex]:
                ans = max(ans, j - currentColIndex)
    return ans
        
print(maxDistance([4,4,4,11,4,4,11,4,4,4,4,4]))


## Optimized solution
# The above solution has a time complexity of O(n^2) because it uses nested loops.
# We can optimize this to O(n) by observing the pattern. 
# Since there should be at least two different colors, one of the house with different color should obviously be at the start or end of the list to get the maximum distance between those 2 colors.
def maxDistance(colors):
    ans = 0
    currentColIndex = 0
    for i in range(0, len(colors)):
        if colors[i] != colors[currentColIndex]:
            ans = max(ans, i - currentColIndex)
            
    currentColIndex = len(colors)-1    
    for i in range(len(colors)-1, -1, -1):
        if colors[i] != colors[currentColIndex]:
            ans = max(ans, currentColIndex - i)
    return ans
        
print(maxDistance([4,4,4,11,4,4,11,4,4,4,4,4]))