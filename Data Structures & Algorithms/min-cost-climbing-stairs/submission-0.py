class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        top = len(cost)
        def climb(ind: int) -> int:
            if ind >=top:
                return 0
            return cost[ind] + min(climb(ind+1), climb(ind+2))
        
        return min(climb(0), climb(1))
            