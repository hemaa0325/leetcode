class Solution(object):
    def maxProfit(self, prices):
        minp = prices[0]
        maxp = 0
        for price in prices:
            if minp>price:
                minp=price
            p=price-minp
            maxp=max(maxp,p)
        return maxp