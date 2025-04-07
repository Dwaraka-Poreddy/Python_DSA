# https://leetcode.com/problems/majority-element/description/
nums = [2,2,1,1,1,2,2]

#Using Dictionaries/HashMap
def majorityElement(nums):
    dic = {}
    for num in nums:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
    for i in dic:
        if dic[i] > len(nums)/2:
            return i


#Using Sorting
def majorityElement(nums):
    print(sorted(nums)[len(nums)//2])
    