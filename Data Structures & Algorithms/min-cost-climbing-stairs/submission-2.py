class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        top = len(cost)
        memo = {}
        def climb(ind: int) -> int:
            if ind in memo:
                return memo[ind]
            if ind >=top:
                return 0
            res = cost[ind] + min(climb(ind+1), climb(ind+2))
            memo[ind] = res
            return res
        
        return min(climb(0), climb(1))
            