class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        for i in range(len(prices)-1,0,-1):
            maxP = max(prices[i]-min(prices[0:i]), maxP)
        return maxP
            