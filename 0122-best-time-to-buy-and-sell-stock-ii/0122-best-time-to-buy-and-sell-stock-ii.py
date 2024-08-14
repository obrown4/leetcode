class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # understand
        # return the max profit 
        # stock only goes down --> return 0 

        # match 
        # dp bottom approach 
        # max profit at each day 

        # plan 
        # iterate through prices
        # hold the profit_if_not_holding
        # hold profit

        not_hold = 0
        hold = float('-inf')

        for p in prices:
            hold = max(hold, not_hold - p)
            not_hold = max(not_hold, hold + p)
        
        return not_hold