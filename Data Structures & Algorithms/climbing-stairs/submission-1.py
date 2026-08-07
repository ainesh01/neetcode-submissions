class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0]*(n+1)
        if n <=2:
            return n 
        memo[0] = 0
        memo[1] = 1
        memo[2] = 2
        def recurse(n: int) -> int:
            if memo[n]!=0:
                return memo[n]
            res = recurse(n-1)+recurse(n-2)
            memo[n] = res
            return res
        

        return recurse(n)



        



        