class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        num_stairs = len(cost)
        cost.append(0)
        memo = {}

        def dp(stair):
            if stair < 0:
                return 0
            
            if stair in memo:
                return memo[stair]
            
            memo[stair] = cost[stair] + min(dp(stair - 1), dp(stair - 2))
            return memo[stair]
        
        return dp(num_stairs)