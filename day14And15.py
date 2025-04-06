# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

def maxProfit(prices):
        lowestTillNow = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[i] - lowestTillNow)
            lowestTillNow = min(lowestTillNow, prices[i])
        return maxProfit 
 

print(maxProfit([7,1,5,3,6,4]))