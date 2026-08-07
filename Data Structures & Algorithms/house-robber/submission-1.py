class Solution:
    def rob(self, nums: List[int]) -> int:
        memo= {}
        def recurse(ind: int) -> int:
            if ind in memo:
                return memo[ind]
            if ind >=len(nums):
                return 0
            res =  max(recurse(ind+1), nums[ind]+recurse(ind+2))
            memo[ind] = res
            return res
        return max(recurse(0), recurse(1))