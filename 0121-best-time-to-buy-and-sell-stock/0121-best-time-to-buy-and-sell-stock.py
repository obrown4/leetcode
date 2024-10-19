class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        min_buy = float('inf')
        profit = 0

        for p in prices:
            min_buy = min(min_buy, p)

            profit = max(profit, p - min_buy)
        return profit