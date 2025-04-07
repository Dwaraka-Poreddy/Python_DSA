# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/description/

def replaceElements(arr):
    length = len(arr)
    maxTillNow = arr[length - 1]
    arr[length - 1] = -1
    
    for i in range(length-2, -1, -1):
        currElement = arr[i]
        arr[i] = maxTillNow
        maxTillNow = max(maxTillNow, currElement)
    return arr
        
print(replaceElements([17,18,5,4,6,1]))