class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0:0, 1:1, 2:2}
        def recurse(n: int) -> int:
            if n in memo:
                return memo[n]
            res = recurse(n-1)+recurse(n-2)
            memo[n] = res
            return res
        

        return recurse(n)



        



        