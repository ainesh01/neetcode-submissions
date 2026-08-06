class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0

        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            prof = max(prof, price-lowest)
        return prof