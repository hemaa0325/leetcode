class Solution(object):
    def maxProfit(self, prices):
        min_p = prices[0]
        best = 0
        for i in range(len(prices)):
            if prices[i]<min_p:
                min_p = prices[i]
            profit = prices[i]-min_p
            best = max(best,profit)
        return best