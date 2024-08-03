class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = float('inf')
        maxP = 0

        for p in prices:
            min_buy = min(min_buy, p)

            maxP = max(maxP, p - min_buy)
        return maxP

