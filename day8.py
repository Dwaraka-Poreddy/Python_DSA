arr = [5, 7, 10, 11, 59, 34, 45, 23]
maxi = arr[0]
for i in arr:
    maxi = max(i, maxi)
    # if i > maxi:
    #     maxi = i
print(maxi)


# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/submissions/1597630514/
def mostWordsFound(sentences):
    maxi = 0
    for sentence in sentences:
        maxi = max(maxi, len(sentence.split(" ")))
    return maxi
sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
print(mostWordsFound(sentences))